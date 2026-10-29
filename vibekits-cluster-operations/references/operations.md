# 恢复、监控、升级与清理

## 断联恢复

先核控制端桥/本机 App 是否刚重启，再查原事务 PID+创建时间+日志/回执。仿真断联必须使用已登记且获授权的同机远程桌面排查进程、原仿真开关/权限/焦点；黑屏、输入失败、认证拒绝与整机离线分开。普通同范围允许/UAC确认可自行完成，密码/PIN本人输入，工具拒绝不得换渠道绕过。用户确认关机/断网且不要求恢复的设备不盲连/WOL。恢复后原 ID 实际工具调用+新鲜房间心跳，不能只看窗口。

同一设备的VibeKits仿真ID、hbbv心跳和KEMI远程办公备用ID要分别读实时状态。房间中签名上报的`remoteControl.deviceId`只提供备用入口，在线查询为true也尚未独立证明它与原仿真ID是同一物理机；取得不打断共享前台的窗口后正常连接，先核目标主机/安装身份，再查旧App进程与原事务，最后用原仿真ID真实工具和心跳验恢复。2026-10-26 newlink售后Windows784仿真/心跳离线但其登记Office146390118在线，是**待核双通道现场**，不能把额外设备波动冒充原七台故障，见[只读时间线](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_EXTRA_POOL_SPLIT_PRESENCE_20261026.md)。

KEMI远程办公的WebView输入框不能仅凭AX`setValue`后的可见文字判目标已更新：实测它没有触发输入事件，连接仍指向旧最近设备。用真实键入后核格式化ID，再在连接窗口标题核**精确目标ID**；标题不符立即关闭本轮自建连接，不操作远端。目标弹空密码框时不猜或提交；无已授权保存入口就请持有人直接在窗口输入。观察本机主窗时避免把一次性密码带入截图或工具输出；如已意外暴露，停止使用旧值并请用户本人刷新，凭据变更由人完成，不写入报告。见[当次首败与阻塞](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_EXTRA_POOL_SPLIT_PRESENCE_20261026.md)。

macOS SSH 可连接但不能访问受保护文件时，在获授权设备打开：**系统设置 → 通用 → 共享 → 远程登录旁的 ⓘ → 允许远程用户对磁盘进行完全访问**（文字随系统版本略有不同）。管理员认证由本人正常输入；这是远程登录访问权限，与屏幕录制/辅助功能/App自身文件权限分别验证。不用 chmod -R、删 TCC 或重置钥匙串替代，开启后在原 SSH 会话实际读取获授权目标文件。升级保持 Bundle ID、团队、完整 designated requirement、entitlements/辅助程序身份和 Keychain 标识。

## 监控

