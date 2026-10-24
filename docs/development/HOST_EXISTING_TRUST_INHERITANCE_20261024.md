# 同设备旧 MFA 信任继承到个人协同 Host（2026-10-24）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 目的与边界

同一账号、同一 installation 的有效旧设备信任，不因旧 v1 登录迁移到 v2 Host 而重复短信。只补服务端信任连续性；不改变客户端专用票据 `host-bootstrap-v1.` 加 64hex，不修改原客户/SDK 数据归属、房间权限、管理员等级或其他服务。Phone 仍不是 Host。

## 实现

`account_host_mfa_inheritance` 只保存派生来源，不新建独立 `account_host_mfa_trust`。来源是已完成安装及原生双签的 bootstrap；同时验证服务器身份、账号安全 revision、原 installation、安装/原生双指纹、当前源 session/binding/native pin、真实原生连接及未过期旧 MFA 的原摘要。历史客户信任仅在账号、installation 和两把原公钥均相同且原摘要可重构时复用，不继承租户权限。

首次完成及已有 ready 票据认证均可幂等派生，覆盖 787 已完成 bootstrap、尚未取得 Host 登录的升级现场。派生到期时间最多为原 MFA 到期时间，重复查询或服务重建不会延长。未知响应通过同一 operation/state 对账，不重发验证码。

每次有效性判定重新核原信任、源 session/binding、双指纹和安全 revision。Host SMS 模式的 `current_device` 也重新检查，继承来源失效后既有 Host 不继续作为可用设备。独立完成过 Host 短信验证的信任按原独立策略有效，不靠派生来源维持。密码、账号、key、binding 改变或信任过期/删除均不能靠客户端 metadata、相同 ID、策略布尔或旧 bootstrap 固定放行。

能力端点新增严格布尔 `features.hostExistingDeviceTrustInheritance`。它表示服务端支持，不是某台设备已继承或 Phone/SDK 全链路已通过。Host 登录仍必须走原挑战、双证明、prepare/activate；验证状态的 executionAuthorized 仍为 false。

## 本轮证据与未完成

- Mac 开发合同：新继承 20 项及原 bootstrap 18 项通过；相关 46 个有效测试单项通过，但首批错误选择了不存在的 `test_account_collaboration_api`，该批整体失败记录保留。纠正为实际 HTTP/directory/startup 模块后 51 项通过。共 135 个不同成功测试 ID；开发合同不替代最终包验收。
- 关闭继承回调后，带真实原 MFA 的 TLS 正例确实失败（1 失败、0 加载错误）；不是用缺 fixture 冒充旧行为负控。
- 新正例使用真实 TLS 双公钥通道及原 MFA 引擎，短信仅合成接收器；来源信任不是 mock True。保留旧“只有策略布尔、没有真实信任行”的 assertFalse 控制。
- 原有 ready 操作、服务重建、同钥重连、来源过期/撤销、密码变更、双 key/pin 变化、binding/source session 变化、错误账号、未知提交响应及活动 Host 失效均有覆盖。
- 生产只读：155 的原 ready bootstrap 尚有效，2 条旧 MFA 与原双指纹及当前密码摘要匹配，源 binding 匹配，原 serverId 保持。SQL 不证明瞬时原生连接，也没有创建信任或改变生产数据。

当前状态：服务端已按原身份部署，真实客户端免重复短信及完整协同待最终候选实收。本机/Phone/PeerB、原 SDK 中文消息、工具/审批/附件和注销隔离仍需唯一最终客户端实际验收，不能把以上合同当完整协同交付。

证据目录：本机 hbbv 发布根 `host-existing-trust-inheritance-v1/`，保存原失败、合同、负控及只读生产摘要。数据库备份仅本地最近 3 份有效，云端项目不超过 3GB；后续仍按既定资格、冻结、本地备份、部署身份/健康与 cloud-build-cleanup 门禁。


## 实际部署与收尾

运行代码：priv/main `452eeb5f458a730c71671486c5e56e0510316326`；实际 release `/opt/vibekits-group/releases/20261024-host-trust-inheritance-v1`，PID 2749373。591 个运行源文件、原 serverId、账号存储密钥和外部门户目标已独立读回；hbbc/hbbs/hbbr PID 保持。公开 HTTPS 新能力标志为 true，fullHarnessCollaborationReady 仍为 false。

Linux 首轮 134 个用例通过；1 个 CLI 启动用例的 3 个分支因我准备的测试归档缺 `tool/runtime_release_health.py` 而失败，原日志保留，未据失败批部署。补入同一冻结主线的 test-only 依赖后，9 个启动合同通过（其中8个重复），累计覆盖全部135个不同用例。运行归档没有改动。

部署前只落本地的一致性备份已验证129表/198544行，121434112字节；本地仍仅最近3份有效备份。云端未创建数据库备份。3个临时合同/部署目录已回读不存在，清理1416文件、18542592分配字节；运行源码再次全SHA通过。项目加所属日志2704121856字节（另有共用端口门户），低于3GB；并发环境不把全盘净增算作独占回收。

独立生产审计时 Host 独立 MFA 与派生记录均为0：这证明没有手工预置真实信任，不证明某台已完成迁移。需要788用正常双证明/状态查询触发继承并完成Host激活，再核Phone目录与消息、审批、附件；不得把能力开关或合同当完整实收。原客户端会话已收到集中交付通知。
