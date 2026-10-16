---
name: vibekits-room-signing
description: 在已获授权的VibeKits房间内发现和使用现有Windows硬件令牌或Mac签名公证能力，核对身份、任务、固定签名流程和最终产物；不授予证书、发布账号或任意设备访问权限。
---

# 房间内的签名能力协作

先读项目、本机规则、当前房间目录及实际工具Schema。能力声明、管理员角色和执行授权分别验证。

1. 从获批房间发现节点，核原ID/可信身份、系统、工具、验证证据、负载与签名资源。不固定历史IP或个人设备ID，不索取密码、私钥、Key或PIN。
2. 冻结项目/应用身份、源码/锁、版本、完整输入清单/SHA、签名者、时间戳、输出、回滚及验收。业务任务需有效合同、唯一分配/租约、本机grant与operation permit；已有同范围直接授权按其范围执行。未知事务先对账，不重复签名、安装或发布。
3. Windows读[固定交互签名流程](references/windows.md)，并读取统一集群包的kemi-windows-remote-signing完整GUIDE与references/workflow.md。只走已批准固定GUI启动链；Session0不冒充桌面。PIN由签名人在设备窗口输入；明确拒绝不得改内联、包装器、身份或策略规避。
4. Mac读[项目签名与公证](references/macos.md)，复用项目既有脚本、节点Keychain/profile。不导出私钥，不借另一个App的Bundle ID、helper或凭据身份。内层先签、外层后签，保持原权限和指定要求。
5. 核当前run的完整报告/计数、签名/时间戳、精确字节/hash和真实安装功能。公证跟踪同一submissionId，Accepted后staple与最终归档读回。上架另需发布授权与完整门禁。
6. 关闭本任务闲置连接/临时进程，保留源码、签名材料、正式包、必要回滚和脱敏证据。云编译才执行cloud-build-cleanup。

完整团队技能及脚本：https://github.com/caucy2026/skills-group/tree/main/vibekits-cluster-operations 。获取整个目录，专项资料在references/modules按需读取，不只复制入口。工具缺失或执行未开启须报告真实不可用，文档不代表已经验收。
