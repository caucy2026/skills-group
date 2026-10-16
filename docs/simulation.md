# 远程仿真完整流程

## 获取完整技能

原云端目录：https://github.com/caucy2026/skills/tree/main/vibekits-remote-simulator

团队副本：https://github.com/caucy2026/skills-group/tree/main/vibekits-remote-simulator

安装整个文件夹，保留 scripts 和 references。已有同名目录先比较合并，不覆盖本地定制。默认技能目录 ~/.codex/skills/，已设置 CODEX_HOME 时按自己的配置。

## 准备目标

目标正常运行 VibeKits、联网、开启远程仿真。核对电脑名称、原仿真 ID 与本次允许的工作。首次请求由目标确认，ID 不能绕过关闭的开关或拒绝。无需先索取公网 IP、SSH 账号、密码、私钥或办公软件密码。

## Harness 内的工具顺序

```json
{"tool":"vibekits.simulator.connect","arguments":{"routingId":"<目标原ID>"}}
```

核 connected=true、同一 routingId、可信身份、transport=p2p_or_relay。再读 simulator.catalog 的实际工具和 Schema：

```json
{"tool":"vibekits.simulator.catalog","arguments":{"routingId":"<目标原ID>"}}
```

选实际存在的只读工具，按其 Schema 填参数：

```json
{"tool":"vibekits.simulator.call","arguments":{"routingId":"<目标原ID>","toolId":"<目录中的工具ID>","arguments":{}}}
```

是 toolId，不是 toolName。逐层核 ok、isError、structuredContent、data 和 exitCode。HTTP200、目录数量与外层 ok 不能代替目标执行成功。优先系统、应用、进程、日志、UI 等专用工具，避免不必要的 shell。

## 外部 Mac 上的 Codex

仅在没有注册 Harness MCP 时使用随包 Ruby 桥：

```sh
SKILL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/vibekits-remote-simulator"
ruby "$SKILL_ROOT/scripts/invoke.rb" vibekits.simulator.connect '{"routingId":"<原ID>"}'
ruby "$SKILL_ROOT/scripts/invoke.rb" vibekits.simulator.catalog '{"routingId":"<原ID>"}'
```

先运行本机对应 VibeKits。脚本定位可信回环桥；不要打印 tool-bridge.json、token 或认证头。Windows Harness 使用实际注册 MCP，不能照搬 Mac 路径。

## 房间内互通

同房间有效成员使用 room-members 委托，无需逐设备手工白名单。原安装身份、目标同意、票据/连接代次、工具权限和本机 OS 权限仍保留。管理员身份不等于可以执行任意业务。

## 分流与收尾

consent_pending 保留原申请；remote_disabled 核原开关；identity_mismatch/指纹变化停止修改并核实身份。断联先查本机桥和原事务，再用登记的同机桌面或可信入口恢复，不重放未知安装。完成后只断开本次不再使用的 simulator.disconnect 连接，交付真实平台/版本、调用与未验项。

## 完整技能与深入阅读

- [完整远程仿真技能](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/SKILL.md)
- [工具参数合同](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/tool-contract.md)
- [详细仿真流程](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/simulation-workflow.md)
