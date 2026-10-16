# 使用房间 Windows 签名能力

## 发现既有签名节点

先加入管理员指定房间，查看成员能力与当前验证证据，选择具备 Windows、AuthentiCode、硬件令牌与活动桌面的节点。由房间实际目录取得仿真 ID；不要硬编码历史机器、IP或驱动器映射。核原指纹、当前用户/Session、签名证书指纹/有效期、令牌可用性、负载与执行范围。

完整固定链与脚本见统一技能包的 kemi-windows-remote-signing 模块。请求签名不等于获准发布，也不能借用另一个 App 的身份。

## 提交签名合同

提供项目与应用身份、冻结源码/版本、完整未签 Release 树及清单 SHA、目标文件范围、预期证书、时间戳要求、输出格式、回滚、交付位置和独立验收条件。保持相同 AppId/原应用签名身份，正式包不可混编。

在房间合同/唯一分配/签名租约/本地 grant/operation permit 或同范围明确授权均有效后，才能调用实际设备工具。能力自述或管理员角色不是使用令牌的充分许可。

## 构建机与签名机

- 单机路线：在既有获准工作区构建和签名，不与另一构建混用目录。
- 已登记的双机路线：构建 A、令牌签名 B、Mac 控制与发布。复用已验证的受限挂载/回环转发，只暴露该版本产物，先比对 A 与 B 视图的 SHA；授权未覆盖的新共享/访问需按平台要求处理，不复制私钥。B 在挂载路径签，A核物理文件变化，再在A打外壳并由B签外壳。不能临时另起全盘共享。

具体盘路径以设备约束为准；本团队既有 Windows 签名工作站沿 D:/KEMI-Test。其他设备不得擅自照搬或在受限 C 盘编译。

## 固定启动链

```text
VibeKits app_control（活动登录桌面）
  → 固定 GUI 签名启动器 EXE
  → 固定 BAT
  → 固定 PowerShell 签名脚本
  → signtool
  → 硬件令牌当次确认
```

SSH只检查、暂存、核哈希和读结果；不能在 Session0 直接运行 BAT 期待出现 PIN，也不把签名改成 ScheduledTask。按当前 catalog Schema 启动获批准且哈希绑定的 GUI 启动器，不接收任意命令。

工具或系统明确拒绝时，保留原事务并诊断，不能改执行策略、把被拒脚本改内联、换包装器或身份绕过。

## PIN 与跟踪

核实当前 SignTool PID、创建时间、用户/Session、PIN 窗口来源与输入前空框，展示检查过的窗口截图，再请签名人只在设备窗口输入并确认。不要在聊天索取、读取、复制或自动填写 PIN；请求输入后不再截图输入状态。黑屏按已登记 Session1/桌面恢复路线处理，不重复签名。

始终跟踪同一 runId/attempt 的状态、进程与报告；内层与安装器外壳可能各需一次认证，分别由对应新窗口证明，不能假设PIN缓存。

## 签名与交付验收

先签所有本方内层 PE/.node/辅助程序，原厂文件按原字节和签名保留；再制作完整安装器并签外壳。每轮核新最终 PASS、清单数量、预期证书、有效时间戳、SignTool 全量验证和签后 SHA。退出0、窗口消失或老报告不是完成。

签完只交付同一最终字节，并在获准测试设备安装、冷启动、真实功能/模型/MCP、原 ID/权限/会话及回滚验收。上架另按应用发布授权与商城流程。结果未知对账原run、日志和实际文件，不再签一次。

## 给 Codex 的任务示例

```text
我已获授权使用当前房间的 Windows 硬件签名能力。
请先发现当前可用签名设备并核原身份、用户/Session、证书与运行负载；
读取完整 room-signing 和 windows-remote-signing 流程。
核我提供的项目合同、产物清单与 SHA，凭有效分配和本机许可执行固定签名链；
PIN 只交签名人在设备窗口输入。先核原事务，再报告内外层签名、精确产物与未验项。
```

## 完整技能与深入阅读

- [房间签名能力](https://github.com/caucy2026/skills-group/blob/main/vibekits-room-signing/SKILL.md)
- [固定远程签名链](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-remote-signing/GUIDE.md)
- [签名详细工作流](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-remote-signing/references/workflow.md)
- [实机工作区](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-device-lab/GUIDE.md)
