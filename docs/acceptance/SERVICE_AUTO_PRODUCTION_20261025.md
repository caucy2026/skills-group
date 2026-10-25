# 通用服务自动分房生产开启与实机回执（2026-10-25）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2
时区：Asia/Shanghai。服务端原P2代码不变，只在原受保护 systemd 启动参数增加 `--enable-auto-service`；无新端口、无云端数据库备份，不授予设备管理员或任务执行权。

## 上线前门禁

- 生产公网`/api/v1/service-info`原值`automaticServiceAssignmentEnabled=false`；原serverId `da3553a32048bfe691d99ad1a27a914b`，PID2569757，运行目录`/opt/vibekits-group/releases/20261025-host-software-v1`。业务租约、未完成有效房间票据、有效queued/claimed/uncertain账号操作均0。newlink通用服务1原房ID`f450c684b868292f67c534b793e26314`、原approved16，设备17、自动assignment0。
- 生产`service_auto_assignment.py`SHA256 `ec7c07e340ba92235ce32c759e1586c79f80c169b0ab88b9700c12ae5e0401c3`与本地及已验证候选逐字节相同；最新priv/main与冻结候选在运行代码无新差异。此前冻结源993项单元进程通过，其中自动服务17项均ok，覆盖原生双证明真实TLS、跨SQLite连接第10000/10001入槽、8槽满拒绝、旧身份/令牌/epoch保留、离房不自动重入和恶意伪造拒绝。本次本地补跑入口在缺`jsonschema`时于导入前终止，**不把该次算成测试通过**，复用同字节已通过的原证据。
- 按`kemi-storage-cleanup`精确清理两个10月20日已结束的集群候选`source/build`，删除1282文件、822生成目录、已分配1561616384字节；ORICO可用6541508608→8027303936字节，源码/锁文件/证据不变。再建立生产本地一致性快照：175665152字节/SHA256 `632a21cc12ea53f97d45d341f0daa65f2c72f9717fa68a552e564d037c2c3d2f`，134表/278537行；验证后本地仅最近3份有效备份。云端快照worker终态后清自有/run 4文件，无云端数据库备份。
- VibeKits及hbbv真实会话最新main predeploy检查均ELIGIBLE；Phone负责人确认无消息/审批/文件写在途，原R2终态且R3未发。原源代码和正式运行包未替换。

## 一次受控切换与独立读回

2026-10-25 14:03:45执行前只读检查，14:03:57服务端worker状态`verified`。同一运行目录的hbbv PID2569757→2689633；serverId、正式源、hbbc/hbbs/hbbr PID138192/1270335/1270472不变。公开可信HTTPS独立读取`automaticServiceAssignmentEnabled=true`、`serviceRoomMemberLimit=10000`；账号协同、Phone可信恢复、Native路由、原SDK流、文件接收和Host软件声明仍为true，`fullHarnessCollaborationReady`仍为false。原设备17、房成员16、自动assignment0在切换点未被迁移/覆盖。云端配置worker终态成功、自有stage5文件清理后回读不存在，hbbv项目分配2725466112字节，低于3GB。

随后4台**真实既有设备**经原生身份完成`resolve`：1554650784、4240650696、4456560334、5713793648，均为业务客户`kemi`、服务关系归属`newlink`通用服务1、房成员approved、服务关系active、分配revision1、设备level0。各自旧设备token/epoch/owner的组合哈希与启用前本地一致性备份逐台一致，未提升设备等级、未改业务客户、未产生新的任务执行许可。此回执证明服务端协议已接到真实客户端，不代表全新安装首次激活也已实测。Mac155真实本机工具读到该服务房16台；普通Mac132原ID和G73 SSH指纹核对后实际`cluster.rooms`显示同房memberCount16、visibleMemberCount2，与两名有效管理员数相同。132旧包不公开新版`room_devices`工具，不能把可见计数当成逐ID列表验收；本次只释放自建连接。

## 保留缺项

- 全新安装首次自动入服务、重新安装丢失本地房间后按原生身份找回、用户一键退出与主动恢复，仍需真实设备走完；合成合同通过不替代。
- 第10000/10001台和八槽满拒绝只有隔离数据库合同，未有1万台真实同时在线，也未达到G09长期稳定。
- 普通成员只能看到管理员的逐ID列表和互访拒绝仍需新版普通客户端或受权真实HTTP回执；Mac132旧客户端只证明汇总可见数。
- 原七台中529心跳失联、617按用户确认关机/断网；自动分房开启不等于七台升级和房间任务G01–G10完成。

本地私有回执：`/Volumes/ORICO/kemi-build-cache/app-release-gate/hbbv/hbbv-main-deploy-20261024-v1/`下`backup-space-service-auto-20261025-v1/`、`snapshot-service-auto-20261025-v1/`、`service-auto-enable-20261025-v1/`；公开文档只保留脱敏事实，不含设备令牌、私钥、聊天正文或账号口令。

## 公共说明与技能同步

2026-10-25 14:18:48，公开分发网页已静态切到`20261025-service-auto-guidance-v1`，后台PID与serverId不变；入口及r1预检类型错误、r2成功、全资源SHA和云端清理见[网站上线回执](PORTAL_SERVICE_AUTO_GUIDANCE_PRODUCTION_20261025.md)。`skills-group/main b42dd69ea3346f15286805200694e03a52b08ec2`及本机全局技能同步当前kemi业务客户/newlink服务父系、实际自动服务状态与未验边界。线上能力和网页都已更新；七台最终版本与全新安装首次服务入房仍是独立缺项。
