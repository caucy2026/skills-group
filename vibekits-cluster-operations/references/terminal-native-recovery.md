# 终态恢复、原生管道和升级等待

## 已审核的旧任务仍留在恢复队列

先核原room/task/instance、worker、fence、原session、结果正文与审核/ACK。不要重做已经审核的任务，也不要直接清journal、延长deadline或伪造新版结果封套。

旧任务详情可能在过期后返回TASK_EXPIRED；这不是设备离线或结果无效。当前支持的服务器可通过service-info的taskTerminalReceiptEnabled发现只读终态路径：

`POST /api/v1/agents/rooms/{roomId}/instances/{instanceId}/terminal-receipt`

请求仅为`{"fence":原整数,"sessionId":"原会话或null"}`，使用原设备正常认证；不要把设备token复制到其他设备或写报告。当前客户端自动使用该路径；技能本身不允许从管理端伪装worker。旧服务器没有能力标记时保留原恢复流程，不猜接口。

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
