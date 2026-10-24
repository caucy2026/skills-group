# G03 原客户历史任务日志核验与退休（2026-10-24）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 实际缺口

本机155已用原客户端真实读取原newlink任务的终态收据：原serverId、实例、fence=1及原会话匹配，accepted/accept、executionStopped、terminalConfirmed、processed ACK及审计哈希齐全；原SDK状态active=false、not-resumed。当前配置为kemi，当前任务与退休列表没有原实例。因此不能用当前命名空间为空证明原newlink日志已退休。

这项源码修复提供正常应用内的旧命名空间核验/归档，不需要外部读取Keychain秘密或切换当前配置。未修改真实旧日志、未删除聊天、未重启或部署客户端。

## 客户端入口

仅在实际catalog出现 `vibekits.cluster.tasks.historical_terminal` 后调用。参数为原customerId、mode（inspect或retire）、roomId、instanceId、fence及原sessionId；未启动预留省略sessionId。先inspect核原记录与archiveAllowed，再对同一目标retire，最后inspect读回retirementVerified及retiredAt。缺记录不伪造退休；存储或返回未知时先读同一目标，不反复写入。

整个工具保守标记writesData（inspect也一样），服从原工具授权；不能遇拒绝后改用SSH手工清Keychain。`force`、凭据、额外参数、非法ID/fence或模式均显式拒绝，不能只依赖catalog Schema提示。

## 约束

- 只使用当前已认证服务器，不接收任意origin或worker。原命名空间的已存serverId必须与当前服务器一致；当前命名空间不能走此入口。
- 必须当前无活跃/恢复任务，暂停本次期间自动领取，客户配置激活等待原事务完成；generation、原生调用预算和30秒截止检查拒绝迟到写入。
- 服务端收据必须经正常已授权协议读取并绑定原设备、房间、任务、实例、fence、会话、安全状态和原始结果/审核证据。已启动会话还要新鲜的原SDK停止证明；不启动模型、续租、补结果或重记评分。
- 写入前再次核原始存储和serverId，保留其他字段、实例及其他fence。只移除所选旧记录，追加限量审计摘要，写后读回；原配置和当前客户日志不变。
- 兼容原终态记录和原completion型退休记录；后者核原收据完整哈希。返回不含lease、原始journal、聊天或工具正文。错误解析也不回显私有原文。

## 验证

53个不同合同通过：34个核心归档、3个MCP授权/参数、2个真实Agent代码路径（合成HTTP/存储/原生状态）、14个原终态回归。实际Agent路径保持kemi配置与当前日志，成功归档newlink目标；原服务器不匹配时不取收据或写日志。最新main叠加本会话精确修改的6个源/测试文件静态检查无error/warning；已有info单列，不把它们当全项目绿测。

移除终态/原生eligibility检查的预先声明负控，确实执行“active native session remains pending”并失败，不以加载错误当负控。首次隔离准备缺package graph/资源和HTTP测试默认阻断、首轮MCP测试对Schema自动校验的错误预期均保留；纠正后不隐去原日志。

当前为已测试源码交付，不是最终签名App验收。需要下一合格客户端包含入口后，对原范围设备原命名空间执行真实inspect/retire/重启读回。原G01–G10仍未完成；不因该组件通过打断788或Windows在途构建/签名。

证据：本机release-gate/vibekits/g03-historical-journal-20261024-v1，以及hbbv发布根g03-local155-terminal-v1。主线投影基底及精确文件SHA保存在main-projection.json，公共源码归属与提交会话均为本会话。
