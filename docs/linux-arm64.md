# 寻找与使用 Linux ARM64 仿真设备

## 先说清“仿真”的含义

VibeKits远程仿真是按原设备ID操作远端；它不会把 x86_64 机器自动变成 ARM64。若需求是 ARM64 Linux，必须同时核操作系统与架构，并说明是否接受虚拟机、容器或跨架构CPU仿真。

- 原生 ARM64 Linux：物理CPU与系统环境匹配，适合需要原生性能/兼容性结论的任务。
- ARM64 Linux虚拟机：核客体系统/架构、宿主资源与虚拟化条件，结论限定该客体。
- 容器：核镜像平台、实际执行方式、宿主内核与权限边界；不能把镜像标签当真实架构或独立物理机。
- x86主机上的QEMU等ARM64仿真：只有用户允许、节点已有获准能力时使用，明确性能与硬件限制，不能冒称物理ARM64通过。

## 1. 从房间选择候选

在获批房间读取当前设备目录，按 Linux + arm64/aarch64 + 新鲜心跳筛选候选，继续看已验证工具、组件、磁盘/RAM、资源用途、实际负载与工作区。没有对应筛选界面就逐项读目录，不猜按钮或API。

本网页不提供虚构机器或固定私有ID。当前房间没有Linux/ARM64时，应明确“没有已验证候选”；不能把Mac ARM64、Linux x86_64或离线条目当作匹配。

## 2. 原ID连接并核实

按仿真完整流程 connect→catalog→实际只读工具，核原身份与主机。工具不足时，在本次授权与真实Schema允许的SSH执行入口逐条读取：

```sh
uname -s
uname -m
getconf LONG_BIT
```

预期系统Linux、架构aarch64（或明确等价arm64）和64位；还要核发行版、内核、运行环境与编译器目标。容器/QEMU可能报告客体aarch64，不能只凭uname判断物理CPU，须同时核宿主事实和节点虚拟化说明。

MCP ready、SSH ready、模型ready与房间在线分别验证。先完成一个真实只读调用，再提交业务。

## 3. 使用现有环境完成任务

写清项目/源码commit与hash、Linux发行版、原生或交叉编译要求、目标ABI、依赖/许可证、命令、资源/截止、交付物、回滚与验收。按有效房间合同、唯一分配/租约、本机grant与operation permit执行，不因“同房间”就开放任意shell或root。

建立独立工作区；复用该节点既定工具链/缓存，不默认sudo、全局装包或修改网络策略。跨编译时记录主机与目标各自架构；核产物ELF目标、动态依赖与目标环境实际启动，不把编译器返回0当兼容通过。

## 4. 当前没有合适节点怎么办

1. 先检查已登记且获授权的其他房间/资源与已有分工，不擅自派新任务或抢占节点。
2. 有已获批准的ARM64虚拟化/仿真能力时，按原部署脚本、资源与网络范围创建客体并验收；未覆盖的新访问、权限或系统要求按平台处理。
3. 也可请管理员让现有Linux ARM64设备安装正确正式客户端、开启仿真并完成原身份入房流程。Linux尚无正式商城包时，不猜下载URL或使用其他平台包替代。
4. 若只有已保存SSH/SFTP服务器，使用已授权profile工具；profileId不是routingId，该资源不自动成为房间原生仿真成员，仍需单独登记用途与许可。不能把生产房间服务本身当作默认编译机。

没有条件时说明缺的是设备、架构、工具链、资源还是权限；其他可独立工作继续。不要伪造一个可连接ID或把脚本/方案当作已经创建机器。

## 直接给 Codex 的提示

```text
我需要当前获批房间中一台Linux ARM64远程仿真设备。
先查实时目录与能力证据，区分物理ARM64、ARM64虚拟机、容器和x86上的CPU仿真；
用原ID核身份、Linux/aarch64、发行版、工具链、资源和当前工作，再做只读验通。
没有匹配候选时列出实际缺项和已授权现有资源方案，不虚构设备、不改系统策略。
具体任务按有效分配、最小工具范围、产物SHA与真实目标运行验收执行。
```

相关：[仿真连接](simulation.md)、[房间协作](rooms.md)、[异常恢复](recovery.md)。

## 完整技能

- [集群任务执行](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-agent/GUIDE.md)
- [能力声明与验证范围](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-capabilities/GUIDE.md)
- [Windows设备工作区](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-device-lab/GUIDE.md)
