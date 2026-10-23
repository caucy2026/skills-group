# VibeKits remote-simulation tool contract

Inside VibeKits Harness, call registered MCP tools directly. Use `vibekits.simulator.catalog` if a tool schema is not yet known. Never reveal local bridge credentials.

## Controller tools

- `vibekits.simulator.connect`: `routingId`.
- `vibekits.simulator.connection_status`: `routingId`.
- `vibekits.simulator.catalog`: `routingId`.
- `vibekits.simulator.call`: `routingId`, `toolId`, `arguments`.
- `vibekits.simulator.ssh_exec`: `routingId`, one exact `command`.
- `vibekits.simulator.upload_file`: `routingId`, `localPath`.
- `vibekits.simulator.download_file`: `routingId`, `remotePath`.
- `vibekits.simulator.screenshot`: `routingId`.
- `vibekits.simulator.disconnect`: `routingId`.

## Remote device tools

Call through `vibekits.simulator.call` with the current catalog schema:

- `vibekits.device.processes`: running state/resource use.
- `vibekits.device.applications`: installed identity/version/path.
- `vibekits.device.logs` and `vibekits.device.crash_reports`: bounded diagnostics.
- `vibekits.device.ui_inspect` and `vibekits.device.screenshot`: permitted visual/AX evidence.
- `vibekits.device.ui_action`: only for requested, non-destructive interaction or with explicit authority for consequential actions.
- `vibekits.device.app_control`, `vibekits.device.app_install`, `vibekits.device.app_uninstall`: only when in task scope.

Examples for an external macOS controller without the registered MCP tools, from this skill folder:

```bash
ruby scripts/invoke.rb vibekits.simulator.connect '{"routingId":"123456789"}'
ruby scripts/invoke.rb vibekits.simulator.call '{"routingId":"123456789","toolId":"vibekits.device.applications","arguments":{"limit":50}}'
ruby scripts/invoke.rb vibekits.simulator.disconnect '{"routingId":"123456789"}'
```

The loopback bridge can wrap tool results in `content` and `structuredContent`. Check nested `ok`, `connected`, identity, authorization and tool-result fields; HTTP success alone is insufficient. Redact secrets and cap output.

## 上传后校验未完成的恢复（2026-10-23）

保留原routingId、已返回的remotePath、字节数、本机正式源文件SHA256和原调用结果。源码df3a23945将“SCP完成但校验命令失败/无摘要”区分为upload_verification_unavailable，errorContext含copyCompleted=true、verificationCompleted=false及expectedSha256；expectedSha256是本机预期值，不是远端已验证值。此源码修复尚不证明当前安装的控制端已更新。

旧版可能把SSH校验失败误报为upload_checksum_mismatch。先对账原连接和原文件，再用已授权、身份与指纹匹配的同机通道只读核实际大小和完整SHA256；路径取工具实际返回/错误context或已核实的暂存记录，不猜临时路径，不盲目重传、覆盖或重复安装。真实摘要不符仍按不完整文件处理；没有取得可信远端摘要时保持未验证，不能放行安装或发布。

命令通道忙、断流或观察超时，先查原PID/创建时间、唯一作业与终态；保存的同机SSH可用于对账，不借备用通道跳过身份、权限、拒绝或共享作业占用。执行新编译时仍走该项目规定的原路线和最新main资格检查。源码/43项隔离回归与两台Linux实际收件核验分别记录，不能相互代替。详见[源码及验证范围](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/SIMULATOR_UPLOAD_VERIFICATION_OUTCOME_20261023.md)。
