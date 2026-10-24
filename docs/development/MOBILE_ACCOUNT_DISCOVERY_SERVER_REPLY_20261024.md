# 手机版同账号设备发现：服务端核对与首次接入合同

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 已验证现场与四问答复

2026-10-24生产只读聚合（采样1792820519.0695）：account_host_session_security=0；account_collab_devices=1，类型phone/mobile_controller；activeV2Sessions=1、bindingsV2=1。未导出账号、手机号、令牌或数据库正文。证据位于本任务phone-discovery-consultation-20261024-v1/production-aggregate-diagnostic.json。采样只证明当时不存在v2桌面Host，不能据此宣称所有桌面包永久缺少实现。

1. 推荐且应复用的路线：原可信双钥身份 → 同账号Host登录激活/持久槽位恢复 → HostQueue应用启动与verified presence → v2同账号目录 → command receipt queue → 原SDK的会话、事件、结果和文件。旧仿真在线和v1设备presence不等于v2协同Host在线；不把旧表直接并入目录。当前未发现已落地的等价自动迁移入口。
2. 桌面必须完成host/login/challenge、prepare、activate的现有双签与安全校验，原生绑定有效，启动HostQueue并实际报告可信presence。服务端account_collaboration_directory.py只接纳report_verified；account_native_identity.py的current_device要求当前会话、account_host_session_security、绑定代次、原安装身份及live原生连接均成立。目录租约12秒；只读版本号784不证明这些条件满足。HostQueueAppBootstrap._readSession没有current/pending槽位时返回null，故只接bootstrap不够。
3. 诊断应分阶段且不带秘密：服务serverId是否一致；两侧账号是否由服务端认证为同一canonical account（本机可比对，不公开账号值）；Host槽位是否存在/当前绑定是否有效；队列是否启动；可信presence是否成功、租约是否有效；最后检查手机版过滤原因。普通目录目标要求非phone、canHostCollaboration、collaborationEnabled、online。fullHarnessCollaborationReady=false不是全目录过滤；fileReceiver缺失限制文件接收，不能据此隐藏全部会话目标。禁止打印认证头、槽位token、手机号、完整数据库或原生密钥。
4. doc92的App/presence/login接线仍是可复用方向，但其旧基线0ae必须按最新main逐文件重核，不覆盖共享树。根会话已核三处仍匹配APP-BOOTSTRAP-INPUT的base字节。保留main已有consumeFile、commands-list、close等行为；18项组件合同不等于最终签名Mac包接入证明。现有交互登录可使用瞬态purpose=account认证调用bindHostFromAccountLogin；remembered/device/management认证不能冒充该认证。旧restore只有显示元数据时，首次Host接入缺少合法引导，是服务端和桌面需要共同补齐的合同。

## 旧账号首次Host接入：拟新增合同，尚未实现

目标是不退出旧账号、不销毁原会话、不依赖终端命令；不是把低用途凭据直接升级成普通账号凭据。以下均是设计，不是当前可调用的HTTP接口，前端不能先猜URL上线。

服务器应提供独立、短期、仅用于本安装Host接入的bootstrap证明事务。输入为当前有效v1独立设备认证、服务端原绑定与新鲜原安装双钥签名；账号取服务器当前绑定，不采信客户端提交的accountId/customer角色。校验原服务身份、绑定revision、原公钥与原生公钥指纹、实时连接generation、账号securityRevision及账号未注销/换绑。记忆账号凭据或管理cookie本身不够，Phone身份不得走此路径。

challenge必须绑定独立operationId、一次性nonce、服务器、原安装、源绑定代次、短期deadline与专用签名domain。complete验证原安装密钥和可信原生密钥两份证明后，只产生purpose=host-bootstrap的限安装/限事务凭据；不能生成通用account登录、Phone登录、管理会话、房间权限或另一台Host权限。

该凭据只可用于本安装现有Host验证与登录事务，并继续执行原MFA策略。已有完全匹配的Host安全信任才可沿原规则复用；首次新安全验证不满足时，在原App内展示必要验证，保留旧登录和本机功能，不要求退出重登。不得通过迁移接口自行创建MFA信任或改变风控判断。现有NativeAccountIdentity._actor及NativeLoginVerification._identity需要显式传递目标installation和专用用途，避免把新凭据接入Phone/account的通用account_auth。

完成activate后，沿现有受保护Host槽位持久化和恢复；以后重启/正常覆盖自动恢复同一绑定，不重复发起首次迁移。失败、取消、超时保持原v1账号与会话，status读取原operation结果，不重放未知prepare/activate。logout、换号、绑定代次或原生连接变化、账号securityRevision变化必须令未完成bootstrap失效；不能只在签发时检查一次。凭据只保留摘要或现有稳定密钥保护的密文，不记录明文。

## 实施与验收顺序

先冻结合法源会话认证/当前绑定适配器及签名Schema，再实现bootstrap事务和用途隔离负控；随后接Native Host MFA/login限定入口、HTTP精确字段合同、桌面自动恢复接线。正式路由以实现后的合同文档为准，不让前端依赖上述拟案。

必须验证：合法旧登录首次迁移；无需退出重登；没有双钥/过期/重放/另一服务/另一安装/换账号/撤销/旧绑定均拒绝；bootstrap不能进入普通account、Phone或管理API；新安全验证仍生效；同一operation幂等和未知结果恢复；失败保原v1、本机原会话/草稿；成功后真实Mac进入75目录并完成原会话中文实收、审批、附件、异常重连与资源验收。当前这些新增迁移验收均未通过，不将拟案或目录绿灯称为真实同步完成。

## 后续实施状态

上述首次接入拟案已由正式[Host Bootstrap接口合同](HOST_BOOTSTRAP_API_20261024.md)替代并部署；签名格式复用现有严格client-login/1和原domain，以专用host-bootstrap命名空间及独立事务存储隔离用途，不采用本旧拟案推测的新增任意签名domain。线上与验收以[生产记录](../acceptance/HOST_BOOTSTRAP_PRODUCTION_20261024.md)为准；仍未完成最终Mac/75真实协同闭环。
