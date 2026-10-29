# Phone 原生票据与同账号点对点协同

用于手机作为同账号电脑的远程操作界面，沿原 Native peer/1 的直连或加密中继继续会话、发送消息和传文件。手机只作发起方；没有集群和房间，不作为被仿真的 Host。先检查当前正式客户端和后台实际能力，不能把设计稿或旧测试结果当上线状态。

## 身份与传输分工

- 手机的账号安装身份是 `phone-<32hex>`，当前登录由本机 P256 安装私钥、Bearer 会话和 `account-phone-request/1` 每请求签名证明。原 RustDesk/Native 数字路由 ID 与 Root 签发的 Ed25519 原生公钥是同一 App 的**另一种身份**。数字路由用于原 peer 寻址，不取代 Phone 账号安装 ID；不能靠 HTTP 自报账号、仿真 ID、设备名称或复制证书推定同一设备。
- hbbv只负责账号登录、当前设备目录、原生双钥关联、12秒presence和原 `client-access/1` 短票据。聊天正文、会话同步、审批及文件仍走原 Native peer/1 直连或加密中继。新手机业务不得使用 hbbv `commands/results/events/files` 队列，也不得回退房间白名单来绕过同账号验证。
- `GET /api/v2/account/capabilities` 同时报告 `features.phoneNativePeerSource=true` 与 `features.phoneOriginalAccessTickets=true` 才可进入下面流程。`fullHarnessCollaborationReady=false` 表示完整真机业务未获验收，不等于这两个控制面功能未部署；反之两个能力为true也不证明手机可以实际聊天。

## 发起流程

1. 手机先完成自己的正常账号登录、安全验证与当前绑定；确认同账号目标电脑为在线 Native Host，且它的原生通道、12秒presence和远程开关实际可用。普通账号、设备和管理令牌不能互换。
2. 手机用现有 Bearer 加 `account-phone-request/1` P256 签名发送 `POST /api/v2/account/mobile/native-link/challenge`，JSON只有 `signedCertificate`（原Root签发给此手机数字原生路由的证书）。服务端核当前账号、Phone安装指纹、安全revision及证书后给60秒一次性 `linkId`、`signingPayloadBase64`、`domain`、`expiresAt`。以响应 `domain` 原字节加解码后的 `signingPayloadBase64` **原字节**作 P256 ECDSA/SHA256 签名，Base64作为 `phoneLinkSignature`；签名域为 `HBBV/ACCOUNT-PHONE-NATIVE-LINK/1\n`。
3. 同一手机App的原 Native producer在TLS `/api/v2/account/native/channel` 提交恰好这些offer字段：`schema=client-native-phone-open/1`、`serverId`、`customerId`、`installationId=phone-*`、当前P256 `publicKeyPem`、同一Root `signedCertificate`、`phoneLinkId`、`phoneLinkSignature`。不得附Host descriptor。收到 `client-native-phone-challenge/1` 的原始字节后，Ed25519对 `HBBV/ACCOUNT-PHONE-NATIVE-CHANNEL/1\n` + 原字节签名，P256对 `HBBV/ACCOUNT-PHONE-INSTALLATION-CHANNEL/1\n` + 同一原字节签名；以 `client-native-phone-proof/1` 的 `nativeSignature` 与 `installationSignature` 标准Base64提交。必须读到 `client-native-ready/1` 且 `phoneSourceOnly=true`、`executionAuthorized=false`，并核 Live broker generation，才进入票据环节。
4. 用同一已签Phone请求调用 `GET /api/v2/account/peer/access-trust`；每12秒内向 `POST /api/v2/account/peer/presence` 送当前 `sequence`、`nickname`。向 `POST /api/v2/account/peer/tickets/challenge` 送 `targetInstallationId=<同账号数字Host安装ID>`；Phone P256对 `HBBV/CLIENT-ACCESS-REQUEST/1\n` + 返回的 `signingPayloadBase64` 解码原字节签名，再以 `ticketId`、`signature` 请求 `POST /api/v2/account/peer/tickets/issue`。服务端签发的仍是原 `client-access/1` envelope，接收端必须验服务签名、目标身份和当前状态。手机号或Phone安装ID不能当target。
5. 将短票据交原 peer/1 通道，继续会话与文件；退出时 `POST /api/v2/account/peer/tickets/revoke` 只阻断后续服务端validate，Native/SDK仍须关闭已建连接。注销、换号、改密/安全revision、原生证书或密钥变化、producer断联、presence超时与票据到期都应阻断新票和再次校验；断联后恢复须重新完成当前证明，不复用旧generation。

