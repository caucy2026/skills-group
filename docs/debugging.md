# 调试方法与证据

## 最短有效路线

先读项目 AGENTS、本机规则、相关技能与最近成功记录，确定用户目标、原设备、允许副作用和现有事务。优先实际源码、版本、进程与有界日志，再用UI补充体验。不要只根据截图猜根因。

## 连接与发现

用原仿真 ID 连接、核身份，再读当前 catalog/Schema。先执行一个只读工具，分别确认 MCP、SSH、ADB、模型与房间心跳。需要升级/删除/发布的诊断不自动取得这些动作权限。

## 按问题查

- 应用启动：实际安装路径、版本、主进程/创建时间、窗口、当前启动阶段和同时间错误。没有dump/栈时保留未知，不把旧WER算新崩溃。
- UI：当前设备/窗口身份、前台/焦点、浏览模式、权限、首击、中文输入与实际结果；工具ACK或第二次成功不证明第一次正常。
- 文件：使用专用文件工具与精确获授权路径，验证读回哈希；Mac远程登录完全磁盘访问、App文件访问和屏幕权限分别处理。
- 资源：系统可用RAM/提交额度、App及helper进程族CPU/RSS/句柄/FD/TCP端口、当前业务负载。严格空闲前先证明没有其他任务，不停别人的工作凑低数字。
- Windows：使用目标端预算，纯DTO输出；读取文件先限大小，用.NET有界流和FileShare.ReadWrite，避免深度序列化PSProvider。控制端超时不证明远端已回收。
- PAD：通过本次动态ADB串口读取包/系统/Activity事实；双屏先确认真实display，已知不安全的GPU取图路线不复现。

## 长任务与未知结果

构建、签名、公证、升级各有唯一任务ID、PID/创建时间、意图、日志和终态；独立守护适配实际生命周期，短诊断预算不能杀掉正常长任务。单设备写事务串行，独立只读可并行。观察中断先读同一原任务，不重发。

## 日志和收尾

只收必要、限定时间/数量/字节的诊断。普通原始日志最多24小时，错误/警告/崩溃最多7天，并限量轮转；保存脱敏报告与证据索引，不记录Key/PIN/token、聊天/剪贴板或文件正文。仅清自己无占用的生成物，不删业务会话、源码、配置、签名材料和正式包。

报告区分已证事实、推断与未验：触发、版本/包SHA、原身份、命令/工具及退出码、错误、改动、复验和下一步。源码/夹具通过不冒充真机通过。

## 完整技能与深入阅读

- [Windows实机](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-device-lab/GUIDE.md)
- [Mac文件访问](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/mac-file-access.md)
- [全局运维](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/operations.md)
