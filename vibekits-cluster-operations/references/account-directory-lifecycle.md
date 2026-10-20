# 同账号“我的设备”：目录生命周期与研发接续

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
