# 同账号“我的设备”：目录生命周期与研发接续

本文件前半保留v1客户端的customer作用域兼容路线；不要将其当作v2 Phone/Native Host个人目录的客户过滤规则。v2边界见末节及实时部署/客户端验收记录。

当前状态见项目最新验收台账。目录源码与隔离HTTP联调通过，不等于客户端已发布；App级presence源码已接入并完成隔离联调；生产可信身份适配、旧会话原生证明迁移、原生执行票据及完整远端原Harness呈现仍须分别验证。不能用简化远程面板替代用户要求的一键完整切换。

## 身份、凭据和订阅

- 目录绑定键包括origin、serverId、customerId、原installationId、userId、bindingRevision。相同userId在其他客户／服务器仍是不同上下文。后台“最后成功登录”以原子绑定版本为准，历史登记不授权。
- 正式宿主使用HarnessAccountDirectoryRuntime监听已验证账号与原配置事件。一次绑定一个自有HTTP/SSE；重复状态通知不重建，退出／配置失配／认证未知立即释放旧视图，关闭旧连接不阻塞新绑定启动。视图使用精确owner代次，不能只按accountId关闭／处理迟到错误。
- 从原OS凭据槽读取时核期望账号与bindingRevision，异步等待后再次核完整scope；token仅缓存本绑定网络生命期，不能在每次SSE续租时反复拉起凭据读取器。凭据不写URL、页面、日志或跨域缓存。
- 401/403或OS凭据未知停止旧订阅并标记待核验，保留凭据以便恢复；不自动注销后来账号、不拿新账号token重试旧请求、不反复弹系统凭据确认。
- 12秒在线租约需要新快照续期；同游标snapshot_required必须处理，不能当重复事件忽略。昵称变化保持选中，绑定／route／native pin变化应清除旧呈现。目录的设备ID和pin仅供发现；真实目标握手与短票据仍须验证，不能把列表当执行许可。

## 验证与源码协作

使用现有原生项目测试框架。至少覆盖：登录/退出/恢复、相同userId跨客户、旧读未完成时切scope、旧close/错误、版本变化、OS凭据等待时切账号、401停止、昵称事件与退出移除。真实HTTP/SSE服务端要实际flush流式输出；Dart夹具须关闭输出缓冲，不能通过延长超时或放宽客户端帧校验掩盖未送达数据。

用受控旧逻辑负控证明回归能发现缺陷。测试副本换回仅accountId归属时必须失败；不修改用户共享源码做负控。hbbv测试fixture仅在显式测试环境启用，临时生成测试密钥，结束时会话归零、HTTP/SSE线程先退出再关临时DB；不得把fixture身份解析器部署到生产。

合并到主线时保留并行内容，仅应用本任务增量。共享区宿主与桥接类可能不属于同一次主线：不要删主线新增调用来迎合旧桥接，也不要整文件覆盖。冻结同一Git提交的lib及pubspec声明的path依赖，再用离线、强制lockfile生成package_graph等元数据。区分依赖声明分类差异与实际包版本/内容变化；保留原锁，不能伪造缓存有效标记或忽略真实版本变化。用合并后闭包再验证，源码/共享索引/正式包和运行服务均保护。

实证：[目录正式宿主与跨域回归](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/CLIENT_ACCOUNT_DIRECTORY_RUNTIME_20261021.md)。其中25项Flutter包括隔离Dart→真实hbbv Handler登录/签名presence/目录SSE，不是两台物理设备、最终signed GUI原生IPC、七台覆盖或AC01–34通过。最终应用仍需完整真实验收后发布。


## 应用级在线心跳与会话继承

App拥有唯一HarnessAccountPresenceRuntime，不能把心跳挂到设备面板/房间列表的显示生命周期。一次完成后4秒再发，最多一个在途心跳，失败复用既有4～60秒抖动退避，Retry-After最低期限对重连、恢复前台和同绑定换TLS配置都有效。无账号不建心跳timer，退出后不自动把该scope重新登录；启动仅核已有OS凭据，临时网络失败退避恢复，不保存管理密码。PAD须先完成原仓库恢复Gate再读取原key。

原生短断/新generation/proof过期/旧sequence与会话撤销分开：前者重取可信当前状态、退避恢复，不强迫密码登录；真正会话过期或撤销停止。旧有效会话缺少新原生证明时保留登录和原功能、暂停新协同能力，不造证明、不生成替换ID或key。在线仍由服务端当前绑定、会话期限、签名及真实原生连接和12秒租约决定，不因客户端自报enabled/online放行。目录本机presence说明可缺失；presence-state/report仍严格拒绝缺原生上下文。

共用传输信任指纹需覆盖URL/客户/可信host/证书/服务公钥/转发方式，房间enabled开关不改变账号信任。信任更新关闭旧HTTP；旧异步结果按scope、epoch、传输与账号代次拒绝。模型的UI错误边界可能吞原异常，重连层必须保留原错误/Retry-After，不能只抛泛化“不可用”后过早重试。错误仅留有界白名单code，不把响应message或令牌写日志。

登录入口读取统一账号状态，不能只缓存本按钮的旧用户名。旧菜单退出前重新核绑定，实际logout还须核菜单显示UID/revision与原OS凭据快照，避免另一入口/进程已切到B却注销或删B。账号变更后用原restore核验，不索取另一遍管理密码。

