"""Finite LAN transfer of one public signed archive; no directory exposure."""
import argparse,hashlib,http.server,json,os,re,socket,time,signal,ipaddress
from pathlib import Path

def handler_for(filename,expected_sha,peer,deadline,receipt):
    filename=Path(filename);initial=filename.stat()
    identity=lambda s:(s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns)
    class Handler(http.server.BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def do_HEAD(self):self.send_archive(False)
        def do_GET(self):self.send_archive(True)
        def send_archive(self,body):
            if self.client_address[0]!=peer:self.send_error(403);return
            if self.path!='/package/'+expected_sha:self.send_error(404);return
            if time.monotonic()>=deadline:self.send_error(410);return
            if self.headers.get('If-Match', '"'+expected_sha+'"')!='"'+expected_sha+'"':self.send_error(412);return
            if identity(filename.stat())!=identity(initial):self.send_error(409);return
            start,end=0,initial.st_size-1;partial=False
            value=self.headers.get('Range')
            if value:
                match=re.fullmatch(r'bytes=(\d+)-(\d*)',value)
                if not match:self.send_error(416);return
                start=int(match[1]);end=int(match[2])if match[2]else end;partial=True
                if not 0<=start<=end<initial.st_size:self.send_error(416);return
            self.send_response(206 if partial else 200)
            self.send_header('Content-Type','application/octet-stream')
            self.send_header('Content-Length',str(end-start+1))
            self.send_header('Accept-Ranges','bytes');self.send_header('ETag','"'+expected_sha+'"')
            self.send_header('Cache-Control','no-store');self.send_header('Connection','close')
            if partial:self.send_header('Content-Range',f'bytes {start}-{end}/{initial.st_size}')
            self.end_headers();self.close_connection=True
            sent=0
            if body:
                self.connection.settimeout(15)
                try:
                    with filename.open('rb')as source:
                        source.seek(start)
                        while sent<end-start+1:
                            if time.monotonic()>=deadline:raise TimeoutError('TRANSFER_DEADLINE')
                            chunk=source.read(min(65536,end-start+1-sent))
                            if not chunk:raise OSError('SOURCE_SHORT_READ')
                            self.wfile.write(chunk);sent+=len(chunk)
                except (OSError,TimeoutError):
                    receipt.append(dict(start=start,end=end,sent=sent,complete=False));return
            receipt.append(dict(start=start,end=end,sent=sent,complete=(not body or sent==end-start+1)))
    return Handler

def validate_private_peer(bind,peer):
    for value in (bind,peer):
        address=ipaddress.IPv4Address(value)
        if not address.is_private or address.is_unspecified or address.is_multicast:
            raise ValueError("EXPLICIT_PRIVATE_UNICAST_IPV4_REQUIRED")

def main(lifetime_seconds=900):
    if os.name!="posix" or not hasattr(signal,"setitimer"):raise RuntimeError("POSIX_CONTROLLER_REQUIRED")
    if not 0<lifetime_seconds<=900:raise ValueError("MAXIMUM_900_SECOND_LIFETIME")
    expired=False
    def expire(signum,frame):
        nonlocal expired
        expired=True
        raise TimeoutError("SERVER_WALL_TIME_LIMIT")
    signal.signal(signal.SIGALRM,expire)
    signal.setitimer(signal.ITIMER_REAL,lifetime_seconds)
    p=argparse.ArgumentParser();p.add_argument('--intent',type=Path,required=True);p.add_argument('--bind',required=True);p.add_argument('--peer',required=True);p.add_argument('--state',type=Path,required=True);a=p.parse_args()
    validate_private_peer(a.bind,a.peer)
    assert not a.state.exists() and not a.state.with_name('provider-terminal.json').exists()
    intent=json.loads(a.intent.read_text());source=Path(intent['localTransferFile']);assert source.is_absolute() and source.is_file() and not source.is_symlink();h=hashlib.sha256();deadline=time.monotonic()+lifetime_seconds
    with source.open('rb')as f:
        for block in iter(lambda:f.read(1048576),b''):
            if time.monotonic()>=deadline:raise TimeoutError('PREPARATION_DEADLINE')
            h.update(block)
    assert h.hexdigest()==intent['sha256'] and source.stat().st_size==intent['bytes']
    receipt=[]
    server=http.server.HTTPServer((a.bind,0),handler_for(source,intent['sha256'],a.peer,deadline,receipt));server.timeout=1
    state=dict(pid=os.getpid(),bind=a.bind,peer=a.peer,port=server.server_port,sha256=intent['sha256'],bytes=intent['bytes'],startedAt=time.time(),expiresAfterSeconds=900)
    with a.state.open('x')as f:json.dump(state,f,indent=2)
    print(json.dumps(state),flush=True)
    def stop(signum,frame):raise KeyboardInterrupt()
    signal.signal(signal.SIGTERM,stop)
    try:
        while not expired and time.monotonic()<deadline:server.handle_request()
    except (KeyboardInterrupt,TimeoutError):pass
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);server.server_close();a.state.with_name('provider-terminal.json').write_text(json.dumps(dict(endedAt=time.time(),requests=receipt),indent=2))
if __name__=='__main__':main()
