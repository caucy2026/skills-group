# 入房、退出和同房间仿真

## 客户端

设置保留集群开关、后台地址和客户 ID；房间列表、申请加入和退出在主界面“远程状态/仿真信息”入口操作。具体名称以实际版本为准，旧版本差异先记录。加入按钮紧跟房间名称，房间名称、ID、角色、在线数及状态一眼可见，设备名小号单行省略并可查看全文；列表可折叠，连接明细默认折叠。

1. `cluster.status` 保存脱敏旧配置。按目录调用 `cluster.configure`：serverOrigin、trustedHosts、trustedCertificatePem、serverSimulationId；公网可信证书不沿用旧自签 CA，不关闭 TLS。客户 ID 字段按当前 Schema，不猜参数。
2. 授权范围内 `cluster.set_enabled({enabled:true})`，仿真独立开启并 ready。`cluster.rooms` 等异步发现完成，核对 roomsAreLive/connected、正确服务/客户和目标 roomId。
3. `cluster.apply({roomId})` 提交一次；已邀请且支持的客户端带 invitationId。立即显示“申请中/等待审批”并禁重复点击，提交超时通过原申请状态对账；刷新和重启后仍按服务端 pending 恢复。只有明确拒绝、撤销、过期或不存在且允许重新申请时才能再次申请。
4. 管理员审批后客户端原安装身份激活，服务端产生新鲜心跳；查 approved、实际版本/主机、能力档案同步。历史 approved 行不是当前在线证据。
5. 退出从同一外部状态入口，按当前 catalog 的退房接口执行并核回成员/本地状态；退房应失效该房间会话/票据，不能修改另一房间资格。未提供接口时按实际 UI，不猜工具名。

后台邀请：输入单台/批量原 ID→读逐台回执→目标开启集群读取邀请→原签名申请→原管理审批→激活。POST `/api/v1/manage/rooms/{roomId}/room-invitations`，deviceIds/reason/expectedRevision，固定 Idempotency-Key。成功项不批量重放；响应后取消邀请与拒绝申请不同。邀请本身不打开设备集群、不批准身份、不授予执行。

## 成员互相仿真

同房间的有效成员使用 room-members 委托，不新增逐设备白名单。管理员另外显示独立标识。真实授权仍要求当前房间/身份、目标有效 consent、原生 P256 签名 envelope、原连接 generation、单次票据、工具范围及本机权限；没有同意时不造授权。

用普通 simulator.connect 选定 roomId，记录 authorizationMode=room-members、实际 transport、工具目录和目标身份，再经普通 simulator.call 做真实工具调用。按两方向检查：system.info、一个超出历史五项诊断的低副作用工具（如获授权文件差异读取）、调用审计与工具结果。目录265项不代表265项都验过。

必须区分：后台设备在线、MCP connected、SSH ready、模型 ready、任务执行授权。委托按需模式 SSH=false 可以正常调用 MCP。旧逻辑会话 expiry 显示离线但实际新票调用成功，需修复状态刷新，不放宽票据 TTL 或用永久白名单掩盖。

同步验收包括新成员、管理员新增/降级、电脑名、掉线/恢复、退出、撤销。收到变更刷新当前修订；断网显示最后更新时间和未知状态，不把缓存显示为在线。自动同范围续约不能旋转修订使在途有效票突然失效；显式撤销、降级、退房必须拒绝旧授权。未知执行结果不自动换票重做。

每机入房通过：原 ID+安装身份一致、客户端实时 connected/approved、正确服务新鲜心跳、真实只读 MCP、角色/名称同步。稳定性另按持续观察证明。

## 单工具原生票据的实际验通

隔离验证原生链路时，按实时Schema执行 simulator.room_connect（routingId、roomId、toolId、唯一requestId）→room_call（同目标、同工具、arguments）→finally room_disconnect。connect的tunnelPrepared和executionVerified=false只证明准备完成。票据短时有效，准备与调用连续执行；仅在已证明本地派发前过期时，才可重新申请只读检查，未知业务结果不得换票重做。

同时检查外层ok、MCP isError、structuredContent.ok及实际数据。有管理审计入口时，核对同一delegationId的controller/target、claimed和completed，无需读取授权envelope或密钥。实际Mac app_signature及Windows applications已验证可通过房间票据执行，但空软件列表不证明便携程序不存在或版本正确。TOOL_DENIED保留为范围拒绝，不放宽白名单、TTL或目标同意来凑通过。

反向测试可通过已有获授权通道调用对端控制器，分别记录编排通道与被测房间段。断开后的本地SESSION_EXPIRED不是成员退房或服务端撤销证据。心跳以last_seen和服务端阈值判断，presence的ended为空不足以证明在线；短采样不能覆盖历史共同间断、离线设备或长期稳定性。
