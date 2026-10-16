# 远程仿真完整操作：从原 ID 到真实调用

## 入口与技能安装

原始云端技能目录：https://github.com/caucy2026/skills/tree/main/vibekits-remote-simulator 。团队同步副本：https://github.com/caucy2026/skills-group/tree/main/vibekits-remote-simulator 。安装整个目录（含 scripts、references），不能只下载 SKILL.md。默认安装到 ~/.codex/skills/，CODEX_HOME 已配置时用其 skills 子目录；已有同名目录先比较合并，保留本地定制。

下载网站：https://kemi-chat.newlinksz.com:21122/vibekits/ 。集群后台连接地址：https://kemi-chat.newlinksz.com:21122 （不要带网站路径）。仿真单机连接本身不要求先加入房间。

## 设备端准备

在目标电脑/PAD 正常启动 VibeKits，开启远程仿真，读取 6–16 位原仿真 ID 与电脑名称。办公远程桌面 ID 是另一标识。当前产品手动开启不应额外要求仿真密码；首次访问同意、本机系统权限仍保留。设备主人确认允许的工作范围，首次请求在目标端接受；等待、拒绝、撤销均不能当成功。

## Harness 内连接

直接使用注册 MCP 工具，不额外启动 Ruby/SSH：

```json
{"tool":"vibekits.simulator.connect","arguments":{"routingId":"<原仿真ID>"}}
```

核 connected=true、routingId、可信身份与 transport=p2p_or_relay，再读取 simulator.catalog 的当前 Schema。选一个目标实际提供的只读工具，按 Schema 填 arguments：

```json
{"tool":"vibekits.simulator.call","arguments":{"routingId":"<原仿真ID>","toolId":"<目录返回的实际工具ID>","arguments":{}}}
```

参数名是 toolId。层层检查 ok / isError / data / structuredContent / exitCode；HTTP200和外层ok不是业务成功。核对主机、平台、版本与原身份，成功读取目标事实后才算仿真验通。目录数量、房间绿点、模型可用分别判断。

## 外部 Mac 控制端

当当前智能体没有注册 Harness MCP 时，正常运行对应 VibeKits App，使用随包脚本：

```sh
SKILL_ROOT="${CODEX_HOME:-$HOME/.codex}/skills/vibekits-remote-simulator"
INVOKE="$SKILL_ROOT/scripts/invoke.rb"
# 把占位原ID换成用户授权的数字ID；不打印桥配置或 token。
ruby "$INVOKE" vibekits.simulator.connect '{"routingId":"<原ID>"}'
ruby "$INVOKE" vibekits.simulator.catalog '{"routingId":"<原ID>"}'
ruby "$INVOKE" vibekits.simulator.connection_status '{"routingId":"<原ID>"}'
```

桥脚本只连接本机可信回环端点，自动定位当前桥。配置文件存在不代表 App/桥仍活着。Windows Harness 使用注册 MCP；不要照搬 Mac Ruby 路径。

## 房间、权限与恢复

同房间有效成员可按 room-members 委托通信，不必另加逐设备手工白名单；原设备同意、工具范围、签名票据、本机权限仍生效。管理员不自动获得所有业务执行权。

| 状态 | 处理 |
|---|---|
| consent_pending | 保留原申请，等待目标当次同意，避免反复请求。 |
| remote_disabled | 目标须开启原仿真访问；ID不是绕过开关的凭据。 |
| identity_mismatch/主机指纹改变 | 停止目标修改，核实原身份；不换号、清数据或自动接受新指纹。 |
| App重启/切网后连接拒绝 | 先核本机控制桥，再核原连接/事务，不立即判断目标离线。 |
| MCP可用但SSH未ready | 按工具实际可用性操作；PAD不要求SSH。 |
| 断联且事务结果未知 | 查同一任务PID/创建时间、回执、真实版本，不重启安装/签名/删除事务。 |

在已有授权范围内使用登记的同机远程桌面或可信备用入口恢复；拒绝与身份异常不能换通道规避。Mac可远程登录但文件无权读取时，核“系统设置→通用→共享→远程登录旁ⓘ→允许远程用户对磁盘进行完全访问”；本人完成系统认证后，实际读取获授权文件验证。与屏幕录制、辅助功能权限分别检查。

## 收尾验收

记录原ID、身份、平台/版本、一个真实只读调用、实际改动与未验证项。仅断开自己不再使用的 simulator.disconnect 连接，不终止他人的会话。普通原始诊断最多24小时，错误警告崩溃最多7天并限量脱敏；不记录密码、PIN、token、聊天/剪贴板或文件正文。

PAD远程ADB继续阅读 [mac-pad-remote-adb.md](mac-pad-remote-adb.md)。
