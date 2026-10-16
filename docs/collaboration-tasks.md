# 从找设备到交付任务

## 所有协同需求先回答六个问题

1. 要什么结果：编译、测试、签名、调试、文件处理还是设备现场操作？目标平台/架构、材料和验收是什么？
2. 谁能做：当前获批成员、真实工具/组件、能力证据、模型/账号/许可证与资源是否匹配？
3. 谁获准做：设备原身份、房间角色、合同、唯一分配/租约、本机grant、外部操作permit是否有效？
4. 在哪里做：独立工作区、允许目录、输入SHA、缓存与输出如何隔离，是否有另一任务正在推进？
5. 如何回报：双方消息、问题、进度、结果、ACK、审计与产物hash如何持久化？
6. 如何证明完成：源/目标各自实际状态、功能与外部效果由谁独立验收、失败如何恢复？

## 三个常见入口

- 在自己的电脑编辑，借一台Windows编译：读[Windows构建场景](windows-build.md)。
- 需要Linux ARM64远端：读[架构与设备选择场景](linux-arm64.md)。
- 已有产物要用团队签名资源：读[Windows签名](windows-signing.md)或[Mac签名](mac-signing.md)。

PAD现场/ADB、跨设备调试、自更新、异常恢复和清理分别有对应手册。搜索文档可以用“ARM64”“PIN”“工作区”“更新失败”等关键词。

## 任务生命周期

发现成员与能力→只读预检→冻结合同/材料→发布和竞标→唯一allocation/claim/fence/lease→本机grant/operation permit→执行与持久进展→双向ACK/审计→独立review与评分。

同房间、管理员、竞标成功、收到消息或目录里有工具，都不自动等于执行许可。queued是服务端排队，received是持久收到，processed是设备回报已处理；三者都不是业务通过。

高级工具在当前客户端或服务端不可用时明确报告缺项。已授权的直接远程操作和完整房间自治闭环分开记，不以一次SSH命令冒充竞标领取验收。

## 协作边界与效率

- 无模型节点仍可执行已授权的确定性工具任务，推理在具备账号与实际模型能力的控制端进行，不复制Key。
- 同一工作区/设备的写事务串行；独立工作区的只读或构建可按资源并行。空闲进程不证明目录无人占用。
- 复用最近成功的工具链、脚本和缓存；先核版本/输入/当前差异，不反复从零搭环境。
- 读原task/instance/operationKey/PID/出生和回执。超时不重发安装/签名/发布，已高于目标版本不降级凑任务。
- 工具或平台明确拒绝不能换包装器、身份或通道规避。普通授权内恢复自行完成；本人密码/PIN、身份变化和平台强制边界保留。
- 故障发生后保首次证据，恢复原设备/任务/授权；不抢占其他会话，不删除业务数据。

## 最小任务材料模板

```text
目标与应用/项目：
房间与原设备范围：
目标OS/架构、工具链和依赖：
源码commit/补丁、输入清单与SHA：
允许的命令/工具、目录和副作用：
资源、截止、排队与唯一实例要求：
交付格式、输出位置、精确hash：
签名/发布权限（如适用）：
独立验收与回滚：
消息、ACK、审计和评分条件：
```

结果应写清实际完成、失败、未知与不适用，关联唯一实例/回执和最终字节。跨设备取回后再次比对SHA；只清本任务确认无占用的临时物，保留源码、正式包、必要回滚和脱敏证据。

## 完整技能

- [集群任务执行](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-agent/GUIDE.md)
- [能力声明与验证范围](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-capabilities/GUIDE.md)
- [Windows设备工作区](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-windows-device-lab/GUIDE.md)