新实证：[应用级presence与登录状态](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/CLIENT_ACCOUNT_PRESENCE_RUNTIME_20261021.md)：46 Flutter、72后端；隔离服务无房间续租→原生断连→租约移除→原pin新generation恢复，无须再登录。包括100 emoji昵称按code point而非UTF16限长。不是物理机、最终包或生产已启用的证明；完整远端呈现与最终设备矩阵仍须验收。


## v2 Phone与Native Host：独立于房间的账号范围

v2个人目录按serverId、服务器认证的canonical account、installationId和当前bindingRevision隔离，不按customer筛选同账号设备；不能混入另一服务器或账号。Phone只发起同账号协同，不作为Host、没有集群/房间。原v1来源customer仍用于验证旧设备凭据、原pin和安全策略，不可省略或伪造，但它不是v2个人目录过滤条件。

Phone把当前P256账号安装身份与Root签发的数字Native路由双钥关联、获取原`client-access/1`短票并走peer/1业务时，按[手机原生票据与点对点协同](phone-native-peer-control.md)执行；后台能力开启与真实手机业务通过分开记录。

服务端hostLegacyBootstrap能力出现只说明接口存在，不说明桌面已有Host槽位、实时原生通道或可信presence。旧登录无Host槽位时按[正式Host Bootstrap合同](https://github.com/caucy2026/skills-group/blob/main/docs/development/HOST_BOOTSTRAP_API_20261024.md)以原v1独立设备凭据及原双钥接入；保源绑定/原v1通道，继续原Host MFA，成功后再启动HostQueue/presence。普通account、remembered、device与management令牌用途分开，不能互换；失败不清旧登录、会话或草稿。

目录为空先按原生生产者→Host槽位→队列→可信presence/12秒租约→客户端过滤逐层核对，不移除Phone安全过滤或把原仿真在线投影成v2在线。新版App版本、后端ready、旧原生签名IPC都不证明包内有v2通道/host descriptor；冻结实际relay的原生Git ref、完整输入和签前/签后SHA，复用受限正文验证解释正常签名差异。实际包的旧来源与新开发的最新main分别记录，不能把兼容对照ref当降级指令；增量须保留PEM链、原v1、原签名IPC及权限，走独立完整构建和最终GUI门禁。


## 同设备有效 MFA 继承到 Host（2026-10-24）

服务器已支持 `features.hostExistingDeviceTrustInheritance`；以实时 capabilities 为准。旧v1已可信设备应通过正常bootstrap双证明迁移，已有ready事务也可在认证/state查询时幂等派生。派生不是独立MFA或执行许可：账号、installation、安装/原生双指纹、源session/binding、原信任和安全revision必须持续有效，期限不延长；失效按原安全验证处理。不能只凭相同账号文本、设备ID或客户端metadata放行。

`host-bootstrap-v1.`加64hex是专用票据，不改成普通账号/Phone token；只能给规定Host认证/验证路径。服务上线、bootstrap ready或信任状态为true均不等于Host已激活、更不等于原SDK业务通过。需要最终客户端实际Host目录、中文消息、工具/审批、附件和注销隔离证据。不要手工修改信任表或更改旧SDK DataOwner来修客户端接线。

操作依据：`docs/development/HOST_EXISTING_TRUST_INHERITANCE_20261024.md`。当次运行代码priv/main452eeb5，原serverId及密钥保持；本次135个不同Linux合同覆盖、生产能力和清理已核验，真实788/Phone业务仍待客户端验收。此版本号仅是当次证据，不代替下次现场核对。

## 关联设备的目标目录选择：安全范围与真机负例

2026-10-30原Mac445覆盖823后，APP“关联设备”已能进入第二台、载入目标工作区/历史，退出与重入保持本机位置及目标未发送草稿；但协同模式“添加工作区”真实报`directoryPicker/list: ACCOUNT_UI_REQUEST_FAILED`，823不能因此宣称完整协同通过。当前源码`harness_account_original_sdk_gateway.dart`将`directoryPicker/list/pick/createDirectory`列为本地GUI操作，远端Native peer的`_proveLocal==null`会被`ACCOUNT_LOCAL_GUI_REQUIRED`拒绝，`harness_account_ui_host.dart`随后可把根错误折为通用`ACCOUNT_UI_REQUEST_FAILED`。这与现场现象吻合，仍须由目标有限诊断核真正异常阶段；不要从泛化UI码单独断言根因。

现有`test/support/account_original_sdk_gateway_checks.dart`明确要求远端原生peer的上述目录操作和`workspace/create`被拒且原SDK不执行；正向`harness_account_workspace_picker_actual_sdk_test.dart`只覆盖可信本机GUI。修复不能删除这个旧拒绝负控、把任意路径交给远端，或把同账号目录发现当文件系统许可。应另设经当前同账号绑定、原生身份和目标设备会话代次核验的**有界目标目录读取/选择**，在目标侧应用禁止访问目录及其子树、路径规范化/符号链接防逃逸、最小字段与分页/容量、授权撤销及连接代次校验；创建工作区需独立确认目标路径和归属。新增安全正控与跨账号、旧票、禁入目录、越界路径、撤权负控之后，再用正式签名包同一“添加工作区”入口真实复验，不用本机picker通过冒充远端通过。现场边界见[445协同失败台账](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_MAC445_HEARTBEAT_LAPSE_WITH_DUAL_ONLINE_ROUTES_20261030.md)。
