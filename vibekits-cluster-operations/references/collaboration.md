# 能力、消息及任务协作

能力先读 advanced.capabilities/system.capability_check/cluster.capabilities.read，修改经 cluster.capabilities.mutate，完整 device-capability/1 declaration，使用 expectedProfileRevision，冲突重读合并。sync_status 区分本地保存/待同步/云端 acceptedRevision。自述不写 verified/eligible/health，不复制模型 Key。详细 Schema 和方法见随包 capabilities 模块。

后台筛选在线、平台、关键词，展开设备的电脑名称、原 ID、办公 ID、版本、心跳、工具、能力证据、负载与权限。管理 MCP hbbv_room_devices 仅在当前 tools/list 存在时使用，按 nextCursor 全部分页。无 Key 设备可运行授权的确定性工具，但不能称自主模型就绪。

普通房间消息在网页登录原管理账号后选接收 ID/正文发送，不要求发送者仿真 ID。POST `/api/v1/manage/rooms/{roomId}/messages` body requestId/deviceIds/body；最多32设备、4096字符/16384字节，GET after/limit 增量合并 messageId。queued=服务器已存，received=设备持久 ACK，processed=设备回报处理；都不是业务独立验收。超时复用同 requestId 与完全相同正文，先对账再重试。消息不自动执行命令或调用计费模型。

真实任务：组长冻结合同/材料 hash/目标平台/原设备范围/工具/截止/分值/验收→原发布者签名 challenge→发布→候选能力分析竞标→唯一分配→签名 claim/fence/lease→本地 grant→每个外部操作 permit→执行→完整消息/产物/ACK→独立验收→积分。只有竞标、offers 或执行 scope 配置都不是执行许可。用实际 management MCP 和 cluster 工具，不猜 URL 或手写数据库状态。

断联先查原 taskId/instanceId/operationKey、租约及外部真实结果，未知安装/发布不能重复。合同要求新版本时核实际版本，已更高则 not_applicable，不降级凑任务。消息双方原身份、合同 hash、签名票据、工具回执和产物 hash 关联保存。详见随包 cluster-agent；后台内置旧指南与当前协议有差异时以实时合同及对应源码核验。
