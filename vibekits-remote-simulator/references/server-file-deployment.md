# 其他应用的文件上传与服务器部署

## 选择通道

服务器没有安装 VibeKits 时，使用开发工具中已保存的 SSH/SFTP 连接。远端只需可达的 SSH 服务、SFTP 子系统和具有目标目录权限的账号；不需要仿真 ID。已安装 VibeKits 并授权仿真的设备，才走 simulator 通道。profileId 是本机保存的服务器连接标识，routingId 是设备仿真标识，不能互换。

## 无 VibeKits 服务器：复用保存的连接

首次连接用 `vibekits.remote.open_interactive`（host 必填，user、port、openSftp 可选）打开原登录工作流，核验主机指纹并保存凭据。已有有效连接直接复用，不重复要求输入密码。密码和私钥留在系统凭据中，不写进对话、脚本、日志或文档。主机指纹变化须查明，不能跳过校验。

智能体调用当前注册工具，不需要在终端模拟键盘输入：

| 工具 | 参数 | 用途 |
|---|---|---|
| `vibekits.remote.list_profiles` | `{}` | 查保存的服务器，取得 profileId |
| `vibekits.remote.sftp_list` | profileId、remotePath（可选） | 查看远端目录 |
| `vibekits.remote.sftp_upload` | profileId、localPath、remotePath、overwrite（可选） | 上传单个文件，路径使用绝对路径；覆盖必须明确指定 |
| `vibekits.remote.sftp_download` | profileId、remotePath、localPath、overwrite（可选） | 下载日志或产物 |
| `vibekits.remote.ssh_exec` | profileId、command | 执行部署脚本和状态检查 |

例如上传参数：

```json
{"profileId":"<已保存连接ID>","localPath":"<本机包的绝对路径>","remotePath":"<远端暂存文件绝对路径>","overwrite":false}
```

部署前读取目标系统、架构、原服务和部署目录，核对当前任务授权的应用及精确路径。记录本地包字节数和 SHA-256，上传到本次任务独立暂存位置，再通过 ssh_exec 校验远端哈希。多文件应用可上传一个已验证归档再按项目原部署脚本解包；不能把上传成功当部署完成。

保留原配置、数据、身份、授权和可回退旧包。沿用该项目既定部署脚本，只替换任务要求的文件和服务。需要短暂停服时新包须先准备好，替换后立即恢复运行；失败按已准备的旧版本回退。验收真实版本、进程/服务状态和实际接口响应，检查工具结果的 ok、退出码、stdout/stderr，不能仅看调用或 SSH 成功。完成后只清理本次任务不再占用的暂存文件，不删除正式包、源码、其他任务或日志证据。

## 已装 VibeKits 的设备

按主技能先 `vibekits.simulator.connect` 验证身份、授权和连接，再查 catalog。上传使用 `vibekits.simulator.upload_file`，参数为 routingId、localPath，远端位置以工具返回为准，不假定路径。执行用 `vibekits.simulator.ssh_exec` 的 routingId、command；安装应用优先当前 catalog 中专用的 app_install/update 工具。同样校验上传哈希、版本和运行结果，完成后断开。Windows 命令编码与脚本执行沿用主技能，不改变执行策略。

## SFTP 目录兼容性记录

Linux/POSIX 文件名中的反斜杠是合法普通字符；SFTP 路径分隔符为正斜杠。客户端不能因某个名字含反斜杠就拒绝整个目录，也不能把它转换成路径分隔符。仍拒绝 NUL、正斜杠和越界条目，跳过 . 与 ..，保留目录数量和超时限制。下载到 Windows 时先拒绝不能安全表示的本地名称，不能通过放宽本地路径边界解决。

2026-10-08 现场：SSH 正常，默认 /root 中四个含反斜杠的旧条目触发客户端新增的名称检查；/opt 和 /opt/kemi-gm/swdol 没有这些条目。条目时间早于本次故障，不能据此断言服务端今天变化。修复后须实际验证这三个目录，而非仅编译通过。
