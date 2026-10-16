# 入房、管理员与能力协作

## 入口与身份

客户端后台地址是 https://kemi-chat.newlinksz.com:21122 ，本团队 customerId=newlink。网页管理入口同站根目录 /，用已有获授权账号正常登录。后台账号、客户管理员与房间设备管理员是不同身份，账号名为 admin 不代表总管理。

默认通用房是 VibeKits 六机通用验收房（f450c684b868292f67c534b793e26314）。入房仍须本机原安装身份响应和管理员审批。

## 客户端加入与退出

从主界面远程状态/仿真信息操作。选择房间核名称与 roomId，点击一次申请，保持申请中/等待审批；超时先查原 applicationId，不重复申请。管理员批准后等客户端激活、实时心跳，再做原 ID 的真实只读调用。退出后验证成员资格、旧票据与相应委托失效，而不只是隐藏条目。

列表和明细可折叠；折叠不停止同步。设备信息应显示名称、原 ID、办公 ID（有时）、平台/版本、角色、在线与最后更新时间。缓存或绿灯不是执行证明。

## 管理员邀请与审批

- 先选择当前客户与正确房间。入口待审批消息可直接查看设备基本资料、原身份与申请，批准或拒绝。
- 手工输入或 UTF-8 TXT 文件，每行一个 6–16 位原 ID；解析、去重、确认列表后才邀请。常规单批最多100台，当前限制以界面为准。
- 逐台查看等待身份、等待响应、待审批、等待激活、已加入、拒绝、撤销或过期。缺设备资料显示未知，不编造。
- 未入房设备的管理员意向不代替审批。现有成员升降角色核 revision；普通成员入口不能暗中降级现管理员。降为组员与移出房间分别处理。

## 查找可用能力

加入后从客户端/后台成员列表和实际 cluster 工具目录发现设备，不把历史 IP 或本网页当固定设备表。公开网页不提供私有凭据或固定个人设备清单。

查看平台事实、能力自述、验证证据、模型、工具/组件、当前负载、最近心跳。能力声明不等于实测，也不等于授权。无模型设备可提供已获准的确定性构建、签名、ADB或文件资源；开放推理任务须真实模型就绪。

## 借用设备完成任务

1. 写清应用/项目、目标平台、材料与 SHA、输出/签名要求、允许副作用、截止、回滚和独立验收。
2. 检查当前获批设备与能力，核原身份、当前工具 Schema、资源与运行中的工作；不停止其他同事任务。
3. 房间任务须冻结合同，发布、竞标、唯一有效分配、claim/fence/lease、本地 grant 和 operation permit 均有效才执行。
4. 任务正文、问题、进展与结果进入持久账本并双向 ACK。queued/received/processed 都不是业务通过。
5. 独立检查实际外部效果与产物 hash 后 review/评分。过期/failed旧任务不重放，未知结果先对账原实例。

当前工具未提供或服务执行未开启时，如实报告 task_execution_unavailable。文档描述协作合同，不代表任意版本、所有设备已完成全链路验收。

## 签名资源怎么使用

选择当前已批准且声明/实测具备硬件令牌签名的 Windows 节点，或具有项目 Developer ID/公证能力的 Mac 节点。按“Windows 签名”和“Mac 签名”手册准备完整合同；证书、Keychain 和 PIN 留在签名设备，不复制给请求方。房间成员身份不会自动授予证书使用、发布账号或任意工具权限。

## 完整技能与深入阅读

- [后台管理](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/management.md)
- [入房与角色](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/rooms.md)
- [任务协作](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-agent/GUIDE.md)
- [能力声明](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-capabilities/GUIDE.md)
