# 785舰队升级前置核对与手机版原生来源交接

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 真实Mac目标，不按旧路径假设安装

本轮只读通过kemi房间委派核对应用和更新状态，未安装、上传候选或改权限。

|设备|实际运行包|原进程|Bundle ID/团队|严格签名/Gatekeeper|
|---|---|---|---|---|
|1321656264|723/2723，/Users/mac/Library/Caches/Vibekits 2.app|55002|com.caucy.vibekits / 26T5WV4GLP|均通过|
|5298938227|728/2728，/Users/kemi/Library/Caches/com.caucy.vibekits/Vibekits.app|466|com.caucy.vibekits / 26T5WV4GLP|均通过|

529另有/Applications/Vibekits.app，版本723、未运行；不可把该副本当当前运行包。132无receiving/applying/uploadIntent，旧735候选仍staged并保留UPDATE_AUTHORIZATION_RECHECK_FAILED，requiresReconciliation=false；未复用旧token、未重放旧apply。529无receiving/applying/uploadIntent及候选token。旧失败原因尚未取到原生直接证据，不归因为路径、权限或网络。

两条app_signature调用票据26205ab085c0c7a5d54095c48ae3bf17和cd6ef7a0e7943b4ddf706ee08fa200c0，均已及时核服务端controller155、对应target，以及created≤claimed≤completed≤expires。候选与旧包的完整指定签名要求、entitlements等仍须在真正暂存/应用时由原升级门禁比较；本次基本签名预检不冒充完整覆盖升级通过。

首次两目标同时发room_connect，529得到ROOM_SIMULATION_BUSY。源码RoomSimulationSingleFlight在执行握手work前拒绝重叠请求，不能据此判529离线或权限拒绝。132原只读调用终态后，529改为顺序握手，两项正常完成；未切普通执行通道来规避房间限制。以后同一控制端房间握手串行，其他可独立的检查才并行。

785包的构建Mac与第二台实测仍由原个人账号会话负责，不抢占、不重做155/445安装；已向其同步132/529实际路径、旧候选失败与下一统一包需求。785尚不能凭公证Accepted单独视为整个舰队合格，原G01–G10未完成。

## 手机版所需relay：精确来源及SHA分层

手机版同事反馈当前785缺v2原生Host入口。独立读取本机现装/Applications/Vibekits.app，元数据785/2785，内嵌relay SHA91c206bb1ee4cb30f75dc8dd041a9b6e605a19244f2120849b5ff7ab7d32c6fa，与785最终签后记录完全相同；/api/v2/account/native/channel及account-collaboration-host/1两个标记均不存在。结合785的noNewRust来源，不能把新版前端/后端ready当该原生能力已在包内。

785原生输入来自caucy2026/rust-desk的nativeMain63c102dfb748a745e29755d0f02dac6baff488e1。合格签前Universal输入48051472字节，SHAe2c671d3f1f8aee650664ae1919bcab8e2338f57154740846f11c4d7f8dc7433；785签后SHA如上。已有严格签名及限定两处LINKEDIT字段的正文规范化比对确认等价，不因为正常签名变化把它误判混包；不能扩大归一化忽略范围掩盖代码差异。

原完整输入/驱动根在已登记的personal-account-native-channel-20261021-v1/native-ca-bundle-fix-v1/full-native：native-root/client、evidence/source-inputs-ca-bundle-r2.json、run_native_ca_bundle_r2.py、verify_rustdesk_frozen_inputs.py及两架构91+91合同/二进制记录。实际读取channel、login、ipc、Cargo.lock四项SHA均与1144输入清单一致；Git63c102的channel blob与冻结文件一致。输入清单mainCommit48ff267是编译基线，叠加当时已审核两文件才等于63c102，不能遗漏PEM链修复。

明确区分实际包来源与新实现基线：只读ls-remote观察到原生仓库最新main为52941b4eddbb740a66bcf7540a2aaba0daadd31d；review本地无该对象。自动惰性取对象等待已仅中止本任务读取进程，exit130；GIT_NO_LAZY_FETCH=1确认缺对象。没有声称已读最新对象源码，没有改共享HEAD/index、785或原冻结输入。正式新候选仍需按最新原生main合并，63c102只作785兼容对照，不能要求同事降回旧主线。未来远端再次前进须重新核对。

已定向回复“vibekits手机版本”成熟来源、精确文件/包SHA、Git ref、独立构建输出和最新main边界；不群发该咨询，不启动构建或改后台。Phone v2补丁的INPUT基线10e7不能直接覆盖785的dfee源码，也不能单凭此差异断言哪份最新；应按最新main三方合并并保留PEM、原v1、签名IPC、房间及工具权限。现有来源链没有已合格包含v2增量的relay，模块/TLS合同不等于完整原生/最终签名GUI通过。

并存原则：新Host Bootstrap只以仍有效的原v1独立设备会话和原安装/原生双钥引导；保留源customer的可信绑定/通道与安全策略，再开独立account-v2通道。源customer是迁移凭据作用域，不是v2个人目录的客户过滤；v2目录按serverId+canonical account隔离。Phone继续非Host发起端，没有房间或集群，不能放宽过滤伪造上线。新失败不清除旧登录、本机会话或草稿。

证据位于本任务mac-fleet-785-preflight-v1：原/r2应用与update-status、两台signature-result、signature-delegation-audit、reported-signature-tools、phone-relay785-source-handoff。未创建云端编译缓存或备份，无安装。G02仍待合格候选同身份覆盖和完整升级验收，手机版仍待v2原生增量及真实会话/消息/审批/文件联调。

## 在途候选后续门禁与维护通知

个人账号会话后续通报：445的原785事务以simulator_gate_not_ready健康失败，已自动回退784且回退HEALTH_PASS。此为同事原事务通报，root未重放或独立占用445调查；785对外舰队扩展保持BLOCK，root未对132/529暂存或应用。公证/签名通过不能替代此失败，待原负责人定位并按资格及验收门禁修复后继续。其原证据在个人账号785任务目录，不能把旧包回退健康冒称新785通过。

Linux同事已通知同源main c5edc0fe加Linux补丁的755/2755两机clean构建，报告原生worker88=2483071、101=749323，之后320 GUI阶段计划正常退出748并finally恢复。root保存该维护通知，没有独立核其worker进程，也不连接、跑分或抢占两机；此前120秒基线已结束，不在本维护窗宣布全在线PASS或把计划断档认作产品故障。原755事务终态和原ID恢复后再安排严格稳定验收，不重启未知作业。
