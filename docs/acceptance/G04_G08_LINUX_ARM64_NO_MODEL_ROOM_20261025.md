# 无模型 ARM64 Linux 房间委派真实调用（2026-10-25）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 实际动作与结果

控制端原仿真ID`1554650784`和目标原仿真ID`5713793648`在`kemi 通用测试房`（roomId`c0985cc4dfeedaf71515ae029fc4cc4f`）均为approved且心跳新鲜，未利用newlink隔离售后房或永久旧白名单。目标服务端profile为Linux/`linux_arm64`、VibeKits`1.9.0-dev.755`；本轮健康声明`modelReady=false`、工具容量1槽。控制端当前工具目录确认`vibekits.simulator.room_connect`、`room_call`及`room_disconnect`的实参Schema。

仅产生一次持久请求ID：`g08-arm64-268e3d317c6e45939ad3ab332b6683e2`，指定目标571、当前业务房和唯一只读工具`vibekits.system.info`。`room_connect`返回`authorizationMode=room-delegation`、`tunnelPrepared=true`、`connected=false`；按原协议直接继续同一票据`room_call`，外层ok、isError=false、内层ok，实际返回目标platform`linux`、hostname`mp730-156`、内核`Linux 5.10.43_wudangstick`和目标进程PID839849。随后只关闭本轮通道，`room_disconnect.closed=true`。没有调用普通仿真连接、SSH、模型、编译、签名或会改变文件的工具。

服务端只读SQLite按同一委派ID`a0a787f61e33db6ee54c9ebcfff560bf`独立确认room/controller/target正确，消费记录`claimed=true`、完成记录`completed=true`且均指571；不是仅客户端准备灯。这次显示当前Linux ARM64目标已跨过2026-10-23旧`ROOM_SIMULATION_NATIVE_POLICY_INACTIVE`失败，但旧首败和其他Linux/房间不能因此自动改判。

## 验收边界

G04只通过“无模型就绪仍能通过已授权房间实际提供确定性`system.info`”这一子项；CPU编译、签名、真实模型生成及多个设备的资源任务仍未完成。G08只通过当前控制端→571、当前房间、唯一只读MCP工具与服务端领取/完成的一次正向调用；成员降级/退房撤销、旧手工授权兼容、Windows和所有工具范围仍未完成。房间短票据准备时`connected=false`是此协议的正常中间态，不能等它变永久连接或把其当失败；必须核同票据实际调用和断开。目标仍是七台范围，571为额外Linux设备，不替代原七台中529失联或617离线。

私有证据位于`/Volumes/ORICO/kemi-build-cache/app-release-gate/hbbv/hbbv-main-deploy-20261024-v1/g08-linux-arm64-room-20261025-v1/`，含精确intent、连接/调用/关闭回执与服务端领取完成只读投影。公开文档不含票据正文、密钥或用户文件。
