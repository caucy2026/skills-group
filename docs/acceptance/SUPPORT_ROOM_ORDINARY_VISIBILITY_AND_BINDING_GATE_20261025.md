# newlink通用服务房普通成员可见性与账号前置门禁（2026-10-25）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

目标房`f450c684b868292f67c534b793e26314`是售后隔离房。本轮两个原Windows设备4240650696/build2789与6192992780/build2732均已获批，客户端实时目录均标`supportRoom=true`、`simulationAccess=administrators_only`，两者都不在该房`administratorSimulationIds`中。生产只读聚合为该房16台approved、近30秒9台新鲜；目录列表的权限投影与完整成员数不可混为一谈。

从普通成员424真实调用`vibekits.cluster.room_devices`，结果仅1台、role=administrator、原ID1554650784且online；普通成员619、132、529等均不在响应中。旧723的132实际catalog尚无`room_devices`工具，因此未把132列入该接口真机通过。此项证明**本次424普通视角的列表隔离**，不能外推所有版本/设备或管理员完整可见性。

又从424以唯一requestId、售后房ID、目标普通成员619及只读工具`vibekits.system.info`发起一次正式`vibekits.simulator.room_connect`负向调用。外层仿真工具交通成功，但目标424的脱敏Harness诊断记录该调用`status=failed`、原因`CUSTOMER_SIMULATION_ACCOUNT_BINDING_REQUIRED`、耗时3450毫秒；生产只读查询同房、controller424、target619的近5分钟`room_simulation_delegations`新增数为0。没有生成票据、连接或访问目标的结果，也没有重放同requestId。

**限制**：此次拒绝发生在账号绑定前置层，尚未真正抵达`administrators_only`角色分支，不能把它冒称为同房普通成员互访角色规则已真机验收。下一步须在已登录同一客户且身份有效的普通客户端上，保留账号/安装身份与原房间授权，重新用新的有界QA请求验证角色拒绝；仍须另测管理员读取所有设备和获批管理员委派。不得通过白名单、伪造账号或后台直接改数据库绕过前置门禁。本轮未变更生产成员、角色、客户或服务。
