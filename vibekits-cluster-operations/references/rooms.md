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

普通协作房的有效成员使用room-members委托；售后房仅接受有效客户管理员，成员身份不授予互访。普通房有效成员不新增逐设备白名单。管理员另外显示独立标识。真实授权仍要求当前房间/身份、目标有效 consent、原生 P256 签名 envelope、原连接 generation、单次票据、工具范围及本机权限；没有同意时不造授权。

2026-10-26[已安装Mac132/799真机目录回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G06_G07_MAC132_799_ROOM_ROSTER_SCOPE_20261026.md)展示普通成员的两种视图：newlink通用服务1后台16台approved，132的`room_devices`仅返在线管理员155一台、不返回自己和其他普通设备；kemi普通业务房后台8台approved，132得到完整8/8（1管理员、7成员，含自己）。先核原serverId、安装身份、房间批准和目录真实结果，再判可见范围。这个目录数据验收不代替最终网页折叠、实时通知、管理员看全体或其他客户房间矩阵。

按当前catalog使用room_connect/room_call选择明确的房间范围；不向普通simulator.connect传未声明参数。若普通connect自动选择房间，也须从实际返回核authorizationMode=room-members、roomId、server/customer、transport与原身份，再做真实工具调用。按两方向检查：system.info、一个超出历史五项诊断的低副作用工具（如获授权文件差异读取）、调用审计与工具结果。目录265项不代表265项都验过。

必须区分：后台设备在线、MCP connected、SSH ready、模型 ready、任务执行授权。委托按需模式 SSH=false 可以正常调用 MCP。旧逻辑会话 expiry 显示离线但实际新票调用成功，需修复状态刷新，不放宽票据 TTL 或用永久白名单掩盖。

同步验收包括新成员、管理员新增/降级、电脑名、掉线/恢复、退出、撤销。收到变更刷新当前修订；断网显示最后更新时间和未知状态，不把缓存显示为在线。自动同范围续约不能旋转修订使在途有效票突然失效；显式撤销、降级、退房必须拒绝旧授权。未知执行结果不自动换票重做。

每机入房通过：原 ID+安装身份一致、客户端实时 connected/approved、正确服务新鲜心跳、真实只读 MCP、角色/名称同步。稳定性另按持续观察证明。

## 单工具原生票据的实际验通

隔离验证原生链路时，按实时Schema执行 simulator.room_connect（routingId、roomId、toolId、唯一requestId）→room_call（同目标、同工具、arguments）→finally room_disconnect。connect的tunnelPrepared和executionVerified=false只证明准备完成。票据短时有效，准备与调用连续执行；仅在已证明本地派发前过期时，才可重新申请只读检查，未知业务结果不得换票重做。

同时检查外层ok、MCP isError、structuredContent.ok及实际数据。有管理审计入口时，核对同一delegationId的controller/target、claimed和completed，无需读取授权envelope或密钥。实际Mac app_signature及Windows applications已验证可通过房间票据执行，但空软件列表不证明便携程序不存在或版本正确。TOOL_DENIED保留为范围拒绝，不放宽白名单、TTL或目标同意来凑通过。

2026-10-26旧Windows普通设备619与424的**两方向**实测可复用为正负例：在kemi业务房分别以新请求ID执行单次system.info，明确`authorizationMode=room-delegation`、真实目标PID及服务端同一委派`claimed=1/completed=1`，然后关闭；在newlink售后房分别返回`CUSTOMER_SIMULATION_ACCOUNT_BINDING_REQUIRED`且对应请求ID的服务端票据数为0，不继续调用目标。见[两方向旧端真机矩阵](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G06_G08_OLD_WINDOWS_BUSINESS_SUPPORT_MATRIX_20261026.md)。这只覆盖这对旧版普通设备和一个只读工具；最终统一包、管理员撤权及其他工具仍须各自验收。

短授权票据有独立保留期，调用后立即收集当前账本证据；已按保留策略清除的行不补造、不恢复成活票据。缺证据须明确列出，必要时仅对可重复只读检查取得新回执，不重做未知结果的业务操作。

反向测试可通过已有获授权通道调用对端控制器，分别记录编排通道与被测房间段。断开后的本地SESSION_EXPIRED不是成员退房或服务端撤销证据。心跳以last_seen和服务端阈值判断，presence的ended为空不足以证明在线；短采样不能覆盖历史共同间断、离线设备或长期稳定性。

newlink“通用服务1”保留原ID f450c684b868292f67c534b793e26314及成员，服务端已置售后/default/pinned标记并启用原生签名自动分配。4台既有真实设备resolve通过，旧728曾未置顶；全新安装首入、重装找回、退出恢复、多后台同时入房与跨后台退出仍待真机验收。按当前工具/UI核每个后端的房间、身份和退出结果。
