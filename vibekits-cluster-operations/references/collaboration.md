# 能力、消息及任务协作

能力先读 advanced.capabilities/system.capability_check/cluster.capabilities.read，修改经 cluster.capabilities.mutate，完整 device-capability/1 declaration，使用 expectedProfileRevision，冲突重读合并。sync_status 区分本地保存/待同步/云端 acceptedRevision。自述不写 verified/eligible/health，不复制模型 Key。详细 Schema 和方法见随包 capabilities 模块。

后台筛选在线、平台、关键词，展开设备的电脑名称、原 ID、办公 ID、版本、心跳、工具、能力证据、负载与权限。管理 MCP hbbv_room_devices 仅在当前 tools/list 存在时使用，按 nextCursor 全部分页。无 Key 设备可运行授权的确定性工具，但不能称自主模型就绪。

普通房间消息在网页登录原管理账号后选接收 ID/正文发送，不要求发送者仿真 ID。POST `/api/v1/manage/rooms/{roomId}/messages` body requestId/deviceIds/body；最多32设备、4096字符/16384字节，GET after/limit 增量合并 messageId。queued=服务器已存，received=设备持久 ACK，processed=设备回报处理；都不是业务独立验收。超时复用同 requestId 与完全相同正文，先对账再重试。消息不自动执行命令或调用计费模型。

真实任务：组长冻结合同/材料 hash/目标平台/原设备范围/工具/截止/分值/验收→原发布者签名 challenge→发布→候选能力分析竞标→唯一分配→签名 claim/fence/lease→本地 grant→每个外部操作 permit→执行→完整消息/产物/ACK→独立验收→积分。只有竞标、offers 或执行 scope 配置都不是执行许可。用实际 management MCP 和 cluster 工具，不猜 URL 或手写数据库状态。

断联先查原 taskId/instanceId/operationKey、租约及外部真实结果，未知安装/发布不能重复。合同强制特定升级而本机已更高时可报not_applicable；若明确允许同版/更高零动作分支，则提交实际版本、签名和官方记录，零下载零安装，不记实际升级功，不能降级凑任务。消息双方原身份、合同 hash、签名票据、工具回执和产物 hash 关联保存。详见随包 cluster-agent；后台内置旧指南与当前协议有差异时以实时合同及对应源码核验。

## 结果、通知和独立验收

模型完成、结果镜像、对方持久入箱、processed ACK镜像、反向实际送达、独立验收分别核对。发送返回pending时保留原messageId/seq；不得换正文或新消息冒充重试。租约过期但原生会话确已停止且完整原结果可验证时，使用正式reconcile接口核原outputHash，不重做业务；对账到verifying不等于accept或加分。

核工具回执时，按callId/offset重组后台分片，检查总字节数、完整SHA和实际原生session_status的回执索引。MCP文本不一定是JSON：保留解析失败及原hash，不能重写原文冒充有效结构；关键事实须有可验证结构化来源。不要读取或发布SDK私有推理记录、授权envelope或宽范围原始进程内容。

排查入站通知慢时，检查接收回调是否同步等待反向ACK的仿真通知。入箱和ACK服务端镜像必须先持久完成；反向通知可留在原持久发件箱，由既有重试按原ID/序号送达，避免嵌套回调等待。显式processed仍由处理者决定，不伪造对方已收到。源码回归通过不等于已安装包具备该修复。

## 原生房间镜像过期的恢复边界

后台approved/consent有效与本机原生策略有效不是同一件事。先读原生拒绝、当前后台授权和公共本机策略元数据，核原服务器、设备、安装/原生公钥、成员修订、工具集、期限及资源上限。若明确撤销、身份变化或权限不足，不恢复授权；不得写数据库、策略文件或白名单来绕过。

只有后台原授权仍有效、原生只是镜像过期且仍属用户授权维护范围时，才可通过目标自己的正常签名工具做同范围重对账。遇到BUSY不清SingleFlight；先核原事务。若需受控重启，使用已验证的独立恢复入口，SDK忙碌/审批数、在途工具、精确PID/创建时间/路径/签名和数据指纹均核实后只重启原程序，不清数据或重复授权掩盖打包错误。

工具报错也可能后台已提交，必须读回同一修订和实际原生结果，再决定后续；不盲目重发。恢复后验证原ID、数据、真实房间短票调用及服务端claimed/completed，再观察至少一次同修订、同范围的自动续期。一次恢复或一个续期不等于全设备长期稳定；控制端本地BUSY未派发也不能误记成目标离线。
