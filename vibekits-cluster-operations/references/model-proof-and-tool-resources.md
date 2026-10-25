# 模型健康证明与房间工具资源

适用：模型状态 unknown、显式复验、模型未就绪设备的资源使用。先核当前服务/房间/原ID、已有授权及实时catalog；不采用文中历史设备快照替代当前对象。

## 分清状态

- credentialPresent 仅证明存在配置，不证明模型可调用；modelReady=false 也不能单独证明没安装模型或凭据失效。
- 当前 VerifiedModelGeneration 的健康证明有效期为5分钟，绑定runtime、模型选择和凭据标识；变更或到期会失去ready证明。核对目标版本的实际规则，不能把一次成功外推为永久健康，也不能因过期直接诊断为故障。
- 普通心跳不自动调用模型。需要复验时显式调用一次 `vibekits.cluster.model.verify`，保存原请求，随后读同一状态和新鲜心跳的modelReady/checkedAt。request_started不是通过；没有新checkedAt不能把描述ready当模型通过。不要循环请求来维持绿灯，失败、冷却和需明确恢复的门禁保留。
- ready证明不授予工具、成员资格或业务任务租约；这些仍分别核验。

## 使用房间确定性工具

无新鲜模型证明时，已授权设备仍可能提供文件、编译、系统等确定性能力。先读当前catalog和任务requiresModel合同；不把普通仿真工具成功冒充Harness竞标/执行租约通过，也不为测试清除真实模型凭据。

1. `vibekits.simulator.connection_status {routingId}` 核对控制端已有连接归属；外部控制器新建的直连只回收自己的连接。先核双方原ID/指纹、当前同房批准成员和目标实际catalog。
2. 按**当前schema**显式使用 `vibekits.simulator.room_connect {routingId:目标,roomId,toolId,requestId:新唯一ID}`。普通`simulator.connect`只接受其实际声明的参数，不能自行加`roomId`；不能回退旧白名单掩盖房间失败。准备阶段`tunnelPrepared=true/connected=false`仅表明短票据就绪，room-delegated-on-demand可能无需SSH ready。
3. 立即以同目标、同唯一工具调用`vibekits.simulator.room_call {routingId,toolId,arguments}`；只读可先用system.info，再用当前schema的`system.resources(samples=1,intervalMs=250)`等小预算工具。编译、写文件、签名另需自身合同/资源预算，不能由只读票据扩权；未知调用结果保留原requestId，不换票重做。
4. 检查外层、内层、目标结构化ok/isError及真实数值/身份；管理端按精确requestId核同房/controller/target、claimed=1/completed=1。模型健康心跳在调用前后均无可用模型时，只能证明这次确定性工具不依赖新鲜模型证明，不能推断目标没有安装模型。
5. finally调用`simulator.room_disconnect`并核closed；若外部控制器为了核身份另建直连，再单独关闭那条自建连接，不能断开他人连接。关闭负例不等于服务端退房/撤销负例，后者另验。

2026-10-21项目实证索引：`docs/acceptance/FLEET_MODEL739_ROOM_RESOURCES_20261021.md`。739曾取得一次新鲜模型证明；之后超过TTL回unknown。Windows619的modelReady=false/checkedAt=null时通过原房间完成系统/内存读取，关闭后not_connected。仅证明该确定性工具链，不是未配置模型机器的完整业务验收、长期稳定或七台统一升级通过。

2026-10-26新的[真机G04/G08回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G04_G08_NO_MODEL_ROOM_RESOURCES_REAL_20261026.md)：普通控制端424在kemi业务房对619取一次限定工具票据，目标在调用前后生产心跳可用模型0，真实资源回执CPU计数器可用/内存/存储数值，服务端领取和完成各1，连接已关闭。只保留脱敏数值与原回复SHA，原回复中的Top进程名、告警正文及票据全文已清。这个正例不代替最后统一包、编译/签名能力、管理员撤权或24/72小时。
