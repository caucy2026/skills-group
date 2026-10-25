# 终态恢复、原生管道和升级等待

## 已审核的旧任务仍留在恢复队列

先核原room/task/instance、worker、fence、原session、结果正文与审核/ACK。不要重做已经审核的任务，也不要直接清journal、延长deadline或伪造新版结果封套。

旧任务详情可能在过期后返回TASK_EXPIRED；这不是设备离线或结果无效。当前支持的服务器可通过service-info的taskTerminalReceiptEnabled发现只读终态路径：

`POST /api/v1/agents/rooms/{roomId}/instances/{instanceId}/terminal-receipt`

请求仅为`{"fence":原整数,"sessionId":"原会话或null"}`，使用原设备正常认证；不要把设备token复制到其他设备或写报告。已接入并经过最终包验证的客户端自动使用该路径；技能本身不允许从管理端伪装worker。旧服务器没有能力标记时保留原恢复流程，不猜接口。

- accepted旧格式：服务端必须核原结果与审核哈希一致、原session证据、唯一result消息、原worker/controller及当前controllerEpoch、原正文UTF8哈希和真正接收人的processed ACK。客户端还须核原生同session/fence处于inactive及idle/not-resumed。正文不必是新版JSON封套，不能手工重建正文计算哈希。
- rejected无会话预留：必须有原recoveredAfterFence失败结果、没有session证据及operation；退役原因仍是审核拒绝，不算任务成功或升级积分。不能用这条路径处理有真实副作用的接受结果。
- 两类都必须保留原注册serverId、当前连接/配置代次与原记录身份，先成功持久化有界审计，再移出恢复队列。写盘失败、未审核、缺ACK、native活跃或未知均保留；不重新claim、续租、result、review或score。

验收分层记录：接口/负控测试通过、生产实际加载新源码、客户端同身份覆盖后自动退役、重启后原退役时间/哈希保持。后端部署成功不能代替客户端实装。曾实测某台设备旧主进程退出、新主进程启动后原退役记录保持，但旧helper仍活；只能称主进程重建持久化，不能称完整进程树冷启动。

## Windows Native8原始产物与实际管道

完整源输入、依赖锁、实际Rust depfile中的生产配置、CMake生成器和真实Release依赖库均须可追溯。raw EXE、来源JSON、签后EXE和最终安装包分开记录；新helper不能直接覆盖他人正在构建的冻结输入。跨平台只同步规范源，不复制Mac生成的ABI文件到Windows。

实际新helper可用`--vibekits-harness-readonly-stdio`进行有界私有父管道验证：每行JSON含id、op（仅status或connections）及timeoutMs（5000–8000），同worker多次请求，关闭stdin后确认退出。负控验证修改op被拒、超时范围被拒、残缺EOF不执行；不要把支持此协议当作宿主已注册或仿真可用。实际输出可能外层传输ok、内层callable=false/offline，必须逐层解释。

新helper对旧宿主返回control_response_invalid时，先核实际IPC协议/宿主代次和安装组合；不改身份、开关、信任或凭据来凑成功。整包签名、覆盖安装后仍须原ID真实MCP及入房心跳。

## 守护终态缺失

控制端超时、PID缺失、计划任务Ready及合格EXE是不同证据。计划任务LastTaskResult=267014（0x41306）且守护terminal缺失时，不能称守护正常结束；核原PID/创建时间、精确任务动作、原driver/build日志和产物完整SHA，不重启未知事务。应用内守护deadline与计划任务硬期限相同存在收尾竞争风险；这只是风险解释，须用原事件证据确定具体原因，不能无证据认定所有终止均由超时导致。

已确认构建结束、最新产物已验证留存后，可以按既有授权移除自己创建的闲置手动计划任务：核精确名称、Ready、原动作/工作目录、无触发器及产物SHA，删除后回读不存在；不停止他人进程或删源码/工具链。PowerShell的`@($null).Count`会误把空触发器当一项，应计非null项；CIM创建时间不能替代GetProcessTimes精确FILETIME代次。

## 共享Mac显示busy但有更新ready记录

公开状态可只取sessionRef/taskId/phase及时间，不必读消息、工具参数或SDK日志。旧toolRunning与更新ready并存，或命令代理返回HARNESS_SESSION_NOT_ACTIVE，都不足以证明所有UI执行已结束。按真实SDK owner、活动请求和进程代次进一步对账；不按记录年龄强清busy，也不以最新一行ready覆盖所有工作。核明空闲后再沿原同身份覆盖流程安装已签最终候选。

浏览器工具被设置明确禁用时保留浏览器验收缺项，不用nativeChrome或另一自动化入口绕过。短资源采样结束要明确结束；单点内存或几十秒BOUND稳定不能替代五分钟严格idle、长期稳定性或全机健康。

## macOS更新调度后不要提前断开原连接

`update_apply`返回`scheduled=true`只代表已启动更新器，不代表目录已替换。复制后、首次信号之前，更新器仍要通过原请求的TCP来源和授权revision复核；控制端会保留原socket作有界观察。此时主动`disconnect`、重启控制端或重建隧道，可使提交检查失败。慢盘设备尤其不能套用其他机器的复制耗时。