万人房间容量要分开验证：当前hbbv本机合成合同已证明管理摘要按100台分页，以及售后房满10000离线成员后下一台进入服务房2；这是数据库/分页/分房逻辑回归，不证明100台真实同时在线、断线重连或24/72小时资源稳定。复现时从项目`server/requirements.txt`在独立临时环境运行对应两项unittest，失败先核依赖而不改生产；完成后清理本任务venv/依赖缓存，按卷实测净释放。见[万人房间离线合同](https://github.com/caucy2026/skills-group/blob/main/docs/acceptance/G09_LOCAL_TEN_THOUSAND_ROOM_CONTRACT_20261025.md)。

在线容量另查每轮是否在规定心跳周期内完成、失败请求数及尾端真实新鲜数；只看HTTP 200和最终在线数会漏报超期。2026-10-26隔离10,000合成设备的4秒周期全轮超时，64线程保持连接仍超时；另设10秒周期短测3轮/30,000次全部接收、末尾均新鲜。这只能说明本机30秒合成节奏，在真实设备、生产云机、跨网重连和24/72小时实测前不宣称万人在线验收。原诊断脚本曾漏检周期而误报PASS，原回执和3项负控已保留；复用时使用修正后的周期判定，见[吞吐边界与判定纠错](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_SYNTHETIC_HEARTBEAT_THROUGHPUT_20261026.md)。

售后房管理员名单可能随账号绑定即时变化。真实退出账号后，普通成员445在通用服务1房看到0名管理员，而kemi业务房仍可见原8名成员；155的kemi绑定恢复后，445在售后房仅看到155这一名在线一级管理员，其他普通成员继续隐藏。必须以同一普通设备分别读`room_devices`、`cluster.rooms`，并用只读后台绑定状态核对前后，不把名单恢复等同实际委派仿真通过。见[售后房登录可见性续验](https://github.com/caucy2026/skills-group/blob/main/docs/acceptance/SUPPORT_ROOM_LOGIN_VISIBILITY_TRANSITION_20261025.md)。

每台记录采样时间、设备原 ID/电脑名、进程路径/PID/出生时间、版本、房间心跳 age、真实 MCP 成败、模型/负载/磁盘/内存及错误。房间 HB 监控、实际工具健康和 OS 工作状态分别呈现。轮询使用有界、单飞、退避；页面隐藏/编辑/提交暂停，失败显示未知，不清零或伪造在线。只有 HB 的24小时记录不能称 OS/MCP 全稳定；5分钟空闲CPU验收包含 App/WebKit/helpers，先确认真实空闲而不是正在构建/模型请求。

若要补设备侧证据，用原ID与固定主机指纹核身份后，逐台只读调用`vibekits.system.info`和有界的`vibekits.system.resources(samples=1,intervalMs=250)`；脱敏只保留平台/PID、CPU测量状态、内存和存储数值，不收Top进程名称、文件或聊天。2026-10-26原在线六机真实工具6/6返回，但Mac155、Mac132、Windows424所报最满卷分别使用98.40%、96.69%、97.43%；高写盘任务前须重新测实际目标卷并清闲置生成物，不能凭单次CPU或HB说系统长期正常。见[六机资源快照](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_SIX_DEVICE_OS_RESOURCE_SNAPSHOT_20261026.md)。

需要逐台OS/MCP长时证据时，项目`tool/original_six_device_os_sampler.py`可作为有界本机运行器的采样器，以独立输出根、约一小时间隔和目标机实际挂载卷运行；它只保存六台在线原ID的CPU/内存/磁盘数值及真实工具成败，原始数据24小时滚动、较旧记录保留逐轮时间/成功设备/PID的小时摘要，不落Top进程名称或聊天。617经用户确认离线时不纳入探针，后续上线须先核原身份再扩充，不能以六台样本冒充七台。2026-10-26实证同一探针已有至少四轮真实定时样本各6/6成功、六台应用PID保持；轮次、间隔和当前容量以原始回执重新读回，这些只是小时采样点，24/72小时仍待验，后端15分钟巡检继续独立运行。高写盘前重测目标卷：第四轮155/132约4.06/4.29GB、Windows424约5.61GB，Mac529从第二轮约43.12GB降到第四轮18.92GB，不能沿用旧容量或单次CPU点判断长期负载。见[监控回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/ORIGINAL_SEVEN_MONITOR_SAMPLER_20261025.md)。

单台OS探针`TimeoutExpired`时保留原失败样本，先核原监控PID/子进程终态、后台独立心跳和同机控制桥状态；不要把探针超时等同整机离线或盲重跑整轮。当前采样器在失败原始回执写固定`errorStage`（连接、核身份、info或resources）与耗时，旧于24小时的原始样本滚为小时汇总时逐设备保留ID、错误码和阶段，不记目标正文；旧第18轮原本没有阶段，不能补造；若原连接仍ready，可各做一次有界只读工具复核，但事后成功不追认原轮次。2026-10-26 Mac132第18轮为这类首败，之后原G73指纹/同一MCP连接的info与资源均成功；下一轮阶段字段尚待真实样本，见[首败与诊断修复](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_MAC132_OS_ROUND18_TIMEOUT_STAGE_DIAGNOSTIC_20261026.md)。

长期七台巡检须有**实际采样回执**，不能只凭自动化已ACTIVE宣称正在监控。项目`tool/original_seven_health_sampler_20261025.py`用指纹绑定的远程档案只读取原七台心跳、两房成员、服务身份及RSS/FD/TCP等有限元数据；原始样本仅留24小时，较旧样本转小时汇总并按时间去重；当前main还对旧于24小时的`scheduled_local`逐条保留时间/成功位/服务PID/新鲜计数或错误码，以便72小时后重建真实定时间隔，但跨日真实滚动仍待验。采样器自身错误与产品故障分开。2026-10-27第88轮本地Ruby/桥接返回非零，公网serverId与随后远端同PID/原六台新鲜均正常；该原轮`CalledProcessError`继续记FAIL。新版采样器仅把未来非零桥接/工具拒绝标为固定`REMOTE_BRIDGE_EXIT`/`REMOTE_TOOL_FAILED`、`sampler_transport`及有限退出码，并在小时汇总留来源，不读取原工具错误正文或盲重跑业务。见[首败与修复](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_BACKEND_MONITOR_ROUND88_BRIDGE_ERROR_20261027.md)。聊天heartbeat自动化历史配置了此只读入口，但2026-10-27现场为`PAUSED`，不能从配置推断仍会唤醒；历史独立本地PID37265曾每15分钟写`scheduled_local`回执，现状须按下方停止与新进程回执核验；手工补采仍标`manual`。核具体进程/新鲜来源，自动化是否恢复遵守用户当次决定，状态不变时保持安静。完整24/72小时与百台真实验收仍要求连续覆盖和真实设备池。只读首轮与留存回归见[原七台监控入口](../../docs/acceptance/ORIGINAL_SEVEN_MONITOR_SAMPLER_20261025.md)。不同同事设备须按各自本机规则提供档案ID与输出根，不照搬别人外盘路径。

计算长期窗口必须用第一/最后样本时间、首尾缺口、内部最大间隔、失败数、服务PID/管理器事件以及逐台真实工具回执。2026-10-26[原七台监控回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/ORIGINAL_SEVEN_MONITOR_SAMPLER_20261025.md)的24条15分钟定时样本首尾只约5.758小时；24条**不等于24小时**，只读24小时审计仍因窗口起点、617缺席、百台真实池及历史PID变化返回BLOCK。即使样本间隔约901秒也不得跳过OS/MCP和服务停启证据。

2026-10-27旧15分钟PID37265与小时OS/MCP PID17181均于原截止前停止，不能再写成当前运行；新15分钟PID55268已实收连续三轮`scheduled_local/ok=true`。接班时必须先查**当前**PID、状态文件、原始样本来源和最后定时起点；进程消失且状态终止后，才沿项目同一 runner/锁恢复，保留空白与失败样本，从新进程的真实连续回执另起窗口。手工补采仍单列`manual`，不能倒填中断区间。小时探针会连接原六台；529由其他会话独占升级期间，不擅自重启这条会触碰529的探针，待执行归属释放后再恢复并核至少两轮。该次[断档、恢复及滚动窗口审计](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_LOCAL_MONITOR_RECOVERY_20261027.md)同时保留445失联、两轮采样失败和服务PID换代，不因新绿样本抹去旧失败。

某台设备被其他会话独占维护时，项目 OS 采样器可显式传 `--exclude-id <原ID> --exclude-reason other_session_maintenance`；项目 runner 的对应参数为 `--maintenance-exclude-id`/`--maintenance-reason`，只转给原 OS 采样器。被排除设备在任何连接前记为 `not_contacted`，原完整六台 `ok/lastOk=false`，其余五台全实收才单列 `lastMaintenanceSubsetOk=true`。维护态输出必须使用独立根与有界运行期，不能把维护态样本拼进完整六台 24/72 小时；责任会话释放设备后再切回无排除的原六台探针。真实五台首轮与限制验证见[维护态回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_FIVE_DEVICE_MAINTENANCE_OS_SAMPLE_20261027.md)。

维护监控的有界期限本身也要巡检。2026-10-28原6小时进程按计划退出后，设备侧两次样本间出现41,648.588秒空白；不能以“正常退出”掩盖连续监控失败。恢复时先核旧PID和状态确已终止、无在途子采样，再用原锁/输出根启动新进程并核首轮回执；当前选用runner允许的7天上限减少短周期到期空档，529仍不接触，达到上限或设备归属释放时须另做受控切换。详情见同一[维护态回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_FIVE_DEVICE_MAINTENANCE_OS_SAMPLE_20261027.md)，不能把这段空白计入24/72小时通过。

观察到设备App PID变化时先对账版本、原安装身份、负责人在途升级事务和恢复回执，再分类计划维护或异常；不能只凭PID变化判崩溃，也不能把升级前后两个PID拼成同一App稳定窗口。2026-10-26第五轮六台设备侧工具6/6成功，但构建Mac155因已授权799→800覆盖从PID95968换为52339，其他五台PID不变；额外Linux101为ARM构建暂退使全池新鲜数10→9，原757恢复后全池回10、该额外ID与两房批准由生产独立读回。它始终不替代617，且新Office包构建完成不等于已安装发布。仍需各自完整24/72小时与服务事件证据。

活跃开发聊天期间若heartbeat没有真实样本，先核其调度状态和来源，再补独立但同范围的有界只读采样，不把手工样本标作调度成功。采样器现支持`--source scheduled_local`与旧manual/heartbeat分开，互斥锁防重叠；2026-10-26本机72小时后台进程前两轮样本成功、间隔901.214秒；完整24/72小时覆盖仍须继续读回。该Mac的LaunchAgent因后台访问外盘被系统拒绝，失败配置已移除；不要为巡检绕过系统磁盘权限，可复用hbbv项目`tool/original_seven_local_monitor_loop.py`，传实际受信profile/桥/输出根/serverId与本机必须挂载的卷；先以独立输出根`--max-runs 1`冒烟，在原监控终止后才对正式根启动，单实例锁会拒绝双开，外盘卸载即停写。当前活跃PID37265仍是先前脚本，整理新入口不等于已切换它。方法及限制见[原七台监控生产回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/ORIGINAL_SEVEN_MONITOR_SAMPLER_20261025.md)。

评估24/72小时定时覆盖时，运行hbbv项目`tool/original_seven_continuity_audit.py --output-root <本机受控目录> --hours 24|72`，它合并raw与较旧小时摘要，分别报告窗口首尾不足、内部漏采、失败、服务PID变化及原七台/真实百台门槛。其`fullG09=BLOCK`刻意保留独立systemd停启日志和逐台OS/MCP长时证据要求；短窗口、六台在线或合成百台不能把总目标改判PASS。当前八条真样本只得到窗口未覆盖、6/7和10/100的BLOCK回执；参见上述监控生产回执。

## 覆盖升级

目标机升级前先冻结原App签名身份和完整指定要求，再在目标本机留私有用户数据副本。Mac旧端可能没有可用Python3，优先用系统`ditto`复制、Ruby标准库逐项按`lstat`比对文件类型/普通文件SHA-256/符号链接目标；原始`diff -qr`会对失效的`node_modules`链接报`No such file`，零差异行不能当作备份PASS。私有manifest至少记录文件数、字节数、链接数、差异数和权限；先读回manifest与原PID，正式覆盖前若用户数据继续变化须重新核对或刷新。备份留在目标私有目录，不上传Git/云端；Keychain/TCC不靠文件复制替代升级后真实权限验收。2026-10-25 Mac445实证为11715文件、986链接、0差异，见[VibeKits七台基线](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/SEVEN_ORIGINAL_LIVE_BASELINE_AFTER_132_RECOVERY_20261025.md)。

冻结最新主线及依赖，记录版本整数/包 SHA/大小/签名/公证/生产来源。先构建 Mac 真实启动验原身份和原授权，再按机型覆盖；共享桥被别人更新时先比较实际候选与源码/签名，采用已合格相同或更新包，不降级覆盖。Win 构建/签名在本机规定数据盘，交互 Session1；保留内外签名及时间戳证据，PIN只由人在设备输入。签名结果未知先追原 PID/事务，不能重签。

当前主线若要求随 Windows Release 携带 NLRemoteAdb，必须在完整 Flutter 编译**之前**沿用 `tool/stage_nlremote_runtime.py --source <已构建的NLRemoteAdb源码根目录>`。核 `native/nlremote/windows/runtime/` 的 `runtime.json`、`nlremote.exe`、`libunwind.dll`、`LICENSE`、`HBBS_CRYPTO_NOTICES.txt`，清单中的文件哈希与实际字节一致，控制器真实 `--help` 声明当前所需的 `managed-relay-v7`。缺源码或任一输入时停在输入门禁，保留旧版运行，不先完整编译再等 CMake 安装阶段失败；不能用旧 v5/v6、改清单标记或删除必需项凑包。2026-10-29 Windows58 的 816 编译已完成而组装因这五项缺失失败，见[首败与精确缺项](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/WINDOWS816_TRANSPARENT_INPUT_RELEASE_STATUS_20261029.md)。前置通过仅证明输入齐备，最终包仍须签名、覆盖和真实协议/界面验收。

Windows58随后出现另一类原生回退：已签817包中的`vibekits-harness-relay.exe`来自10月17日的旧缓存二进制，而原可用789带有后来重建的relay；同一服务上789探测返回`protocol_v4`，817返回`control_response_invalid`。**每次同源Flutter重编也须单独核最终包内relay的源码/构建回执、SHA与真实协议**，不能只验主程序版本、签名或旧stage文件存在。817覆盖守护因两房心跳未恢复而按`HEALTH_COMMIT_DEADLINE`自动回退；不要重复安装这份失败包，也不要通过放松服务鉴权或清配置凑通过。回退后还须看真实界面：58旧789虽恢复原ID、SSH和房间心跳，输入框/对话区布局仍有故障，故“进程与心跳恢复”不能写成“运行正常”。保留回退事务与用户数据，修复同源原生候选后再做真实协议、房间MCP、界面、权限及数据连续验收。见[精确失败与回退](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G02_WINDOWS58_817_ROLLBACK_20261029.md)。

Mac覆盖入口返回`scheduled=true`时还须读**守护终态**。445的817原事务最终`CONCURRENT_OWNER_REJECTED`：旧进程退出后、原子目录交换前，守护发现另一个进程已映射正式App路径而安全退出；正式路径实读仍为811/build2811，回退未尝试。随后目标GUI进程虽在，未显示窗口，工具桥还指向已退出旧PID；普通打开正式App仍需核实际初始化与桥重建。沿登记的同机远程办公终端读取原事务、PID出生时间/完整路径、启动日志及原ID心跳；**不以调度、进程存活或另一台529的界面推断445已升级**，不复用旧桥令牌、清数据、结束来源未明进程或盲重放安装。具体并发进程来源仍待现场核实，见[集群当前交接](https://github.com/caucy2026/priv/blob/main/hbbv/docs/PROJECT_HANDOFF_VIBEKITS_CLUSTER_UPGRADE_ACCEPTANCE_20261011.md)末尾。

安装前保存精确原路径/ID/指纹/授权配置摘要及回滚；独立守护核 PID birth、原身份 MCP、目标版本、房间心跳后 ACK。scheduled/脚本 exit0 不是安装通过。失败恢复原包/原数据，不卸载清数据。Mac Universal/Intel老系统与Windows现有舰队分别验证。商城只发布最终已签验收同一字节包，公开元数据/下载SHA/版本及更新行为核验后称完成；内部商城不等于 Apple/Microsoft Store。

## Harness 调试记录清理

须有明确清理授权。先读所有相关新旧 profile、普通/归档/工作区投影/continuation 关联，按内容/来源确认本任务调试会话白名单，业务、未知、其他聊天保留。不能整目录 rm。冻结所有待删条目的语义/文件 SHA，整批全部验证后才开始删除；通过产品 SessionStore 永久删除及关联清理，不只验证自动描述员为零。先核无运行请求、无审批/模型/外部事务，必要时正常停止本任务 App并由独立守护恢复。删除后逐 profile 验 canonical/projection/pin/archive/workspace 引用消失，并原 ID/MCP/心跳复验。详见随包 harness-debug-reset 文档。

用户明确授权“全部旧聊天”时也须分别核产品当前canonical目录、workspace索引与正式`session_status`，不能把旧台账数量或`ownedDebugOnly=0`当当前全量。Mac529实测4条目录仅3条在workspace，Mac132模板于`WORKSPACE_INDEX_MISMATCH`在删除前拒绝；一条未索引的孤立会话必须独立核来源、仍需对账的使用情况及产品删除/恢复语义，不改索引凑通过，也不因inactive或队列空就停共享App。见[529孤立会话首败](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G10_MAC529_HARNESS_ORPHAN_SESSION_PREFLIGHT_20261026.md)。

磁盘清理只清已核用途/可再生性/无占用的本任务旧 build/cache/重复包，保留源码、Git、签名材料、配置、正式最新包和一个合格回滚；不能按目录名/年龄批删。云构建后执行 cloud-build-cleanup 的已交付验证和回读收尾。

## 代码与交接

共享脏树精确改本任务文件，独立索引/工作区正常 merge/push，冲突主动合并验证，不 reset/stash/all-add/force。记录前后主线 commit、文件、原因、测试、失败及修复、真实部署证据。Git不存密码、token、私钥或原始会话正文。每个阶段更新全目标 G01–G10，未完成不标全通过。

## 模型验证结束但健康仍未就绪

先查原请求的in-flight/terminal/failure、描述来源与时间，再对照健康证明TTL；凭据存在和旧描述不等于当前模型可用。已发现旧客户端Node描述缓存永久命中会抑制过期后的显式复验。源码修复将成功缓存限制为与五分钟健康窗口一致，并保留单飞、失败闸门和零工具约束；源测试通过不代表已部署。不要连续重试verify、切换用户模型或写数据库伪造ready。先核所用正式包是否含修复；按用户授权完成一次真实非缓存请求及新鲜心跳验收。
# 动态房间监控的成员数与观察器归属

原验收设备清单用于检查缺失，不能断言房间成员总数永远等于清单长度。房间新增成员时继续记录全部当前成员，分别输出原清单缺失项、额外成员及各自在线/版本；不能因总数变更让监控静默失败或丢弃新增设备。

采样失败至少保存异常类型和限定错误码，空的AssertionError字符串不是有效诊断。每个观察器使用独立运行目录、PID/开始时间、有限期限、最新有效采样和终态，不把多次追加的历史日志当成一次连续稳定性证明。心跳、模型就绪和实际工具/系统健康分别验证。

替换本任务自己的失效观察器时，先启动新观察器并核真实存活及有效采样，再按旧PID、出生时间和完整脚本路径终止旧观察器；不得停止其他同事或设备App/服务器。采样有界、错误退避，不调用模型，不连接用户已确认关机的设备。正式报告保留摘要；原始临时采样按日志期限清理。


## 原生修复包重新资格验证与构建恢复

若正式候选后来暴露共用原生回归，保留其签名/公证证据但停止该候选部署；同版本号的新包也须以新 SHA 区分。先查主线已存在的修复，核精确文件内容及所有改变的编译输入，不降低枚举大小、协议或权限断言。分别执行各目标架构的实际原生测试和可执行文件构建，读取实际生产编译配置证明，再核最终 App 内的原生正文；源码测试、公证与真实升级分别验收。

Unix socket 测试使用本机构建卷上的短临时路径。构建生成的版本日期和目标 ABI 绑定只在确认生成职责后单独记录，手写输入仍完整验哈希；保留首次失败，不能把未知变化统称为生成物。

复制已签 App 再替换 helper 的候选若出现启动停在加载器、或重新签名被系统拒绝，保留进程/创建时间、加载栈及原始错误，不猜作 JavaScript 故障。不要清除保护属性、更改系统保护或反复签同一被拒候选。本次已验证的恢复路线是独立冻结源码、复用合格工具链和运行库、在新输出中完整构建，再按成熟签名、公证和最终包验证流程执行；不修改已安装 App 来试错。

移动源码层级后，CocoaPods 的组相对路径会逐层组合，不能统一增减父目录次数。对实际生成工程运行完整引用图检查，保持 Pod 锁和缓存版本不变；必要时把外部缓存引用映射为同一份已验证存在的绝对路径，再检查所有源码/资源引用及锁与 Manifest 一致。产品输入不变后才复用原代码测试证据。

观察到编译子进程结束时，控制器可能尚未写终态。先有界复读原控制器和原日志；仅确认真实终态及输入后继续下游，不因这个短暂间隙重复构建、签名或提交。请求人工介入前重新核最新同机回执：历史策略失败可能已由现存合格事务解决，不能把旧失败当当前阻塞。

共享控制桥覆盖前准备完整新包、可验证回退和有界健康恢复；核当前进程/创建时间及正在使用的连接。已有升级授权不等于可以打断他人工作，只协调实际新增的中断时机。公证后仍须原 ID、实际工具、房间心跳、原授权及真实界面验收，不能从身份声明一致推定权限调用已通过。

Mac覆盖后的“同包与旧权限”分开核：正式ZIP完整CRC/哈希及最终公证回执对上后，可流式比对已装App的文件、符号链接和多余项，不解包复制或只凭版本号；签名/Gatekeeper再单独验。Accessibility用当前已装App的`vibekits.device.ui_inspect`在明确目标App上设`promptPermission=false/maxDepth=1/maxNodes=1`做一次真实低暴露调用，只保留`authorized/ok/nodeCount`，不输出窗口正文或主动弹系统授权。2026-10-26构建Mac804的29,507文件/246符号链接与最终ZIP全相同、当前App对Finder一节点AX实收成功；这**只证明本机包字节与Accessibility**，不代替Screen Recording、Full Disk Access、账号/钥匙串或全舰队GUI。见[原机窄门禁](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G02_MAC155_INSTALLED804_READONLY_20261026.md)。

## HTTP 资源边界与真实长连接验证

TLS握手槽只限制握手阶段，不能替代完整连接工作线程上限。检查HTTP请求行和头的读取位置：业务Handler内部的正文超时不会保护进入Handler之前的阻塞。按原协议补足I/O超时和全生命周期槽释放，测试空TLS、半头、半正文、溢出、握手失败及恢复；I/O超时不等于整个业务硬截止，保留SSE生命周期及keepalive。

连接预算要包含每设备保活连接和实际查看房间的浏览器流。300个逻辑设备轮流关闭短连接，不证明300条连接可同时保持；补测逐设备实际HTTPS连接数、每轮在线数、旧epoch拒绝、重新注册和排空后的线程/FD。容量样本、真实设备、生产单连接验证与24/72小时分别记录，不用小并发负载关闭真实扩展门禁。

空客户低占用用独立浏览器标签页观察实际请求名称、状态和数量，不读取认证头、Cookie或正文。共享服务器CPU/RSS含其他设备负载，不能全部归因于该页面。退出后读回登录页再关闭标签页；关闭页面不证明退出已完成。

部署调用超时后，先查原切换意图、终态、实际systemd PID/工作目录/源码SHA、原UUID与持久状态及保护服务。原事务可能已经成功，不能再次restart。恢复验证可用一次有界、正常证书校验、无业务内容的空闲连接探针；不要向生产批量注入负载代替隔离容量验收。

## macOS 自动化的窗口焦点与本轮 QA 归档

若原生自动化只读到空container、窗口标题按钮呈灰色且嵌入Harness点不动，先核实际正式App路径及当前窗口。此次有效路线是原生 Window 菜单中选择实际列出的 Vibekits（makeKeyAndOrderFront），再读新AX树；仅Raise可能只调整层级而未设为当前窗口。不要连续猜坐标、把自动化未激活当整机失联，或据此冒称真实用户首击门禁通过。

本轮合成QA需清理时，先按确切会话ID查idle/无审批，核工作区和标题，再走官方“归档会话”，读回“会话已归档”并保留可恢复性。不能用ownedDebugOnly清单为空证明所有普通会话都清理了，也不能为过狭的调试工具临时伪造归属。此次只归档本轮自己的QA，不代表七台Harness全部清理或永久删除通过。


## 同一事务取证与最新候选对账

大文件诊断证据不要塞进SSH stdout或再包一层base64；先检查stdoutTruncated，超过上限的尾部不能当完整JSON或完整文件。用已登记download_file/SFTP下载同一原始文件，核实际字节和完整SHA，再运行原验证器；保留第一次截断回执，不为修复取证方式重做产品采样。

覆盖升级时，压缩会话日志可能在正常生命周期内追加。逐字节相等未通过就保留原失败，分别核原文件是否仍在、原长度范围完整SHA是否等于升级前/精确备份、追加字节和其他文件是否变化。前缀一致只证明原内容保留，不能写成全部文件逐字节相等；未读取或未获准读取的追加内容，不猜其原因。

服务端委派claimed/completed是消费与收尾记录，不保证工具业务成功。必须同时匹配原请求、目标实际返回和真实PID/版本；一次PlatformException即使已有completed也不能计成功。核当前原生协议、策略有效期、修订和原事务后，才按新的只读请求验证恢复，保留首次错误；后一次成功不证明首次异常已根修，也不替代撤销测试。

修复旧构建失败前，先核共享目录里最新候选及其真实PID/出生时间、输入清单和终态。已有更新候选完成同一修复时复用该事务，不再启动旧版本修复或第二次编译。复用隔离运行时后，canonical helper改变必须同步到该候选自有managed runtime并重新冻结/验对；不改已签App，不只改旧预期hash凑绿。

Windows命令保护要求上传脚本时，停止内联执行并使用受信的固定文件入口；保留当次拒绝，不改执行策略或把被拒操作换包装器继续。上传前核实际暂存位置：若本机规则限定D盘，不能假定工具的默认用户目录已重定向；优先使用现有受信文件传输/SFTP直达D盘，并核完整字节。没有执行的旧方案标为未上传/未执行，不能混作新候选成果。

多窗口远程桌面中，窗口标题、实际目标ID与输入焦点分别核对。键盘粘贴无效时停止连续输入，防止落到其他会话；目录面包屑/鼠标导航可用于取得新证据。本次仅由目录导航发现更新候选并放弃旧修复，没有完成上传，不能据此宣称键盘或文件传输门禁通过。保留其他远程会话，只关闭本任务且无在途操作的窗口。


资源采样须包含实际主进程，不按固定App目录名推断全部范围；历史安装名例如Vibekits 2.app仍有同一个正式Contents/MacOS/Vibekits。当前修复用真实主程序路径补齐主进程并保留其子树；对旧选择逻辑的真实命名负控失败，修后3项范围及原9项CPU门槛测试通过，5%阈值不变。新取证报告仍须核每帧实际主PID存在，不以工具exit0替代。

原生协议探针预期必须绑定本候选冻结源码和实际运行服务。709原生当前实读protocol_v4；旧protocol_v2案例保留为历史证据，不能把它硬编码成所有未来版本的唯一通过值。参数错误的本地CLI输出仍不能代替运行中服务IPC结果。

## 房间准备态、MCP封装与真实文件工具

room_connect的成功准备回执可以是tunnelPrepared=true、connected=false、executionVerified=false：尚未调用工具时，这不是失联。按回执限定的工具执行一次room_call，再核实际结果与断开；不要因connected尚为false重建票据、开启旧名单或重放操作。控制器若在调用前自行断言退出，先核调用是否发生和票据期限；过期后关闭自己的通道，记录设施错误，新只读测试使用新的请求身份。

先读目标真实目录再选toolId，不能把猜测名称的拒绝当权限不足。711→709实测中workspace.list_files不在目录，而vibekits.file_hash按其input参数读取获准文件，返回准确哈希，独立账本及时读到claimed/completed，最后closed=true。此例证明一个真实文件工具，不等于所有业务工具或撤销测试通过。

simulator.call外层ok不替代内层成功。MCP结果可能在data.structuredContent里再包一层ok/data，也要检查isError；只沿当前工具约定解析，不把传输成功、隧道准备、claimed或completed分别冒充业务成功。短票据的独立账本应在本次调用结束后立即读取；超期被清除后不能补造旧证据。

## Mac窗口焦点与自建QA

路径和编辑器输入前同时核真实窗口与文本焦点。AX点击文本栏、Raise或按键返回不保证输入已落到目标；若失焦，沿已验证的Window菜单选择实际Vibekits窗口，在同一操作中按当次截图实际点击输入框，读回focused UI element后再粘贴。先核最终字段值再确认，避免旧路径与新路径被拼接。此路线只解决自动化焦点，不冒称失焦首次物理点击或IME门禁通过。

真实模型文件验证可在独立工作区放随机标记，提示词只给文件名、不含答案；核实际读取轨迹、回答、预览与文件不变。摘要派生另问原标记并禁用工具，核答案及零工具步；分叉不能替代摘要派生。711本机已完成这类实测及置顶/取消、重命名、分叉，父/分叉/派生三条自建会话均走官方归档并读回。只能清理本轮自己确认的会话，不把它扩大成所有设备或其他业务会话清空。

Windows helper可能输出小写SHA，Get-FileHash输出大写；验证完整十六进制格式后规范化比较，文件和期望摘要不变。路径按Windows语义核唯一性与映射；规范化不能掩盖重复项、大小错误或不同字节。最终签名清单还要区分候选PE、Inno内部运行程序、原厂文件及真正不随安装器交付的排除目录。


## Windows覆盖控制：出生时间与运行时XML

- 绑定精确PID生命周期时，使用`Process.StartTime.ToFileTimeUtc().ToString()`。不要把CIM的`CreationDate`转换值与该值直接混用：已实测同一进程相差6个100纳秒刻度。遇到差异先核原PID、路径、主程序哈希及真实Process时间，明确是精度问题后重新绑定；不要放宽时间比较或把差异自动当PID重用。跨JSON/JavaScript传递FileTime使用字符串，避免大整数精度损失。
- 沿用已有schtasks路线时，区分Git中的UTF8归档与已验证的带BOM UTF16运行时XML，声明与字节编码同时一致，独立核SHA再注册。编码失败先核任务、启动意向、实际进程和备份目录；确认未注册/未启动后只恢复原注册步骤，不重编复制、不覆盖已有任务、不重复启动安装。
- 本次619无D盘沿用项目已登记的原用户C目录例外；这不是通用C盘构建许可。备份任务启动和进程存活仅证明在运行，仍须原事务逐文件校验清单及正常终态。

完整实证与历史控制源：VibeKits主线`docs/acceptance/WINDOWS619_710_BACKUP_PREPARATION_20261018.md`、`tool/maintenance/windows619-710-overlay-20261018-v1/`。其中PID、时间、路径和SHA仅供追溯，不可重放。

## 终态、输入值与采样资格的实际对账

有限观察器的state.json可能在退出后仍为OBSERVING；恢复先核terminal.json，再按PID和创建时间查真实进程（排除僵尸）。状态文件或旧PID存在不证明仍在运行；不能据此重复启动，终态也不能仅靠等待超时推断。真实样本下载后比对完整字节数和SHA，正式报告保留汇总，原始临时采样按24小时处理。

Flutter控制端中，AX setValue可能只改变辅助功能显示值，没有改变实际提交的控制器文本。改ID/路径时用已验证窗口激活及真实键盘输入，核实际渲染和提交后的目标身份；拼接ID错误不能归为目标离线。窗口标题、焦点文字和工具返回成功不代替实际目标核验。

CPU/RSS数值通过与严格空闲资格分开：任一次busy、等待审批或未知状态都保留，不能删掉样本再报整段空闲。其他工作繁忙时不强停；记录有负载结果，在确实空闲的窗口补测。模型错误的细分阶段也不等于修复模型；不得用日志或目录ready代替实际模型回执。

房间文件读取逐层检查ok/isError/structuredContent及真实path、algorithm、bytes、digest；不能只在整份JSON里搜索期望哈希。调用后立即读取同一票据的controller、target、消费和完成记录，再结束自有连接；取证用的服务器只读SSH与被测原生房间通道分别说明。一次正向成功不替代反向、撤销、退房或管理员降级用例。


## 按设备判定严格空闲与回执契约

共享控制端可以同时操作其他设备；不能把其他设备的调用算成被测设备负载，也不能仅按工具名筛选就说被测设备没有访问。审计的target字段可能只是工具ID。只在内存中解析可验证的路由元数据，落盘仅保存工具、设备ID、开始时间、耗时和状态，不保存参数或结果正文。核最旧记录覆盖采样开始，按调用起止与完整采样窗口求重叠；限量API不足时补受控持久元数据。路由不明、覆盖不足或有被测设备调用，保留BLOCK，不能猜目标。

采样准备宽限放在测量时钟开始之前，避免启动命令污染首帧；绑定主PID、出生时间、正式路径、版本与主程序SHA，前后核一致。全进程族及原生busy/wait资格与CPU/RSS门槛分开，采集器及自身子进程排除；原验证器及阈值不改。观察终态后查原采集器实际退出，完整原样本按字节/SHA取回，再仅清理已结束任务的精确自有临时数据，源控制和脱敏报告保留。

不同工具族的返回形状不能强套：服务器remote.ssh_exec可有外层ok与exitCode而没有仿真SSH的内层ok。按当前工具契约检查外层成功、退出码、输出完整性与实际业务字段；包装器误判时先离线核原回执，不因异常重发签名、安装、房间票据或工具操作。

codesign退出成功但权限声明输出为空时，先核已装程序和候选的完整签名身份，并按成熟验证器将确实没有额外声明规范化为空字典；不要把空输出直接解释为旧系统损坏，也不要吞掉非空的无效plist或非零退出。安装后的真实权限功能仍需另验。


## Windows资源诊断：区分通知节流、采集与实际负载

完整进程族CPU/RSS数值与严格空闲资格分别评估；控制端路由审计须覆盖SSH、上传等调用，不能只看目标原生工具账本。一个账本零重叠不代表所有载体无工作。记录实际重叠，不把其他设备调用算作本机，也不把整段CPU武断归因某一次访问；没有修复或可核验的新现场条件不重复采样刷绿。

少量GraphicsCapture/D3D栈可能来自WebView纹理呈现，不足以证明有人远程看屏、截图、驱动故障或全部CPU根因。结合原PID/出生时间、主进程与子进程贡献、线程实际归属、已匹配本地符号和调用上下文；未命名或未映射PC保持未知，不用旧PDB或两条栈强行定性。状态快照只证明该时点，不外推整个观察窗口。

核对锁定依赖和实际实现后再理解帧率API。参考webview_windows0.4.0先取捕获帧及surface再判丢帧，通知限帧不等于全部采集成本停止；后续版本不能照搬。先读不含正文的实际ready/busy/可见性/已应用限制及观察原因，再做针对性修复和负回归。不能通过停止浏览器、模型、协同或强退他人会话来制造低CPU，也不直接改共享依赖缓存。一次性受限CPU跟踪须独立命名、确认停止、按期清原始临时数据，正式报告只留脱敏结果及哈希。


### 按运行目录使用呈现诊断

只有目标实际工具目录声明includePresentationState时，才向vibekits.harness.diagnostics传入该参数并设置includeLogTail=false；未声明的旧包不能强传。presentationState是按需内存观察，observed/complete只针对已登记呈现器，不代表全局任务空闲或任何授权。desiredFps是意图，lastAcknowledgedFps是最近成功确认值，0表示无限制，不是实际捕获帧率；disabled仅指优化回退。缺失、失败或截断保持未知。

observationReason固定编号：0未知/旧报文，1安静，2输入法，3动画，4图像，5iframe，6canvas，7播放视频，8嵌入媒体，9SVG动画。仅观察这些有界状态，不取正文、图片URL、像素或凭据；不为取证启动浏览器或暂停模型/服务。此能力的源码通过不等于已在某个设备版本上线，仍以实际目录、精确包及真实回执为准。

## Windows 冻结源码与实际装配输入

- 捆绑技能按规范源的完整目录树与平台运行时逐文件比较。旧版逐文件镜像表会遗漏新增文档；只补已冻结规范源中缺失的文件，既有不同字节、额外文件和链接先阻断，不绕过验证器或顺便删元数据。更新独立完整清单并保留旧清单。
- 编译成功后仍核真实成品的原生组件、版本与来源。主线自带的历史预编译运行时可能被 CMake 再次复制，覆盖之前资格化组件；先核平台最终输入再编译。发现回退时，只复用有精确原始二进制、构建终态、源/补丁清单和测试证明的组件，归档旧装配文件，单列平台覆盖与新冻结清单，核编译核心字节保持，再做完整后置检查。不能把旧原生输入冒充最新构建。
- 完整后置核验用独立任务保存阶段、计数进度、stdout/stderr、资源观察和终态；沿已验证的原桌面用户构建入口执行。控制端等待超时先核同一 PID/创建时间及回执，不能重复启动。原进程确已退出但错误未留存时如实记录，再用最短成品检查定位卡点，修正持久记录后续做；不改权限或绕过明确拒绝。
- 复用既有签名须同时验证原证书和时间戳、精确文件 SHA，以及候选载荷一致性。只在严格字节比较证明差异限于 PE 校验和、证书目录项和尾部证书时复用；比较不替代签名验证。保留 unsigned 源清单、候选装配变化及备份，不修改已签交付包。
- 签名计数从当前清单计算：本次新签、复用既有自有签名、原厂签名分别登记，不能沿用历史版本的常数。原生凭据探针用当前源码和实际 Session，资源首帧先于启动；合成键须删除并原生读回为空，不能用旧版本探针替代新原生输入证明。

## SDK 副本的身份与语义核验

官方会话 SDK 会校验 header 中的 ID、cwd 与存储根。读取备份副本时，为备份与当前目录分别创建匹配各自根的 SDK store；先核副本 SHA，保留完整身份检查。错用原目录根导致拒绝，不等于日志损坏，不能修改 header、关闭检查或把副本恢复覆盖原文件来凑通过。

压缩字节变化后，分别验证 current、无截断及读取前后字节不变，再比较原事件是否完整保留、新增事件类型和业务事件摘要。空会话追加结束元数据不能当作聊天丢失；事件类型计数相同也不能证明旧值未变。不导出正文或敏感值，正式报告记录计数、语义结论与哈希。

## 多设备心跳异常与服务器 I/O

多台心跳过期与 HTTPS 超时同窗出现时，分开核真实仿真、房间心跳及服务器资源，不立即重装客户端或判物理离线。CPU不高也可能有磁盘等待；结合服务 PID/出生时间、I/O PSI、等待通道、数据库大小与时间线，再判断是否需要有界进程 I/O 增量采样。相关性不等于根因。

仅用已有授权的服务器连接采样，不读进程参数正文、环境或用户文件；绑定进程出生时间，未知、消失、新生及计数回退单列，不填零。设置期限、内存和日志上限，不为诊断中断其他任务或调整其优先级。日志扫描超时后保留未知，避免重复扩大扫描。完整窗口失败与恢复后的观察分别保留，观察器正常退出、末尾恢复或后续无异常都不能抹去首个失败。

## Windows保护器自观察与两层busy

Windows的device.processes本身经NativeAppDebugService.inspectProcesses→runProtectedDiagnostic启动同一vibekits-command-guard。查询保护器得到的PID可能就是查询自身，且返回时已退出；不能据此认定外部占用、持续等待或按名称终止它。固定工具的采样结果不是原事务存活证明。

区分控制器ssh_command_busy与目标端exit84/VIBEKITS_COMMAND_BUDGET: busy：前者是控制器已有同机命令，后者在目标创建本次子进程前拒绝。本次确未启动的操作，核原回执及目标路径后沿同一受保护路线恢复；执行结果未知则先对账原PID/出生、日志和产物，不重放。不用裸SSH、策略修改或另一执行工具绕过busy。已有CPU记录可离线分析，必须保留原版本/PID/出生、采样范围和符号匹配限制，不能冒充当前包验收。

## SQLite快照、普通默认补行与时间单位

hbbv持续写入时在线backup可能不能在预算内完成。先核当前journal_mode确为WAL，再用只读连接BEGIN并读取schema建立固定快照，执行有预算的backup，finally rollback释放读事务；目标quick_check通过后才作为有效备份。非WAL不能照搬以免阻塞写者。失败/超时保留原阶段及回执，未切换就是未切换，不重启未知部署；不能仅凭一次超时断言全部原因。原数据库、私钥和配置留在授权的私有位置，不上传Git。

启动迁移可能为已有设备补入普通等级行。与备份逐行核对：既有行须完全保留；新增只允许备份中已存在设备的level=0、revision=0、installation_key=NULL，不是管理员提权。不得将其他等级/绑定变化也归为默认补行。源码回退后继续部署时可在相同逻辑事务内核验并复用已通过的私有快照，不还原实时库、不重复测试；最终切换前后身份/权限摘要仍严格比较，旧失败保持。

room_simulation_delegations原生票据的created/expires/claimed/completed为毫秒，任务lease_until和部分心跳字段为秒。按实际契约确认单位并只转换一次；秒直接和毫秒比较会把过期票据误判为活动。给过期/未过期边界保留回归，不用误报阻塞反复等待。

## 命令长度、传输位置与只读检查点

当前仿真SSH控制器拒绝空命令、NUL及长度超过8192的命令，Base64会继续放大长度。此类格式拒绝没有启动远端操作；长源码沿已验证的文件传输入口执行，不改成更大的内联命令。Windows上传工具的默认临时位置可能是SSH用户目录；有D盘约束时用已登记且核原指纹的同一SFTP载体直接传入独立D盘目录，验完整SHA后再执行。不要调用旧传输脚本的main，它可能操作另一台设备。长度调整不是绕过UnauthorizedAccess或其他执行策略拒绝的许可。

对大文件载荷的只读核验逐个保存目标端检查点，输出只返回计数、身份和哈希。控制端等待必须覆盖原目标预算和收尾；超时先核同一原进程及回执，不能用静默或不存在的本地结果当零文件。已确认原核验退出后可按更小只读单元继续，写入/删除仍按原intent与精确对象对账。容量达到只是该时点事实；其他构建继续写入后，必须重新读可用字节，不复用旧targetReached作为准入。

## 会话维护集合与成品证据边界

session_metadata_list若返回scope=ownedDebugOnly、source=trustedRegistryEmpty或legacyInventoryComplete=false，零条只代表可信登记的自有调试集合为空，不代表全部SDK会话不存在或已清理。继续用原SDK维护路径核旧集合，未知会话不认作可删调试数据；也不能据此认定共享宿主空闲并中断其他任务。只需状态时按当前schema关闭诊断正文与日志尾，避免取回整份工具参数和记录。

完整构建的新SDK、正式签名公证ZIP、staged及实际安装分别记录。兼容复用Cargo target后应明确它已可变，先保留旧合格二进制/依赖证据，不能继续将该目录称为旧版冻结输出。跨平台只移交规范源，ABI绑定等生成物由本平台生成。最终helper小样本查询须保留首个冷查询的长等待，不只选暖样本；相同只读响应或较低单次子进程CPU，不替代整体App空闲、权限连续或最终设备矩阵。

## 原任务封套、分页与精确字节

业务报告和客户端“摘要+工具回执”封套可以是不同派生物，各自绑定自己的完整哈希。审核时分别核消息ID、实例、worker/controller、fence、原生session及原独立验收，不要求两个不同格式的哈希相等。received只是持久接收，processed只能在实际处理后发；已processed先读回，不重复确认，不把ACK当新review、加分或真实安装。已验收任务的租约可能已正确撤销，不能为清pending恢复租约、改DB或重跑业务。

管理MCP的hbbv_task_messages/events已有after/limit；after取服务器cursor/eventId，不是同一发送者的seq。原生App消息工具与管理MCP是不同schema，不能混传参数。先用当前认证目录发现实例，再分页只取目标原行；截断/未知保持缺项，不搜索或解压SDK持久日志、思考或凭据。

需要精确正文时，让仍受原权限约束的工具编排层直接保存结构化返回行，再JSON解码外层、取body字符串编码UTF8并实算长度/SHA；不要再次解析body后重排，也不要让模型手抄大段转义文本或猜格式。受限模型不能改走外部脚本或读取桥接令牌绕过拒绝。完整SHA相同在抗碰撞前提下是字节等价证据，手工重构匹配不是“碰撞巧合”；但原行机械提取更直接高效。错误临时副本、匹配重构副本与原行提取各自记录，不因只查错了一个副本就否定其他证据。

完成恢复仍须运行时真正支持的只读核对路径：已审业务结果、原封套processed、可信注册server身份与全部作用域、本机原生停止和持久化成功分别确认。功能未部署或字段缺失时不猜新API；无session资源任务也不能套用原生会话规则。归档仅限本轮可证明自有且已结束的QA，保留业务证据，不把归档/空调试登记说成物理全清。历史事件中的全队计数与当前只读计数分开标时间。

本机截图能看到窗口不代表它已激活或接收坐标点击。先查焦点与真实控件；窗口Raise不保证取得key焦点，必要时用原生Window菜单中的现有应用项恢复，再取新AX状态。应用已被其他授权更新换进程时，核当前版本/PID/签名与源码绑定，复用合格成果，不重放旧候选或降级；不要把版本变化与焦点恢复混成单一已证根因。


## 部署保护校验与普通等级补齐（2026-10-20实证）

切换前继续使用原有一致性事务备份、原服务身份、原配置SHA与当前PID检查；租约按秒，原生房间委派票据按毫秒核活跃项。历史unknown/effect_reported不是许可，不能清除、重放或伪造完成。

已有服务启动可能为此前已登记但尚无device_levels行的设备补(level=0,revision=0,installation_key=null)。本次已实测首切换后仅新增一行普通默认，原12行无变化，却被整表哈希保护判差异并自动回退。恢复前先证明每条旧等级完全不变、没有删除、每条新行属于备份中已存在设备且严格等于普通默认；其他身份、成员、用户、客户保护摘要必须相同。不得把任意新增、提级、修改安装身份或陌生设备行解释为默认补齐。沿既有ordinary_defaults_only检查恢复，不能跳过保护。

观察失败或超时先读同一控制进程的PID与创建时间、切换intent/state和实际systemd工作目录；未知不能重启。确认已自动回退且同次一致性备份通过、当前保护数据满足原约束后，可以复用该备份恢复同次部署，无需制造多份重复数据库。二次切换仍重新检查源哈希、当前PID/listener、租约/票据和其他服务PID，随后验证新service-info能力、原serverId、签名Key及保护记录。保留首次失败，不恢复旧DB覆盖新业务。

新completion-receipt服务上线不等于客户端已完成：最终同身份客户端还须实际升级、原ID回连、真实模型与只读工具、会话数据及权限连续性；pending journal只有在原processed回执、注册serverId与同原生session/fence inactive均证实后才可自动退役。严格空闲CPU/RSS窗口与主动模型、仿真调用分开；采样未结束不能提前记PASS。


## Windows时间字段、可续作清理与原事务保护（2026-10-20）

同一台Python3.12已实测：路径stat的st_ctime_ns是创建时间，句柄fstat的st_ctime_ns是变更时间；inode、device、size、mtime和birthtime完全相同，直接比较ctime会误判。不能因此删掉时间保护。显式使用st_birthtime_ns，并用GetFileInformationByHandleEx(FileBasicInfo)分别冻结、复核CreationTime/LastWriteTime/ChangeTime；在独占读DELETE句柄内核同一文件ID、完整SHA和PE头，读前读后时间均匹配才标删除，关闭后再核路径消失。保留旧拒绝与修正后的同文件正控，不把元数据误差说成源文件损坏。

保护在途进程也要区分时间来源：CIM CreationDate可能只有微秒，转换成FILETIME后会丢100ns尾数；精确PID代次校验用GetProcessTimes，不以四舍五入或忽略代次替代。不要把观察器到期、状态文件或空窗口标题当作签名结束；PIN仍由人员当次认证，不能重签或接管其他在途事务。

大历史副本先复用原冻结manifest和已完成备份证明，生成有界候选元数据；不要每次重新全树扫描并双重完整哈希。每批核当前保留集合与实际引用，最终完整SHA仍必须在删除前的独占句柄内匹配，源码、文档、配置、原工具链和当前恢复/正式包不进入清单。记录paused/completed、游标与删除日志；只续作已确认paused的批，未知结果先对账。达到当次实测可用字节目标即停，后续源码复制产生新缺口时重新量化，只补所需闲置生成物。

复用SDK输入时核对最新已验证组件，不因旧准备目录存在就编译旧SDK；保留原平台专有输入，禁止把Mac生成的ABI/version文件混入Windows。复用兼容Cargo target前先保全原合格独立raw产物，并验证没有其他构建占用同一可变target。独立硬件签名与无签名构建只能在原进程代次、不同输出路径及资源边界均已证实不冲突时并行；不使用token、不改签名目录、不停止别人的进程。

同名helper也不是重复进程的充分证据：Native8新增固定只读stdio worker，按参数标志、父PID、创建时间区分主服务、stdio worker及短命查询，不能按进程名批量杀。SQL length(TEXT)是字符数，原消息哈希必须对原body字符串直接UTF8编码；例如字符4832与UTF8字节5566可同时正确，不能混用或手工重构正文。


## 压缩会话覆盖后的只读前缀核验

压缩文件字节变化时，不直接把压缩字节前缀当作事件前缀，也不使用只解首个 zstd 帧的工具判断历史缺失。先绑定升级前的精确备份、profile 根、session ID、当前安装包和实际随包 SDK 的完整哈希，再沿该 SDK 已验证的只读持久化接口解码两份日志。比较原事件是否按原顺序完整保留；输出只含计数、状态和摘要，不输出正文或思考。

当前已验证的 readStoredLog 路线会核 session ID、cwd 对应路径、完整多帧和截断状态。使用前核实际版本的方法与字段；只读对象不启动服务、迁移、writer 或 lease，不能把写句柄的 read-only 选项当作无写入证明。读取前后复核两份文件和 SDK/安装身份，发现并发变化则保持未知，不停止其他会话或重放业务。原事件前缀保留只证明这一份历史连续性，不代表其他配置、全部会话、权限或整版升级通过；已有同范围同字节证据先复用。


## 传输账户与执行上下文分开核验

同一设备的 LAN/SFTP 账户能读写工作盘，不代表它能注册另一用户的任务或读取其进程。执行前分别核对传输账户、项目已授权的仿真执行入口、实际 Session 和任务 principal；不要从成功上传推断启动权限，也不要通过伪造用户名、改策略、复制凭据或换身份规避明确拒绝。使用既有执行入口时，仍按它原有的授权和权限返回结果。

发布包的复制目录不一定是签名事务汇总所在目录。源码准备门禁引用 summary 前，读取原事务实际记录的路径及完整 SHA，不能由最终 EXE 的父目录猜出。首轮失败后保留原代码、回执和零写入证明，核原进程/Job 已终止，才以新 attempt 修正路径；不清旧 intent 重放未知任务。Windows 本地化错误保留原始字节和 OEM code page，乱码不能重造为确定的错误号。

## Windows Job 残留与 Mac 运行时预检

Windows 构建主命令 exit0，但自有 Job 仍有成员时，在终止或关闭 Job 前用有界的 `QueryInformationJobObject(JobObjectBasicProcessIdList)` 记录成员；逐个核 `IsProcessInJob`、PID、创建时间和映像名称。权限错误或退出竞态记为未知，不能记成零；句柄关闭后不能补造历史成员。自建 Python 子进程可以与 conhost 同属一个 Job，但普通 Python、cmd、cmd→Python 的真实对照均能自然清空。因此不能凭 conhost 名称推断历史残留无害、放宽门禁或按名称杀全机进程。

未装开发工具的 Mac 上，系统 Python 入口可能只触发命令行工具安装提示。只读运维优先使用实际运行客户端自带的已核验 Node；不要为了读取磁盘或文件信息安装开发环境。若本轮误触发安装提示，只取消已核对来源的那一个提示，并复查窗口或进程已退出。

大文件上传保留原事务和完整回执。专用传输进程存活、文件偏移或 SSH 已发送字节只证明在途进展；远端完整大小与 SHA-256 匹配、更新接口明确暂存后才算暂存完成。传输观察用有界、数字地址采样，不留长期观察器；未知结果先对账，不重复上传或应用。


## 原生身份读取与签名的缺失分支

开发只读身份或账号签名RPC时，核实际getter的空值分支，不凭方法名判断无副作用。已确认Config::get_id在空ID时会gen_id/set_id；只读路径使用get_id_or(空)，缺失／非法原ID在取私钥之前拒绝。已有密钥缺失也保持不可用，不在查询、签名或失败恢复中生成新ID／Key、借另一App身份或重置授权。原生签名仍由实际已认证GUI IPC请求，严格签专用域和原挑战字节，不增加通用签名CLI。

先对真实旧源码或内存变体作无配置访问的负控，再核完整原生候选、实际IPC拒绝／许可和最终签名App覆盖证据；这些层次不能互代。项目tool/test_native_account_readonly_identity.py检查窄处理器，verify_rustdesk_frozen_inputs.py在账号模块存在时拒绝已知生成式API；旧预检器缺这项时不能声称已检查。源码修正及组件测试不是生产同账号互通已可用。

记住设备原生身份与当前账号绑定分开：短期挑战清理和注销可保留原ID／指纹记录，但退出后的历史记录不授访问；当前账号、绑定修订、真实身份、原开关及执行范围仍须重验。不要把历史owner、显示等级或同名账号当作当前本人登录证明。


### Windows任务原生Principal与清理误分类

见[Windows计划任务原生核验](windows-task-native-status.md)：XML缺省字段不是实际权限；核原生Principal和固定action，按HResult处理缺失，守护只读探针不代替真实App退出与全SDK空闲。


### 同账号目录运行时与跨域归属

见[账号设备目录生命周期](account-directory-lifecycle.md)：完整绑定键、精确视图owner、凭据等待竞态、401停止、真实SSE与主线依赖闭包验证；源码组件通过不等于完整远端执行已发布。


### 房间时间校验与等级拒绝

出现INTROSPECTION_TIME_FUTURE、高等级审批拒绝或需要核普通成员双向互访时，读[房间时间与等级恢复](room-time-and-rank.md)。校时、成员资格、管理员等级和原生票据分别验证；关闭通道不是撤销证明。


### 同账号恢复与原生节点观察的交付边界

Phone可信恢复先核原服务caps的phoneTrustedRecovery/version1，只复用原P256、当前绑定/安全修订和仍有效的原MFA；新凭据不能延长原信任。恢复登录成功、设备目录可见、选中设备、operation入库、Host领取、会话/消息实收分别验收，不能合并成“协同已通”。现场对账只查元数据和固定错误码，不读token、密文或聊天正文。

原A/B/C/D观察沿现有Host签名presence，只有features.nativeServerRoute=true及nativeServerRouteVersion=original-native-server-route/1时才发送可选字段。该flag只证明服务器承载格式，旧Host未采样时仍未知。观察绑定同账号、installation/binding和真实Native connectionGeneration；12秒短租约受凭据及目录期限限制，配置节点不能补实际节点。切账号/目标、失联、旧generation和观察过期都清显示；坏可选观察不破坏核心目录或授予权限，不新增轮询。

字段与后续实际验收见公开主线[节点投影合同](https://github.com/caucy2026/vibekits/blob/main/docs/development/NATIVE_SERVER_ROUTE_PROJECTION_V1_20261025.md)和[生产证据](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/NATIVE_SERVER_ROUTE_PRODUCTION_20261025.md)。2026-10-25服务器格式已生产验证，最终Host采样→手机版节点显示/断线撤回仍未完成；不能把某台Root的C当手机或另一电脑的真实节点。

### 房间工具诊断：参数、到期与执行回执

房间票据按实际target/toolId及当前身份签出后，仅在有效期内room_call一次；先核目标真实catalog/当前版本合同，不能照搬同名本地脚本。vibekits.file_hash的已验证参数示例：

```json
{"input":"/System/Library/CoreServices/SystemVersion.plist","params":"sha256"}
```

返回digest/bytes；input是目标设备已获准的实际文件路径。不要误传path造成空输入后将“文件不存在”当整机/后台失败。529实测603字节与132旧样本529字节不同，各设备用自己的实收基线。失败结果已知且原委派claimed/completed后，修正参数使用新requestId/新票据；未知结果先查同一委派，不能重放。独立核created≤claimed≤completed≤expires，再关闭本次新建的通道；不关闭其他任务已有连接。

ROOM_SIMULATION_CONSENT_REVOKED同时可能表示active=false、到期、成员revision变化或安装指纹失配，不能仅凭码断言人为撤销或服务回退。对照当前自有设备许可元数据、成员/身份和必要的部署前快照，区分原因；active=true但expiresAt已过仍不是授权。沿原客户端续期/已授权恢复路线处理，不写SQL补许可、不改走普通仿真绕过拒绝。部署前已过期而切换前后payload相同，不归为本次新代码撤销；这种新请求拒绝也不能代替有效未使用旧票据的撤销验收。


## 手机快照分片与跨证据核对（2026-10-25）

同账号协同的operation终态、结果清单、事件流和界面必须分开。`completed`只说明宿主完成了该operation；`account_collab_results.state=sealed`说明分片已由宿主上传并封装，不能证明手机已收齐。`acknowledged`是源端明确确认并释放暂存分片，也不独立证明GUI渲染正确。事件流的open/closed、sequence和过期时间是另一组证据；它没有逐消费者读取ACK列，不能用该事实否认结果清单的接收确认。只读查询不会触发sweep，存储仍为open/sealed但期限已过时必须另标实际过期。

当前HostReadResultTransfer的sessionSnapshot先校原SDK snapshot header.id与原请求sessionId；最终queue/complete封套只带state及eventCursor，正常不带sessionId。因此审计器从completion顶层提取sessionId得到false/缺失，既不能改为true，也不能直接推断错会话。保持“独立关联未证明”，再用原UI选中项、原构造器对应请求摘要和获授权的原SDK边界分别关联；不为补字段解密聊天或重读SDK制造新事务。代码见[原结果传输](https://github.com/caucy2026/vibekits/blob/main/lib/companion_host/integration/account-sdk-host/host_read_result_transfer.dart)，实际版本仍须与冻结源码对应。

跨会话对账先匹配精确operationId摘要、双方installation/binding、时间、原回执及结果清单；只输出必要状态、大小与计数。相同operation并不能让所有派生字段自动通过。依赖命令必须先等待并检查实际退出状态及结构化结果，再生成后续通知；禁止把“检查命令＋预拟成功消息”当作独立并行步骤。false、缺失、截断与未知分别保留，发现错误说明立即更正到原接收方，按项目资格规则处理，不能自己恢复资格。

操作名未以明文持久化时，可在不读取秘密/业务参数的条件下，对已知公开只读请求形状使用原生产canonical编码离线算摘要；引用前端原构造器的匹配时标明证据来源，不能冒称独立重建全部参数。严格限定源/目标、binding和时间窗；“该窗内没有已接收的发送操作”不代表没有HTTP尝试、其他传输或后续副作用，也不是自动重发许可。未知发送始终保留原草稿和operation，先对账原事务。

## 同账号桌面仿真票据与v2设备事件流

2026-10-27后端生产切换的来源主线为`56b62031`；[生产回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/HBBV_HOST_SIM_PRESENCE_PRODUCTION_20261027.md)给出原serverId/PID、三份只在本地的有效数据库快照、3GB占用、门户链接及七台心跳。后续操作必须重新核实时状态，不能照搬该PID。云端临时归档已按`cloud-build-cleanup`核SHA后清掉，正式数据库/WAL、密钥、当前release和旧release回退保留；旧版模板必须保存原`--enable-auto-service`、账号存储密钥与SDK流参数，不再原样重放。

Phone↔Mac同账号只要求原Harness会话、消息和文件协同，不进入房间，也不要求Phone仿真。已上线的Host v2控制入口为`/api/v2/account/host/peer/{devices,access-trust,tickets/validate}`，需当前Host原生连接、安装签名、同账号绑定和原有短票；接口可用及未认证401不等于手机业务成功，仍按真实发送/接收、换号/注销撤销和旧会话继续验收。Phone/Host`GET /api/v2/account/device-events/stream?after=<cursor>`要求完整路径签名，最多25秒/64槽，只发送设备事件元数据；事件只提示重新取目录，不能续授权或将离线设备直接提升为可操作。手机离线可查看旧聊天、禁止新操作需要界面真机验收。

桌面↔桌面同账号免逐台白名单仿真使用独立`/api/v2/account/host/simulator/{trust,challenge,issue,validate,revoke}`：服务端验双方当前同账号、在线租约、原生双证明、非Phone身份及指定目标端口22/32147/32148/5555/51839。其`client-simulation/1`签名域与旧`client-access/1`的Harness域不同，不能互借票据；服务回执`executionAuthorized=false`，目标原生须另验实际socket/路由/公钥、远程仿真开关、端口和工具/系统权限。20秒短票不能直接支撑持续SSH编译或桌面会话；需保留当前双端身份与撤权检查的安全续期或目标本机任务接管，不能忽略过期或任意加长。隔离原生候选与剩余门禁见[接线记录](https://github.com/caucy2026/vibekits/blob/main/docs/development/ACCOUNT_SIMULATOR_NATIVE_CANDIDATE_20261027.md)。**当前后端已上线，Flutter发起与目标原生接收及双机真实互仿未过，不能宣称桌面免授权仿真已交付。**普通业务房、通用服务房管理员、越级审批、撤权旧票和旧手工授权继续按各自真实正反矩阵验收；房间拒绝不能静默走个人或手工路径。

Android PAD 同账号仿真另有[独立源码候选](https://github.com/caucy2026/vibekits/blob/codex/pad-account-simulator-20261028/docs/development/PAD_ACCOUNT_SIMULATOR_NATIVE_BRIDGE_20261028.md)：VibeKits分支`b979ddfcf0`与RustDesk原生分支`4556dcc4d`，专用MethodChannel/JNI把服务端签名票和确切端口送原生隧道，普通无票PAD隧道不继承同账号权限。原生30项小合同通过且已清生成目标；Android完整编译、签名覆盖、PAD↔Mac真实工具、撤票/续票及Phone拒绝矩阵尚未通过，两个分支均未合main。当前本会话资格暂停时只可源码修复与非交付验证，不能换设备或会话代编译发布。

PAD候选后续`b881ea2a39`增加打包前动态JNI符号门禁：仓库当前随包的旧arm64 `librustdesk.so` 确实缺 `Java_ffi_FFI_harnessOpenAccountSimulationTunnel`，真实旧库负控返回 `PAD_ACCOUNT_SIMULATOR_NATIVE_SYMBOL_MISSING`。合格构建者须从匹配RustDesk分支构建新库并让Release前置检查通过，再验最终APK内符号、原签名身份和真机工具。人工两符号检查器正控只证明门禁解析，不代表新库或APK已合格；不得删除门禁或把普通 `openTunnel` 当替代。

本次后台切换后单张kemi业务房票由本机155访问Mac132，实际`vibekits.system.info`返回目标macOS/PID11381，服务端领取/完成各1。另行打开的529普通仿真连接没有承载这张票，必须按155→132记录。不要把单个只读工具、后端源码测试或固定端口SSE槽数当成全部权限、最终统一包、24/72小时或100台真实设备验收通过。

### 原生账号仿真候选：编译前必验正式输入

本会话曾在隔离RustDesk源码中直接运行Cargo，漏做项目已知的pinned`hbb_common` KEMI补丁与官方协议生成，首轮155个缺符号、次轮18个协议字段错误；修正后Mac arm64 RustDesk lib及36项聚焦测试通过，但按全局AGENTS第11条该执行会话新编译/签名/部署资格仍暂停，不能用后续绿测自我恢复。[原事故](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ACCOUNT_SIMULATOR_NATIVE_INPUT_GATE_INCIDENT_20261027.md)与[修复证据](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ACCOUNT_SIMULATOR_NATIVE_INPUT_GATE_REPAIR_20261027.md)分开保存。新同事使用正式Mac发布脚本可复用其原补丁/生成步骤；**若直接运行Cargo合同编译**，先在隔离工作树调用分支`codex/account-simulator-native-20261027`中的`client/res/verify-account-simulator-native-inputs.py`，其负控须拒绝无补丁与缺协议，完全准备后返回PASS，再启动Cargo。检查器只确认输入，不证明候选已签名、安装或G08真机通过；不改共享submodule或借别的会话规避暂停。

### 禁止访问目录仍需目标OS级全入口约束

用户要求设置中可添加、查看、逐项移除目录，且所有下级目录均禁止远程仿真。当前仍是设计与验收草案，**尚无平台可宣称保护生效**。[白盒入口盘点](https://github.com/caucy2026/vibekits/blob/main/docs/development/REMOTE_PROTECTED_DIRECTORIES_ENTRY_INVENTORY_20261027.md)列出SSH/SCP、文件哈希、房间MCP、同账号短票、浏览器/UI及PAD ADB的真实旁路；Dart字符串路径过滤不能限制Shell/派生进程或已打开的GUI文件。先证明各平台目标OS隔离和真实连接来源，再做设置UI/统一broker；同账号或高级管理员也不能绕过本机规则。按项目PD-A01–A12对祖先、任意深子目录、链接/卷别名、在途操作、旧端和最终包逐项真机验收，缺任一远程入口继续BLOCK。

[官方平台边界核对](https://github.com/caucy2026/vibekits/blob/main/docs/development/REMOTE_PROTECTED_DIRECTORIES_OS_BOUNDARY_20261027.md)进一步记录：Mac全局文件授权拦截需要Apple另行授予Endpoint Security entitlement及相应系统扩展/平台批准，当前正式App只读验签未见该能力；Windows须真正限制进程及桌面，Linux Landlock不作用于旧FD/已有GUI，PAD的ADB由设备端权限域决定。不能在未取得这些平台条件时把普通设置开关标成“已保护”。

## 万级房间心跳与持久连接：两类容量分别验收

[隔离容量回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_SYNTHETIC_10000_SERVICE_HEARTBEAT_20261027.md)与[回执窗口及4秒负控](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_HEARTBEAT_RECEIPT_WINDOW_AND_4S_GATE_20261027.md)须分开解读：1万合成设备按10秒节奏的短连接心跳/重注册通过，现桌面客户端约4秒节奏在同项负载中超期；200条独立保留的TLS连接使当前`ThreadingHTTPServer`线程2→203、FD9→409。末尾“全部在线”、短连接PASS和源测试均不能冒称1万持久连接、真实设备或24/72小时通过。接入层须有界异步处理与背压，不靠调大线程/FD上限；房间在线TTL/同步节奏不能擅自放宽同账号presence、Native证明、撤权和任务租约。

2026-10-29[混合负载与误差纠正](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_MIXED_READ_HEARTBEAT_INSTRUMENT_20261029.md)：正式`ClusterRoomAgent`缓存同一Dart`HttpClient`，仿真隧道还限制单主机一连接；短连接发压只是一类压力，不是正式客户端持续连接模型。合成10,000身份两轮共20,000心跳虽最终全在线，4秒节拍仍约18秒FAIL；管理GET与心跳共用**客户端**线程池时数秒长尾主要是本机排队，独立管理池后GET P95约77–129毫秒，TLS单次建连P95约1.20毫秒，不能据此唯一归因服务端锁。32→64心跳工作线程仍未过；现服务默认最多1,024活动连接，万人持久在线须另测有界接入。生产服务PID于03:25:26 CST正常停启换代，见[连续性回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_MONITOR_SCOPE_RECOVERY_20261028.md)；成功的新样本不能接上旧PID的24/72小时窗口。

后续[锁外准备批量候选负控](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G09_PREPARED_HEARTBEAT_BATCH_NEGATIVE_20261029.md)在隔离源码中先认证、锁外Schema/规范化、提交时重验，6项安全/回执合同及1,000合成身份正控通过；10,000身份两轮20,000心跳仍约22.5秒、两tick排空约7秒，明确节拍FAIL，未合main或部署。不能用最终在线10,000或小规模绿测替代4秒节拍；也不能从不同主机负载的两次实验推出确定性能回退。下一候选按[万人在线实现开发单](https://github.com/caucy2026/priv/blob/main/hbbv/docs/development/G09_TEN_THOUSAND_ONLINE_IMPLEMENTATION_PLAN_20261029.md)同时解决有界持久接入与逐请求耐久ACK，并做100台以上真机及24/72小时验收。

当前私有hbbv主线的[心跳回执修复](https://github.com/caucy2026/priv/blob/main/hbbv/server/device_receipt_retention.py)仅保留每设备同epoch最近16个精确重试，旧序号由healthSeq单调拒绝，其它回执不动；**尚未生产部署**。正式数据库内部freelist空页不是云卷释放量；下次部署仍须本地三份有效一致性备份、云端项目<3GB及`cloud-build-cleanup`。本聊天资格暂停时不自行切换服务或VACUUM。

## Phone多设备Peer票额：先核实际运行版

[票额回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/PHONE_PEER_TICKET_PHASE_CAPACITY_20261027.md)：原生产进程按customer+source把未签发与已签发合计限4；私有main待部署源码沿原表`envelope`状态拆为pending最多4、issued最多16，并在issue转签复核，全局4096及双方签名/身份/短到期/撤销不变。客户端ACK后回收旧票、关闭与未知结果对账仍是独立责任；Native消费本身不释放服务额度。后端聚焦45项和全套1,233项通过不等于生产新额度或Phone55/809八Host业务通过。共享hbbv/server是历史快照，不能单文件拷贝到旧树部署；正式候选从完整私有main冻结。

2026-10-29 05:14 CST[独立生产回读](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G05_PHONE_TICKET_PHASED_PRODUCTION_INDEPENDENT_READBACK_20261029.md)：当前PID`3602076`运行完整新release，原serverId保持，公开`/api/v2/account/capabilities`返回`peerAccessTicketLimits={version:1,accounting:phased,pendingPerSource:4,issuedPerSource:16,globalTickets:4096}`，运行issuer源码SHA与冻结候选匹配；旧PID`3169264`的combined4仅是切换前历史。Phone只在同serverId且字段版本/整数有效时按phased协商，缺字段/null/非法值仍保守legacy；combined仅回combinedPerSource总额，不能解释成两组各4。服务每次challenge/issue仍是最终权威，`fullHarnessCollaborationReady=false`未变化；后台票额上线不等于Phone消息/文件/审批及多机续期通过。进程再换代须重新核PID/cwd/能力字段和真实429，不凭main提交或feature布尔值推当前额度。


## 两台Mac同包：安装树与正式ZIP分别核

[809跨机完整树验收](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/G02_MAC155_445_INSTALLED809_SAME_TREE_20261027.md)的成熟路线：先读每台**实际运行**App路径/PID、原仿真ID、Bundle/Team、严格签名与Gatekeeper，再用[系统Ruby树摘要](https://github.com/caucy2026/vibekits/blob/main/tool/verify_installed_mac_app_tree.rb)逐项核普通文件内容/长度、目录、链接目标与模式；Mac没有可用Python时不要因此安装Xcode命令行工具。只用版本号、Team或主程序SHA不能证明整包同字节。

取得原负责人冻结的最终签名公证ZIP后，先核原SHA/CRC/单一App根与稳定文件身份，再以[不解包流式比对](https://github.com/caucy2026/vibekits/blob/main/tool/verify_formal_mac_zip_installed.py)对一台现装App逐成员比字节、目录、链接与额外项；另一台仅在独立完整树摘要相同后才通过传递等式关联该ZIP。ZIP工具须拒绝`..`与已装App符号链接父目录逃逸，不读取用户工作区。该证明不包括xattr/ACL、旧账号/钥匙串/系统权限、会话数据及全部功能；发布前仍按fleet-compatibility独立验收。首败与修复后回执分开，连接非自建时只读复用、不替他人断开。


## 同Bundle旧入口接管：先核运行路径，再决定恢复

[Mac529现场](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G02_MAC529_OLD_APP_RELAUNCH_20261027.md)证明：较新已签2799仍在缓存路径时，旧正式`/Applications/Vibekits.app` build2723也能重新运行并以同一原ID报新鲜心跳。设备显示“在线”、签名有效、另一份新App仍存在，都不能证明**当前进程**是新版。发现版本倒退时，按当前PID出生时间与完整可执行路径、两个App的Info.plist/签名、服务器新鲜版本与工具目录交叉核验；旧模型ready在进程更换后标为历史，不继续当当前证明。LaunchServices的`launch job demand`不能唯一证明用户、登录项或更新器是发起者，缺原始日志就保留未知。

恢复前与设备原负责人核在途操作和用户数据/授权快照；合格同签候选应覆盖被普通入口启动的**正式路径**，而非只把缓存新版重新打开。结束后分别从普通入口和冷启动验实际路径/PID/版本、原ID/主机指纹、账号/会话/系统权限、两房心跳及真实工具，并在下一次重启确认不会回到旧包。资格暂停或他人连接在途时只读冻结并协调，不自行停App、清配置或代装。


## 加入房间后申请中不被旧left快照抹掉

[当前源码修复与负控](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ROOM_APPLY_STALE_LEFT_UI_SOURCE_20261027.md)：客户端已持久记住`checking/pending`申请回执时，随后房间列表短暂返回旧`membership=left`或关闭公开入口，面板仍应显示“申请中”并禁重复申请；服务器新`approved/rejected/revoked`终态优先。UI回执只是显示/防重，不是设备或房间仿真授权。验收要在最终签名客户端真实执行申请→刷新/重开→审批或拒绝→两端设备列表/权限更新，并独立核服务端无第二条重复申请；现装811未包含此后加源码，不可把14项组件绿测写成已交付。

本次隔离测试曾两次因漏检输入闭包失败，详见[事故](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ROOM_APPLY_SPARSE_INPUT_INCIDENT_20261027.md)。后续源码合同测试先核完整`lib`、本地path包和pubspec资源均存在，再运行锁定依赖；0项用例执行的求解/导入失败不是产品回归，也不能以补测绿灯自行恢复执行资格。
