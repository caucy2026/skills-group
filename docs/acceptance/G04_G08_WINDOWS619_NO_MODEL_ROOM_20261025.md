# 原七台 Windows619 无模型房间委派真实调用（2026-10-25）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

控制端1554650784与原七台Windows目标6192992780在`kemi 通用测试房`（`c0985cc4dfeedaf71515ae029fc4cc4f`）均为approved、实时心跳新鲜；目标服务端profile为Windows/VibeKits`1.9.0-dev.732`，健康声明`modelReady=false`而工具容量1槽。当前注册Schema限定一个目标、房间、唯一工具和幂等requestId；本轮仅申请一次`g08-win619-29dddf92cd6f44a6af4b189d20b44a84`，工具为无副作用`vibekits.system.info`。

`room_connect`返回`authorizationMode=room-delegation`、`tunnelPrepared=true`、`connected=false`，随即消费原票据`room_call`，外层ok、isError=false、内层ok，目标实际回报platform`windows`、进程PID7876。自有通道`room_disconnect.closed=true`。后台模式只读核同一委派ID`faa3434f353c2c8d1d3fe2ce25664481`的room/controller/target精确为当前房间/155/619，消费及完成均为true、目标一致；这不是仅准备隧道或缓存绿灯。

这与[同日ARM64 Linux571证据](G04_G08_LINUX_ARM64_NO_MODEL_ROOM_20261025.md)一起，证明在当前业务房和两个不同平台上，即使目标当前没有模型就绪，获授权控制端仍可使用房间短票据执行已开放的确定性只读工具，而不新建永久白名单或SSH入口。619是原七台成员，这次没有覆盖升级，旧732兼容仅覆盖此一工具和当前授权关系。CPU编译、签名、真实模型、多个工具、降级/退房撤销和原七台统一最新签名包仍未通过；不能把两次`system.info`当作G04/G08完整通过。

私有证据位于`/Volumes/ORICO/kemi-build-cache/app-release-gate/hbbv/hbbv-main-deploy-20261024-v1/g08-windows619-room-20261025-v1/`，含原request intent、连接/调用/关闭回执与服务端领取完成只读投影；公开记录不含票据正文、密钥、文件或聊天内容。
