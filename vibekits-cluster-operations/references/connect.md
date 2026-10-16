# 连接与身份

1. 盘点本机实际 VibeKits 进程、版本、仿真/集群开关、MCP 工具、服务器 origin/customerId、已批准房间、设备清单及正在执行的构建/签名/安装。保存脱敏基线。
2. Harness 内调用 `vibekits.simulator.connect({routingId:"原ID",roomId:"目标房间ID"})`；roomId 仅在当前 Schema 支持时传入。查 `connection_status`、`catalog`。房间委托常为 `room-delegated-on-demand`，SSH 可不就绪，不能因此判定 MCP 失败。
3. 对照原 ID、设备名称、主机指纹/安装身份；实际调用 `vibekits.simulator.call({routingId,toolId:"vibekits.system.info",arguments:{}})`。参数是 toolId，不是 name。取得真实主机/系统/进程后才称验通。
4. 外部 Mac 没有原生 MCP 时，在本技能 `references/modules/vibekits-remote-simulator/` 下执行：

```sh
ruby scripts/invoke.rb vibekits.simulator.connect '{"routingId":"123456789"}'
ruby scripts/invoke.rb vibekits.simulator.catalog '{"routingId":"123456789"}'
ruby scripts/invoke.rb vibekits.simulator.call '{"routingId":"123456789","toolId":"vibekits.system.info","arguments":{}}'
```

脚本只从当前用户可信回环桥读取认证，不打印或复制 token。检查每层 content/structuredContent/data 中的 ok/isError/exitCode，HTTP200 不是业务成功。桥重启后先读取新桥并按原身份重新连接，不重复未知状态的写操作。

服务器没有仿真 ID 时使用 `remote.list_profiles` → 核验 profileId/host/port/user/可信指纹 → `remote.ssh_exec({profileId,command})` 或 `remote.sftp_upload({profileId,localPath,remotePath,overwrite:false})`。查询 `system.describe_tool` 确认参数；无保存认证时走原登录工作台。身份变化先处理身份，不自动接受新指纹。

文件/进程/UI/日志优先用实际设备专用工具，限制输出大小。短 Windows 命令沿当前批准的 PowerShell 宿主；长脚本上传后 -File 执行。明确 UnauthorizedAccess 或工具拒绝不能通过改执行策略、换宿主或内联来绕过。用过的外部仿真连接在不影响其他工作时正常断开。
