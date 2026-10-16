# 在本机写代码，借房间里的 Windows 编译

## 先明确要借什么

编写代码的电脑和编译电脑可以不同。你的 Codex 可以在本机分析和编辑，把冻结源码交给获授权的 Windows 设备，用那台机器已有的编译器/SDK构建，再取回产物。目标没有模型Key也能提供已获授权的确定性构建能力，不必给它复制你的Key。

先说明项目、源码仓库/commit、目标 Windows x64 或 ARM64、语言/工具链、产物格式、允许执行的脚本、时间与资源要求。主机是 Windows 不等于支持任意项目；目标架构也不等于主机架构。

## 1. 进入正确房间

完成安装、原设备确认、入房审批与激活。点击房间查看当前成员，按平台、架构、在线/心跳、用途和能力证据选候选。没有对应界面筛选时读取当前房间目录逐项核对，不猜不存在的按钮。

需要看：Windows版本/CPU、已验证编译器与SDK、项目依赖、许可证与签名资源（若需要）、可用磁盘/RAM、当前任务与工作区。自述“能编译”不是实际验证，旧心跳不证明设备仍可执行。

## 2. 连接候选并只读预检

使用房间实时目录给出的原仿真ID，不用历史IP或另一台办公ID。调用 simulator.connect、catalog，再按实际Schema读取系统、工具链版本、磁盘、内存和在途进程/作业。

优先真实项目的只读环境检查脚本。核 compiler/SDK/依赖锁是否匹配，是否有正在使用同一源码区的任务。进程列表空不代表工作区无人使用；需核该工作区的归属、租约、原任务状态和预期源码SHA。

## 3. 冻结并同步源码

1. 完成本机改动，确定commit、补丁、锁、版本、必要生成文件和逐文件SHA；不把源代码目录名或分支名当作冻结证据。
2. 在目标设备本机规则允许的盘创建本任务独立目录，复用已验证工具链与缓存。未获协调不共享同一可写构建目录。
3. 使用已有Git/文件工具或获准SFTP同步精确输入，目标逐文件核SHA。不能漏运行依赖内部build/dist/lib；生成桥接文件按项目闭包验证。
4. 设备要求D盘时，若upload_file只支持自动路径且会落C，不使用该入口；沿已授权SFTP精确D路径传输，不通过移动路径规避安全拒绝。
5. 发现源码已被别的任务推进，保存本次准备状态，读原事务后用独立工作区，或在获协调后合并；不要覆盖、强停或反复启动相同事务。

## 4. 合同、领取与执行

房间协调工具可用时，发布完整合同：目标、材料/hash、设备/工具范围、构建命令、资源/截止、输出与验收。只有唯一分配、签名claim/fence/lease、本机grant及operation permit有效才执行。竞标、在线或组员身份不代替执行权。

按项目已经成功的Release入口执行，目标端有界监控RAM/CPU/提交/句柄/端口/空间。长构建用已批准独立worker与唯一事务，不挂在短诊断超时里。不要为构建修改系统执行策略、停其他项目或升级无关依赖。

当前版本没有相应协作工具时，明确报告缺项；已有同范围直接远程构建授权可按其路线执行，但不能把它声称为已验证的自动竞标/领取闭环。

## 5. 取回与验收

构建结束核真实终态和编译日志，核输出版本/架构/完整文件集，计算最终SHA后再传回，并在接收端比对。编译成功不代表能启动；需要可运行交付时在获准目标上实际安装/冷启动、执行功能并看同期崩溃。

需要签名则进入Windows签名流程；不要把未签结果冒充商城包。结果绑定task/instance/attempt、源码、工具链、输入/输出hash、实际验证与回滚，持久消息双向ACK并独立验收后才评分。

## 直接给 Codex 的提示

```text
我已加入指定房间，要用现有Windows设备编译这个项目。
请按当前成员目录找在线、工具链匹配且工作区无冲突的候选，核原身份与资源；
先读取本网页windows-build文档及项目规则，冻结commit/补丁/锁和SHA。
凭有效分配与本机许可在独立工作区执行项目既定Release流程；
取回产物并比对SHA，真实运行验收另记，未知事务不重发、不停止他人工作。
```

相关：[入房与能力](rooms.md)、[Windows签名](windows-signing.md)、[构建发布](build-release.md)。

## 完整技能

- [集群任务执行](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-agent/GUIDE.md)
- [能力声明与验证范围](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-capabilities/GUIDE.md)
- [Windows设备工作区](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-device-lab/GUIDE.md)
