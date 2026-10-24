# 旧设备登录自动接入同账号Host：接口合同

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

状态：已于2026-10-24部署，受信HTTPS核验features.hostLegacyBootstrap=true；详见[生产验收记录](../acceptance/HOST_BOOTSTRAP_PRODUCTION_20261024.md)。不是手机版必须换登录协议：Phone继续既有v2 API，本合同由桌面/PAD Host调用。

## 目的与前置

原设备已经通过v1独立设备认证，保持其原安装P256、原生Ed25519身份、当前customer/账号绑定和已验证的v1安全策略。原账号的v1恢复成功后，无v2 Host槽位才走本流程；有current/pending槽位继续doc92原恢复。不能把管理cookie、浏览器普通account token、记忆账号token直接当独立设备token提交。v1设备凭据已过期时先走既有设备自动恢复，不要求用户退出账号。

目标端须先用原双钥建立可信account-v2原生通道，仍保留原customer身份的可信绑定。服务端核源独立会话/当前绑定revision、源原生指纹和安装指纹、实时account-v2通道及非phone类型。源MFA策略保持权威，旧源验证已失效不能通过迁移洗成新账号认证；v2 Host MFA仍须单独满足。后台不创建任何房间/客户管理员权限。

## HTTP

服务根为当前配置的受信serverOrigin，不硬编码另一域名。均为POST、application/json、Authorization: Bearer <原v1独立设备凭据>，不带cookie或query，不提交公钥或accountId。四条路径：

- `/api/v2/account/host/bootstrap/challenge`
- `/api/v2/account/host/bootstrap/complete`
- `/api/v2/account/host/bootstrap/status`
- `/api/v2/account/host/bootstrap/abort`

challenge/status JSON严格只有 `customerId`、`installationId`、`operationId`。installationId为原6–16位仿真ID；operationId由调用方生成并持久保存，合法标识符且最多128字符。它是一次迁移事务标识；超时读取同operation状态，不能直接重启事务。

complete/abort再且仅再带 `signature`、`nativeSignature`，分别是下述同一原始签名字节的P256/原生Ed25519 Base64签名。完整字段分别映射服务器方法customer、installation、operation_id及native_signature，客户端不得自行改变协议字段名。

challenge响应：operationId、signingPayloadBase64、domain、nativeDomain、expiresAt（本接入凭据最长期限，epoch毫秒）、phase、serverTime。signingPayloadBase64按原始字节签名，不重新序列化。签名内容为现有严格 `client-login/1` 形状，复用既有原生signClientAccountChallenge接口，**不新增任意原生签名接口**：

- schema、serverId、installationId、userId、fingerprint
- customerId严格为 `host-bootstrap:<serverId>`（专用用途命名空间，不能是业务customer或account-v2范围）
- expectedBindingRevision为源设备当前绑定revision
- challengeId为服务器随机48位小写十六进制，nonce为64位小写十六进制
- issuedAt/expiresAt为签名窗口，最大60000毫秒
- nativeProof严格包含routingId、nativePublicKeySha256、connectionGeneration

客户端在签名前核实际serverId、专用customerId、源当前accountId/installationId/指纹/绑定代次、原生连接generation及完整字段/长度/时间形状。不把响应中的账号、签名字节、凭据写日志。P256 domain是 `HBBV/CLIENT-LOGIN/1\n`，原生domain是 `HBBV/CLIENT-NATIVE-BIND/1\n`，沿现有原生IPC签同一raw。用途隔离由专用命名空间、独立nonce/存储和精确服务器路由共同实现；该challenge不会进入client_login_proofs，不能当作普通设备登录证明重放。

complete成功返回phase=ready、token、sessionPurpose=host-bootstrap、installationId、expiresAt、serverTime。token只保存在迁移事务的受保护短期内存/存储中。后续仅用于本installation的既有host/verification及host/login流程；不能交给Phone、普通account认证、管理API或另一台设备。接入凭据最长300秒；pending证明首次complete必须在60秒内。已ready的同operation重试需再次验证原双签，返回原凭据和原期限，不延长。status只返回phase/operationId/expiresAt/serverTime，绝不返回token；complete未知结果可先status，再用原双签取回同一结果。abort需原双签，清除本事务凭据。

## 既有Host流程和失败恢复

拿到接入凭据后调用原host/verification/state。现有Host信任满足则继续；需要新验证时仍完成原图片/短信验证，不自动建信任、不绕过。随后原host/login/challenge → prepare → activate，保持原双签和激活签名/受保护槽位事务。HostQueue按doc92启动，可信presence进入12秒租约目录，Phone按原账号读取；无须开集群/入房才能个人协同。

每次消费接入凭据都重查源会话是否仍有效、当前账号/绑定revision、账号securityRevision、原身份及实时generation。注销、换号、撤销、密码安全状态改变、原生重连使旧事务失效，按原账号当前状态重新建立；不把这些情况误当网络失败重试旧授权。首次新安全验证不等于强制注销本机账号，失败/取消继续保留本机原会话、草稿与v1登录。

固定错误重点：HOST_BOOTSTRAP_SOURCE_VERIFICATION_REQUIRED、HOST_BOOTSTRAP_ORIGINAL_IDENTITY_REQUIRED、HOST_BOOTSTRAP_CONTEXT_CHANGED、HOST_BOOTSTRAP_PROOF_EXPIRED、HOST_BOOTSTRAP_EXPIRED_OR_UNKNOWN、HOST_BOOTSTRAP_ABORTED、HOST_BOOTSTRAP_RATE_LIMITED、HOST_BOOTSTRAP_CREDENTIAL_INVALID；以及沿用原v1/原生/Host MFA错误。按实际HTTP响应的error.code处理，不匹配本地化message。字段错误沿现有API为422；非法方法/query为400。

## 验收边界

本地合同使用真实loopback TLS、原生双钥握手及ClientDeviceSessions实际签发原v1凭据；MFA允许判断/Host SDK能力为夹具。覆盖同账号Host prepare/activate成功且原v1登录保留、单钥失败、源撤销/换绑/密码代次/原生重连/过期/abort、用途隔离、HTTP精确字段、数量上限和幂等恢复。不是最终Mac原生IPC、真实短信或75实收证明。需客户端将此流程接在旧登录恢复后，最终同签包与Phone真实会话/消息/审批/文件仍按doc96逐项验收。
