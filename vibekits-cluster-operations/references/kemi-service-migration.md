# Kemi业务与Newlink通用服务：接手要点

这是2026-10-23本团队生产案例，换部署先核实时serverId、customer、设备身份与用户授权，不把旧设备表当任意设备操作许可。历史迁移证据见hbbv/docs/acceptance/KEMI_ROOMS_PRODUCTION_20261023.md；自动服务最新生产回执见[技能库验收文档](../../docs/acceptance/SERVICE_AUTO_PRODUCTION_20261025.md)。

## 当前入口与边界

- 同一台设备当前只配置一个服务域名，域内可加入多个房间。当前生产HTTPS为 https://kemi-chat.newlinksz.com:21122 ，管理入口 /manage，公开分发入口 /vibekits/。
- 业务customer为kemi；本批默认“kemi 通用测试房”，ID c0985cc4dfeedaf71515ae029fc4cc4f。newlink作为独立服务父系，只保留“通用服务1”，ID f450c684b868292f67c534b793e26314。设备当前业务customer不等于管理员权限范围或账号身份；只能看到自己的业务房及自己有效加入的服务房。
- 普通业务房按当前同customer、批准成员、等级和原生证据决定互访。服务房普通设备互不可见/不可访，只有实际有权限的管理员按级别服务。用户注册普通会员，管理员由保留admin账号按客户/通用类型提拔；资源owner不是登录账号，也不是租户隔离依据。
- 已有八台可信登记设备在本批受用户明确授权后迁入kemi；这不授予未知设备普通互通房资格。普通业务房入房仍走签名申请及获授权审批。生产自动服务分配已于2026-10-25启用，4台既有真实设备签名resolve并保持原token/epoch/owner；不能把这批回补冒称无人值守全新安装或重装找回已验收。

## 已有设备看不到Kemi房间时

先查实际后台房间customer与客户端持久customer。新版本保留旧配置，升级包版本本身不会把旧newlink配置改成kemi。不得只改房间显示文本或只写后台approved当作接入成功。

本批已验证路线：冻结通过的后台main，私有本地一致性快照及独立工作副本演练，保留身份/钥/全部启动参数后部署；业务房保留ID迁kemi，原服务关系按原安装指纹和成员版本保留。对每台设备先验证原ID、实际目录和现有授权，再调用原Schema：

```json
{"toolId":"vibekits.cluster.configure","arguments":{"serverOrigin":"https://kemi-chat.newlinksz.com:21122","customerId":"kemi"}}
```

从外部控制端通过simulator.call指定真实routingId；本机可用注册工具直接调用。先查catalog，工具标识字段可能是name。相同origin省略签名公钥/CA等字段可保留原信任；换服务器另行核验，不能抹掉有效配置。旧Linux可能返回transport=relay而非p2p_or_relay字面值，核实际身份/SSH指纹、MCP ready和主机，不因此反复重连。

配置后首个rooms可能为空且“发现中”，等原同步推进再读。必须同时证明客户端customer=kemi、目标成员approved、roomsAreLive/connected、原ID以及后台新心跳。旧token/安装钥保持不变，不复制原生pin或伪造账号绑定。账号跨客户登录延续另行验收，不把设备凭据不变等同登录已验。当前处于用户暂缓或离线保护的设备从最新台账获取，不能因该机后台仍有记录而自动解除暂缓。

原七台的617由用户确认关机/断网时保持不连接。2026-10-26后台只读核其业务customer仍是newlink、Kemi测试房属于kemi且无pending邀请；同owner不跳过客户隔离，普通邀请/自动服务resolve不能代替既有设备customer迁移，原`migrate_kemi_device.py`还明确把617列为`DEVICE_ON_HOLD`。待原机恢复后再核原签名身份、当前包与客户端持久配置，按已授权正式迁移/申请路径入Kemi房；不得预先SQL改customer、造批准或拿另一台Linux替代。见[617离线作用域回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G01_OFFLINE617_KEMI_CUSTOMER_SCOPE_20261026.md)。

维护脚本tool/migrate_kemi_rooms.py和migrate_kemi_device.py只用于本次经批准的既有登记身份迁移，不能用于未知ID、首次consent_pending、黑名单或撤销设备，也不是普通入房的数据库审批绕过方法。只读SSH回执和SFTP具备时复用受信保存档案；不取出密码/Key写进文档。

