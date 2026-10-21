# 模型健康证明与房间工具资源

适用：模型状态 unknown、显式复验、模型未就绪设备的资源使用。先核当前服务/房间/原ID、已有授权及实时catalog；不采用文中历史设备快照替代当前对象。

## 分清状态

- credentialPresent 仅证明存在配置，不证明模型可调用；modelReady=false 也不能单独证明没安装模型或凭据失效。
- 当前 VerifiedModelGeneration 的健康证明有效期为5分钟，绑定runtime、模型选择和凭据标识；变更或到期会失去ready证明。核对目标版本的实际规则，不能把一次成功外推为永久健康，也不能因过期直接诊断为故障。
- 普通心跳不自动调用模型。需要复验时显式调用一次 `vibekits.cluster.model.verify`，保存原请求，随后读同一状态和新鲜心跳的modelReady/checkedAt。request_started不是通过；没有新checkedAt不能把描述ready当模型通过。不要循环请求来维持绿灯，失败、冷却和需明确恢复的门禁保留。
- ready证明不授予工具、成员资格或业务任务租约；这些仍分别核验。

## 使用房间确定性工具

无新鲜模型证明时，已授权设备仍可能提供文件、编译、系统等确定性能力。先读当前catalog和任务requiresModel合同；不把普通仿真工具成功冒充Harness竞标/执行租约通过，也不为测试清除真实模型凭据。

1. `vibekits.simulator.connection_status {routingId}` 核对已有连接归属。只回收自己创建的连接。
2. 双方已批准入同一房间时，用 `vibekits.simulator.connect {routingId,roomId}` 精确选择房间；room-members/room-delegated-on-demand可能只有MCP，sshReady/transportReady=false不等于MCP失败。不能回退旧白名单来掩盖房间失败。
3. 获取目标实际catalog，然后用 `vibekits.simulator.call {routingId,toolId,arguments}` 执行目标支持、授权范围内的工具。只读可先用system.info；system.resources按当前schema和平台用小预算。编译、写文件、签名等使用各自既有合同/资源预算，不由只读例子扩权。
4. 检查每层结构化ok及真实结果；记录目标PID/时间、来源/目标ID、房间、版本证据层次及调用收尾。目录、取票、connected与真实执行成功分开。
5. 结束用simulator.disconnect回收自有连接，再确认connected=false。当前“不自动建连”的调用合同下，可用同一只读工具做一次关闭后拒绝负例；拒绝后不换通道重放。关闭负例不等于服务端退房/撤销负例，后者另验。

2026-10-21项目实证索引：`docs/acceptance/FLEET_MODEL739_ROOM_RESOURCES_20261021.md`。739曾取得一次新鲜模型证明；之后超过TTL回unknown。Windows619的modelReady=false/checkedAt=null时通过原房间完成系统/内存读取，关闭后not_connected。仅证明该确定性工具链，不是未配置模型机器的完整业务验收、长期稳定或七台统一升级通过。
