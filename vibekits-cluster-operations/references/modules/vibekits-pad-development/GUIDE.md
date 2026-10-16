---
name: vibekits-pad-development
description: 接续 VibeKits Android PAD 源码开发、硬件能力集成、仿真与ADB排障、完整构建签名、历史回归及KEMI商城交付。用于PAD研发或交接；不用于服务器部署、桌面ID变更或单纯操作本机硬件。
---

# VibeKits PAD 开发全局技能

让接手者从已有源码、真实证据和成熟流程继续开发，交付能够安装、启动、注册、授权并执行实际任务的完整 APK。创建本技能不代表原任务已完成，也不创建新会话。

## 接手第一步

1. 读取工作目录及父目录适用的 AGENTS.md、LOCAL-ENVIRONMENT-RULES.md；只读核对 Git HEAD、dirty、正在运行的事务及同事归属，保护未提交内容。
2. 首次接续读取 [当前目标与现场](references/current-handoff.md)，明确继承 G01–G09；核对最新包、实际进程、日志及接口，不能照抄历史端口/PID。日期状态不等于实时状态。
3. 开发读 [源码与开发方法](references/development.md)；设备排障读 [调试路线](references/debugging.md)；构建交付读 [构建验收发布](references/build-release.md)。 原生库来源、历史编译或重编还须读 [原生构建来源追溯](references/native-build-provenance.md)。当前主机定位在 [环境与证据](references/environment-evidence.md)，这些路径不是所有同事的强制磁盘配置。

## 必须保持的边界

- 用户要求仅改 PAD 时，不操作服务器、不修改官方 Harness SDK，不修改桌面 ID 算法。PAD 自有组件属于 PAD 研发范围；已有具体阶段未修改 H5/C6/Builder，不构成用户长期禁止。仅在实际故障必需时最小修改自有组件，并验证同签覆盖、数据/开发签名连续性及真实功能；不把 SDK 官方核心与自有组件混为一类。共用逻辑只做必要最小改动，验证桌面兼容后才能 merge。
- 已授权同范围操作直接完成；普通允许窗口核对目标和来源后可操作。陌生控制端首次白名单、身份核验、PIN/密码及工具拒绝不能绕过。授权记录不能跨设备泛化。
- 未知写、安装、构建、签名、迁移事务先查原句柄和回执，不重复提交。远端失败不是整机离线；使用已登记同机备用恢复路线。
- APK 只用“传文件→远端 SHA→pm install”，禁止增量 adb install。63 有 DataLoader/eventfd/GPU 内核故障历史；仅主屏 D0、公共自身 AX，不使用 screenshot/screencap/MediaProjection/RTSP/GPU 抓图；不碰副屏外来程序。
- 备份/覆盖/卸载前核对活跃 SDK owner、任务、持久化及 snapshot cut；不得中断在途工作。原 Key、有效授权、会话、工作区与生成 APK 的完整字节均属于保留范围。

## 与已有技能分工

- 仿真与恢复：`vibekits-remote-simulator`，按其工具契约和 Mac→PAD 指南执行。
- PAD 通用资源与工具组合：`vibekits-pad-system-resources`；开发验证不等于每个客户需求都已满足。
- 历史事故硬门禁：`vibekits-release-error-preflight` 及当前项目矩阵，不能用本技能缩减。
- 实际行为与回归：`app-release-stability-gate`；触摸/等待：`apk-touch-feedback`。
- 商城：`kemi-market-publish`；客户端更新与组件：`kemi-market-integration`。
- 云端编译发生时：`cloud-build-cleanup`，保留最新正式包、源码、签名及证据。
- 技能更新/接续：`skill-creator`、`project-handoff`。只整理不投递其他人的会话。

## 完成标准

同一最终签名 APK 的适用历史回归、三类设备仿真、完整包、真实 Key 任务、数据连续性和兼容性通过；源码云端备份逐文件读回，商城元数据及 CDN 包字节一致并验证客户端安装/更新，现场清理完成。只通过构建、灯亮、已有白名单或上传不算完成。未通过项保留原证据和责任，不伪造 PASS、不删矩阵项。