## 排障与验收

- 按顺序定位：当前Phone登录与P256请求签名 → Root证书匹配数字路由 → 一次性link与两把密钥双签 → Live Native generation → Phone和目标Host各自12秒presence → 同账号原票 → 原peer/1真实业务。只看到设备目录、能力flag、票据或Native ready都不能宣称已能同步聊天。
- 负控至少覆盖：只有Bearer/只有Phone P256/只有Native key、错账号/服务器/安装ID/路由/证书/绑定revision、过期或重放link、Phone当Host或target、目标断联、改密/换号与撤销。真实正向需在最终签名包上验证Phone→Host会话读取/继续、消息、审批、文件及已建连接退场；iOS和Harmony分开验收。跨客户房间隔离与旧Host登录不因手机同账号而降级。
- 2026-10-26后端源码已在私有 `priv/hbbv` 主线实现并生产启用：12项Phone专项、99项Phone/Host/Native/票据/HTTP组合、全套1206项通过（3项跳过）；公网能力、原serverId和匿名401已读回。**当时真实已登录Phone与原peer/1正向仍未完成**，故不可把此历史记录写成手机版正式验收通过。按最新现场证据更新判断。

### 2026-10-29 Host控制预算生产状态与边界

原账号Host的精确三条签名控制路由：`GET /api/v2/account/host/peer/devices`、`POST .../access-trust`、`POST .../tickets/validate`，已在hbbv生产加载独立预算，每token最近60秒最多2048、全局最多12288；原普通Host签名请求128、结果分块POST96和全部nonce全局16384仍分别保留。先验当前账号/安装绑定、原Native连接代次、签名、时钟及全局nonce重放，之后才按**精确方法+路径**分类，查询串或换方法不能借控制预算。Phone P256控制预算在另一模块，不能把Host128或Host2048误写成Phone额度。预算拒绝码为`HOST_REQUEST_RATE_LIMIT`；只读公网`/api/v2/account/capabilities`不提供这项Host内部额度，不能靠该端点猜真实429归因。

具资格会话已按原服务身份一次切换到`20261029-host-native-control-budget-r1`，本次独立核运行`account_native_identity.py`SHA-256为`6003ce74614b40475bd417cd70d7ade20434e098d56659c236aa95b2f86d1949`、原`serverId`不变，项目分配量低于3GB、云端临时传输包已清；后续以**实时**PID、模块SHA及签名请求回执重新核。`fullHarnessCollaborationReady=false`仍表示手机真实会话、消息、文件、审批、撤权与断线恢复未完整验收，不能把额度上线当作业务完成。最新生产与真机缺项见[集群接续末尾](https://github.com/caucy2026/priv/blob/main/hbbv/docs/PROJECT_HANDOFF_VIBEKITS_CLUSTER_UPGRADE_ACCEPTANCE_20261011.md)。

完整字段与当次生产回执分别见[后端协议合同](https://github.com/caucy2026/priv/blob/main/hbbv/docs/development/ACCOUNT_PHONE_NATIVE_PEER_CONTROL_20261026.md)和[生产验收记录](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/PHONE_NATIVE_PEER_CONTROL_PRODUCTION_20261026.md)；有私有仓库权限时读取，无法访问时以上流程足以定位控制面，具体当前API仍以实时schema为准。
