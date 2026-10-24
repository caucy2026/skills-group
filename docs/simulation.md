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

普通协作房的同客户已批准成员使用 room-members 委托；售后房不以成员关系授予互访；控制设备有效等级不低于目标时，无需逐设备额外白名单。访问更高等级设备需走原白名单/同意审批。普通设备默认为0级，账号等级不自动提升设备等级。

详见[房间与十级管理](rooms.md)及[分级全局技能](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/account-device-levels.md)。原安装身份、目标同意、票据/连接代次、工具权限和本机 OS 权限仍保留。管理员身份不等于可以执行任意业务。

## 分流与收尾

consent_pending 保留原申请；remote_disabled 核原开关；identity_mismatch/指纹变化停止修改并核实身份。断联先查本机桥和原事务，再用登记的同机桌面或可信入口恢复，不重放未知安装。完成后只断开本次不再使用的 simulator.disconnect 连接，交付真实平台/版本、调用与未验项。

## 完整技能与深入阅读

- [完整远程仿真技能](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/SKILL.md)
- [工具参数合同](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/tool-contract.md)
- [详细仿真流程](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/simulation-workflow.md)


## 禁止访问目录：目录及全部下级统一保护

**研发规划，尚未上线。当前客户端不能仅依据本说明认为目录已经受到保护。** 本节说明新增需求、使用交互和发布验收标准；最终包通过各平台真实验收后再标记可用。

计划入口为“设置 → 远程仿真 → 禁止访问目录”。在本机选择目录、等待原生策略确认生效后，列表显示受限目录及数量；可折叠查看，长路径悬停查看完整值。逐项“移除限制”只移除规则，不删除磁盘文件；远程调用方不能修改或关闭本机限制。

保护范围是**该目录本身、它的所有下级目录及文件，递归覆盖任意层级**，不能关闭递归，也不能通过对子目录单独放行绕过父目录。以后新建或移入的下级内容也自动受限。例如添加 `private/` 后，`private/a.txt`、`private/child/b.txt`、`private/child/grandchild/c.txt` 都禁止远程访问；外部的 `private-other/` 不因名字相似而被禁止。子目录若同时存在独立规则，只移除子规则不会解除父规则的保护。

拒绝范围包括列举、搜索、属性探测、读取、预览、下载、写入、上传覆盖、复制、移动、重命名和删除。操作的源或目标任一在保护树中就拒绝。普通仿真、房间委派、同账号协同、文件共享/SDK附件、SSH/Shell、SFTP、桌面间接读取及PAD远程ADB都必须受同一目标端限制；VibeKits管理员、同房成员、同账号或白名单不能覆盖本机拒绝。Phone没有被控仿真服务时不显示无效开关。

规则应跨重启、注销换号、退房和覆盖升级保留，目录暂不可用时不自动删除。新增规则期间显示“正在生效”，收回受影响的在途远程访问后才显示完成。限制路径仅保存在设备本地，不上传后台。已传给对方的字节或此前独立发布的副本无法追回；应用级限制也不承诺抵抗设备系统root/管理员直接篡改软件。

验收必须用可丢弃目录和随机测试文件覆盖：根文件、子目录、孙目录、十层深目录、新建/移入内容；所有层级逐项拒绝，外部对照正常。另测符号链接、Windows联接、硬链接、路径别名、链接替换、旧缓存、任意脚本、桌面代理与ADB，防止间接绕过。每个平台的最终包分别记录SHA、策略代次和真实结果；任何可用远程入口仍能读取受保护测试内容，该平台就不通过，不能只凭UI或路径单测宣称完成。

- [需求与边界](https://github.com/caucy2026/skills-group/blob/main/docs/REMOTE_PROTECTED_DIRECTORIES_REQUIREMENTS_20261024.md)
- [前后端及原生设计](https://github.com/caucy2026/skills-group/blob/main/docs/REMOTE_PROTECTED_DIRECTORIES_DESIGN_20261024.md)
- [完整验收清单](https://github.com/caucy2026/skills-group/blob/main/docs/REMOTE_PROTECTED_DIRECTORIES_ACCEPTANCE_20261024.md)