保留原连接，读取同一`transaction-public.json`和原更新器PID/创建时间。只有明确`COMMITTED/PASS`后，才主动断开重连并检查原ID、签名、实际新PID、数据、权限、工具和房间。复制中或观察超时均不重放`update_apply`。

若终态为`COPYING/AUTHORIZATION_OR_POLICY_REJECTED`，先读取`update_status`的非敏感字段、原事务及进程，确认是否尚未替换旧App。保留失败证据。只有证实本次控制连接提前结束、原更新器已退出、旧App与授权仍有效，才通过正常重连和同一更新接口重新核权；不能直接运行SSH更新脚本、修改guard、白名单或授权revision。真实撤销、目标拒绝、身份变化或平台拒绝继续保持阻断。

实证：同一签名候选在macOS12设备第一次在复制期断开原连接，随后来源复核失败且未替换旧App；时序及来源校验代码支持提前断连的解释，但未取得原生拒绝原因的直接日志；保留失败终态并恢复正常来源后，同一工具正常核权，保持原连接直到第二次事务`COMMITTED/PASS`。这证明等待提交的必要性，不代表所有同名错误都可自动重试。令牌、完整update_status和私有路径不进公开文档。

### Intel/macOS12 候选已替换但仿真门禁未就绪

若控制端`update_apply`观察超时且目标短暂出现新包，先沿原更新器PID/创建时间读取同一`transaction-public.json`及`transaction-health-*-public.json`，不要按磁盘一瞬间的版本或前一条`applying=true`判成功。2026-10-25原Mac132的723→最终签名798只提交一次：新PID53983实际启动，但30秒原生仿真gate未ready，更新器`ROLLBACK/FAILED/RESTORED`，旧723新PID54977独立健康PASS。旧ID、公钥、签名、MCP及房间均恢复；原90份用户状态85份不变、2份运行时端点重建、3份consent-renew轮换。详情见[首败与回滚验收](../../docs/acceptance/MAC132_798_SIMULATOR_GATE_ROLLBACK_20261025.md)。

当目标新helper日志有`Cluster registration refused: SERVER_ERROR`及另一relay进程`Address already in use`时，把服务器拒绝和IPC竞争分别定位；不能凭DSH/Web已ready或延长健康窗口、关闭native门禁、混装旧helper、重复apply来宣称兼容。保留失败候选和原App回退，待新源修复、负控及同一macOS12真机覆盖重验。控制端封装含一次性token的工具调用时，捕获`TimeoutExpired`并仅记录异常类型与原事务索引，避免默认异常文本把完整命令/令牌写入日志或聊天。


## 终态只读工具与短票据审计

目标实际catalog包含 `vibekits.cluster.tasks.terminal_receipt` 时，可按Schema用roomId、instanceId、原整数fence和原sessionId读取本人历史回执。此工具只投影有限元数据，journalModifiedByThisCall=false、executionAuthorized=false；不能将调用成功称为本地记录退休。源码存在不等于旧客户端已安装该工具。原生停止需独立从目标的 `vibekits.cluster.tasks.session_status` 取得同session/fence、active=false和agentStatus=idle/not-resumed；缺字段不能靠进程列表或服务端executionStopped代替。

当前作用域没有pending记录，不能证明原serverOrigin/customerId作用域已退休。通过合格客户端正常读取原作用域、核服务与身份并成功持久化退休审计，再重启读回；不能切客户后只看空列表、导出Keychain秘密或手工删除旧记录。

每次真实房间调用完成后，及时只读取回该delegation的controller/target、created、claimed、completed、expires，核领取和完成均在有效期内。当前v1短授权票据只保留过期后5分钟，随后发票时会有界清理；延后审计查不到旧行不能判未执行，也不能编造完整回执，应保留缺项及已取得的目标调用结果。不要为保留证据放宽票据期限或重放副作用。原生状态回包只留所需字段；不把finalAssistantText、工具正文、凭据或完整上下文写普通日志。


## 旧客户命名空间的本机任务日志

不能把当前kemi列表为空当成旧newlink日志已退休。仅当合格客户端真实catalog包含 `vibekits.cluster.tasks.historical_terminal` 时，用原customerId/roomId/instanceId/fence/sessionId先mode=inspect，再对同一目标retire并读回；缺记录不制造退休。该入口保守标记writesData，服从已有具体授权，遇平台拒绝不改用SSH读写Keychain。

入口校验原存serverId、当前空闲与预算、后台原实例/设备收据及新鲜原SDK停止状态，只归档匹配旧fence并保留审计和其他记录，不改变当前customer或聊天。原服务不支持、来源不符、当前工作非空或结果未知时保持原数据，先对账原事务，不重发结果、评分、模型或升级。

代码及53项合同不是已部署证明；需要最终客户端真实旧命名空间和重启读回。依据 `docs/acceptance/G03_HISTORICAL_CUSTOMER_JOURNAL_20261024.md`，当次155仅已证明服务端原终态及本机native不活跃，真实旧journal退休仍待验。