## 重复房与数据保护

本次重复来自旧版按不同管理员各生成一套默认模板。2026-10-26 已在生产将十个已隐藏、无成员和业务引用的归档重复房间一次事务退休：`rooms` 20→10、退休回执10条，原十个正式房间 ID、成员、设备和业务任务保持；原事件元数据进入退休回执，审计记录保留。[完整生产验收](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/DUPLICATE_DEFAULT_ROOM_RETIREMENT_PRODUCTION_20261026.md)。不要再把这十个入口描述为仍待删除。

再次部署后台时保留主线 `app.py` 的非 admin 默认房间防重建修复；回退到旧版前须先核对其是否会重新造房，不能只恢复旧代码。其他环境若出现类似重复，先只读核实确实无成员、任务、草稿、邀请、申请、消息和仿真上下文；只落本地的一致性备份验证成功后，使用当前主线的 `default_room_retirement.py` 与一次性维护入口，固定 serverId、精确房间 ID 和只读计划摘要，持部署锁单事务执行，读回正式房间及退休回执。不要直接删 `room_defaults` 映射或复用本案例的房间 ID 和计划摘要。

生产仅本地保留最近3份已验证数据库快照；独立迁移工作副本用完核无引用后清理。云端不建数据库备份，项目与门户合计不超过3,000,000,000分配字节；按cloud-build-cleanup保留正式release和外部门户链接，核验后清自有测试/传输暂存。不是删正式DB/WAL来达标。

## 房间仿真验收与本批首败

同一控制器的房间签名请求按原SingleFlight串行。同请求BUSY先查原requestId是否签过票和原操作终态，不换ID盲重试。room_connect返回tunnelPrepared=true、connected=false可以是正常延迟握手；立即room_call同一票据工具，完成后只关闭自有room_disconnect，不清旧授权或同事原连接。

2026-10-23本批两台Linux的房间调用曾返回ROOM_SIMULATION_NATIVE_POLICY_INACTIVE；该首败保留。2026-10-25已用原ID155→ARM64 Linux571在kemi业务房完成一次签名房间短票据`system.info`：room_connect为tunnelPrepared=true/connected=false，立即同票据room_call实际成功，room_disconnect关闭自有通道，服务端同委派ID的领取及完成均读回；目标当时modelReady=false，证明这项确定性只读资源不依赖模型。参见[真实验收](../../docs/acceptance/G04_G08_LINUX_ARM64_NO_MODEL_ROOM_20261025.md)。另一Linux、编译/签名工具、撤销矩阵及所有房间仍未因此通过。遇到原native错误时仍须查server/room/target、激活/过期、工具/限额和实际安装包，不能关闭安全检查或借普通白名单绕过。

同日原七台Windows619（旧732客户端，modelReady=false）在同一业务房也按此顺序完成一次只读`system.info`，Windows进程回执、服务端同票据领取/完成与自有断开均真实读回；见[Windows619验收](../../docs/acceptance/G04_G08_WINDOWS619_NO_MODEL_ROOM_20261025.md)。这验证的是跨平台单工具与当前权限，不扩大到编译、签名、撤销或全部原七台升级。

2026-10-26 又以两台**普通**旧版Windows（619/build732为控制端、424/build789为目标）对同一对设备做房间策略对照：在newlink通用服务房仅申请一次`system.info`即被`CUSTOMER_SIMULATION_ACCOUNT_BINDING_REQUIRED`拒绝，服务端该requestId委派数0；换成双方均approved的kemi业务房后，新requestId返回短票据，直接同票据`room_call`实际命中424，服务端领取/完成各1，最后关闭自有通道。见[真实正负矩阵](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G06_G08_OLD_WINDOWS_BUSINESS_SUPPORT_MATRIX_20261026.md)。跨房测试必须固定显式roomId、控制端/目标原ID及唯一只读工具；负控拒绝后不换ID盲试，正向准备阶段`connected=false`不替代实际调用。该单对矩阵仍不代表降级/退房/管理员撤权或全部客户、工具、设备通过。

入房和实时心跳已验证，最新同源签名包、实际互通修复、账号延续、任务闭环及长期/规模仍以完整G01–G10台账为准。
