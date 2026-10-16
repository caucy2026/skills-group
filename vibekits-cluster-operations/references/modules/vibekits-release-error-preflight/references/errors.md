# 已有证据的错误与必须验收的回归

## MAC616 冻结版本遗漏（2026-10-11）

本轮执行者复制 615 冻结输入时只改 pubspec/Xcode 参数，漏改 Dart `AppVersion` 与 macOS 生成配置，并漏执行已有版本门禁。616 签名、公证均通过，但安装目录为2616、实时桥为2615，启动核验未通过。仅本机诊断，未发布或推送远端；不能称完整验收成功。修正617仍需最终包实测，不以新增门禁授予PASS。

此事故补充现有 `version-identity`，不增加 PAD 矩阵或放宽旧门禁。构建前执行项目 `tool/verify_app_version.mjs <实际源码> --require-macos-generated`；构建后附带实际APP路径；共享签名入口已在首次签名前强制检查，隔离源码通过 `VIBEKITS_BUILD_SOURCE_ROOT` 指定。覆盖后必须实时桥、包版本与监听进程一致。错误616已被签名前负控拒绝，候选签名未变；已有版本回归包含正例与两项生成配置反例。项目详细记录为 `docs/acceptance/HARNESS617_VERSION_GATE_INCIDENT_20261011.md`。

本表汇总目前项目事故记录及本轮已确认错误。完整原始来源为项目 `docs/acceptance/BUILD_RELEASE_INCIDENTS_2026-10-03.md`（INC-01～13、MH 与后续事故）；具体版本和原失败不可删除。新发现事故在本表及本项目原台账追加，不以“已经全部整理”掩盖未检索历史。

| ID / 平台 | 我犯过的错误 | 必须验证的结果 |
|---|---|---|
| source-inputs / 全端 | 递归排除 build 删掉运行依赖；复制旧文件名清单漏新增源码/资源/依赖图；漏 cwd/TMPDIR；共享源码与实装核心混淆 | 精确冻结输入闭包、资源与锁通过已有检查；实际命令和原生二进制来源绑定。缺依赖负控拒绝；不把未打包源码当实机根因。 |
| version-identity / 全端 | pubspec、AppVersion、生成配置或实际包版本不一致；只认文件名 | 构建前原工具核对源码及生成版本，签后核对精确包版本/架构/哈希。 |
| package-completeness / 全端 | 开发机已有组件掩盖新机漏包；运行时子目录被排除；旧 helper 低于宿主要求；签后组件同名不同字节 | 精确包解包检查全部必需组件、技能、真实平台解析入口、版本和同签名；全新安装能跑。不得拿预装依赖代替。 |
| runtime-functions / 全端 | import/help 成功冒充真正功能；MCP catalog 成功冒充工具执行 | 实际 Node/SDK/原生模块功能、真实锁与竞争、模型与工具调用；不能用受控 Builder 编译冒充模型自主开发。 |
| upgrade-continuity / 全端 | 重置数据/钥匙串来掩盖兼容问题；覆盖升级丢身份/授权；先停旧版再构建导致长时间不可用 | 已授权旧版到同身份新包覆盖后原功能直接可用，ID/授权/Key/名单/会话保留；候选先准备完，失败恢复原包。 |
| routing-auth-identity / 全端 | 混淆硬件ID与认证密钥，清理重生成后冒称身份连续 | 升级保留身份；PAD卸载删除传输身份副本后重新认证；ID不变保留配置/Key/会话，ID变化清旧设备绑定数据。禁止仅凭MAC覆盖服务器身份或假称授权延续。 |
| startup-recoverability / 全端 | 离线/认证失败/注册不返回导致永久忙或主界面不可用 | 最终包缺失/失效Key、服务器离线、同ID新密钥拒绝、ID变化、注册错误及不返回均有期限并结束忙态；真实Key输入/设置/认证入口可操作、状态真实、不无限重试、迟到事务不覆新状态；网络/并发/生命周期至少三次。 |
| startup-single-instance / 全端 | 启动返回错误就再启动，双实例抢端口；安装事务回包丢失即重复执行；旧路径进程误当当前版 | 命令无论成功失败先核实际 PID/路径/创建时间和原回执；唯一主实例/端口归属，冷启动及再次进入实际可用。 |
| simulation-reentry / 全端 | 进程/蓝点/服务器TCP可达冒充仿真成功；断联直接当设备离线；Android误把APK作为桌面恢复命令 | 原 ID 真握手、真实只读工具、ADB/授权/房间心跳；断线再次进入恢复；Android禁止 APK/桌面恢复执行，失败不能永久忙。 |
| credential-replacement / 全端 | legacy 保存新 Key，而已存在 official 文件继续旧 Key；旧镜像迟到盖掉新值；缓存/原 UID AES 文件冒充卸载继承 | 两个实际保存入口及正式 SDK resolve 都用新值；持久提交回读；正常重装恢复最新值、不覆盖已有新值。只记录可用性/版本，不记录 Key。 |
| truthful-status / 全端 | 没网络却显示服务器在线；仅注册缓存/开关/中继进程推导在线；多个位置等待动画 | 已在线、仅可达、离线、未知分开；断网/恢复实测；一个任务只一个忙状态，服务器静态指示灯按真实证据。 |
| session-lifecycle / 全端 | 删除后索引/派生/投影回写复活；菜单被删/重复/无效；队列或上下文压缩误当完整模型循环 | 全部实际菜单动作、普通/派生会话、刷新/重启/覆盖后删除不复活；无关会话保留，真实上下文/模型循环按原目标验收。 |
| resource-lifecycle / 全端 | helper 606%高CPU；用负载均值冒充CPU；未严格空闲就宣称通过；杀进程当修复 | 真实进程族 CPU/RSS/线程/子进程及退出回收；明确空闲前提；旧高CPU/内存证据不抹去。 |
| market-install / 全端 | 组件点击安装无效果；上传成功当发布；大小单位换算误判 | 用户实际点击下载/安装反馈、OS确认、PackageManager/已装文件hash、真实功能；商城下载hash和旧版/新版更新比较正确。 |
| evidence-integrity / 全端 | 错目录、旧缓存、输出截断、未进入断言的设施错误当通过；覆盖首失败；猜根因当事实 | 每项区分产品/设施/环境，证据绑定此包；保留首失败与负控；原生故障先读实际错误/日志，不无限造探针、猜菜单和重复轮询。 |
| 安装事务变体（startup-single-instance） | 增量安装报MEDIA_UNAVAILABLE后备用串口其实是75，安装结果未知就重装/误操作其他设备 | 安装前确认已验证模式与必要输入；失败后先查同一事务和实际包版本；串口变化先验同机身份。不重启共享ADB服务器，不操作未授权设备，不将输送失败等同安装未发生。 |
| delivery-cleanup / 全端 | 未远端读回就称云备份；云缓存、临时包遗留；清掉唯一原生来源/回退或在途文件 | 回读代码/文档提交；发布字节验证；安全清理后读回，保留来源闭包/正式包/必要证据；实际云构建必须用 cleanup 技能。 |
| pad-native-helper / PAD | unresolved FFmpeg native imports；helper5而宿主需要9；替换签名后新装失败 | 最终APK FFmpeg/JNI依赖、helper要求/内层外层C8签名门禁；坏427/458或等价负控被拒；冷启动/后台服务注册真机实证。 |
| pad-input-display / PAD | 搜索点击不出软键盘；旧IME残留短条；同屏操作其他APK；GPU取图造成实际系统卡死后仍重复 | 真点击与IME高度/输入/收起；D0 Harness、D1目标APK；遵守目标已验证图形边界，不擅自触发有已证崩溃风险的采集。 |
| mac-signing-loader / macOS | 内层未签先签外层；确定性签名错误重复重试；错误公证profile；ditto合并签名App；漏macOS12平台入口 | 内到外签名、最近成功公证配置、完整包原子替换；两架构真实模块功能、真实解析基址/Safari兼容；原身份权限继续可用。 |
| mac-first-input / macOS | 第二次激活可用冒充首次点击通过；WebKit异步重复同键事件导致高CPU；防重放吞正常快捷键 | 非活动首次点击、中文IME、粘贴/快捷键/长按/菜单；停止输入后事件计数不持续增长，真机资源通过。 |
| windows-package-updater / Windows | 缺/混CRT；原生载荷更新但来源侧车旧；Job杀升级器；不同PowerShell环境；硬令牌PIN或外壳事务未知仍重复签 | 完整同源Release/官方CRT/动态PE分类与来源；升级器脱离旧Job且同命令环境；内外签名终态与真实覆盖/授权连续。 |
| windows-permission-ui / Windows | native确认已打包但Dart排除Windows；consent_pending没有有效UI；VC异常无dump却猜缺文件 | 允许/拒绝/撤销/既有授权实机验证；崩溃具体记录及调用栈/最短复现，不清配置或随机替换系统DLL。 |

已有证据路径：`PAD_DEV458_EMBEDDED_HELPER_INCIDENT_2026-10-03.md`、`FLUTTER_FROZEN_INPUT_INCIDENT_2026-10-02.md`、`PAD522_VERSION_GATE_INCIDENT_2026-10-05.md`、`WINDOWS_UPGRADE_INCIDENT_REVIEW_2026-10-02.md`、`HARNESS_LOCAL_SESSION_LIFECYCLE_INCIDENT_20261007.md`、`PAD_SIMULATION_AND_CREDENTIAL_PRIORITY_20261009.md`。均相对当前项目 `docs/acceptance/`，不绑定某同事磁盘。

检查回执：phase=prepublish/delivery；artifact={path,sha256,bytes,platform,version,build}；platform=pad/macos/windows。results 每项为 {id,status:"pass",artifactSha256,evidence:[{path,sha256}]}。发布前公共15项（delivery-cleanup 在交付后）及当前平台项必须全部存在（PAD含额外5项）；交付时公共16项及平台项全部存在（PAD共7项），不能自行 N/A。证据中保存实际动作/断言与执行退出码。用户明确接受某个缺口须在原发布流程单独记录，不能伪造成 PASS 或让本脚本免检。

PAD额外5个独立必验项见[逐项表](pad-identity-startup-20261009.md)，均纳入检查器，不得由一般startup行替代。Windows另须覆盖原619双SSHD/Restricted身份查询：全owner身份和创建时间有证据，未知owner不忽略，既有SSHD/密钥/权限保留，最终包原ID实际SSH/MCP调用。

## PAD593：备份占用期间提交任务（2026-10-10）

实机593/2593接受只读任务后2ms即报 `host_snapshot_cut_pending`。已定位 `_run` 在 agent 预抢占预约之前执行工作区设置保存，其同步 admission 检查可直接抛错；备份显示 incomplete 本身不能证明旧 cut 永久遗留。此项归入现有 runtime-functions、resource-lifecycle、startup-recoverability，不能仅凭单独备份或模型测试通过。

回归必须从真实任务入口触发：备份持有/等待 cut 时提交任务，前置会话保存、工作区设置保存及 SDK 启动共同遵守原预约，等待实际 worker/Native 退出后执行；不得吞掉保存错误、强解锁、忽略未知退出或重复提交。保留旧行为失败、修后整链路通过和最终包实机证据；按原并发门禁至少三次。状态诊断区分 host cut、SDK admission、活动 producer 与实际恢复要求，不以历史 incomplete 标签推断当前锁状态。

另须覆盖全新主APK启动时内置helper尚未自动准备完成的时序：复用既有组件准备流程，有界等待实际要求版本；就绪后继续，失败保留可操作Key/主界面及明确重试入口。此为待验证风险，不能写成已发生的593事故或已完成修复。

## PAD增量安装触发内核异常（2026-10-10，诊断包同样适用）

63上安装诊断probe时，裸 `adb install -r` 自动尝试增量安装。前一安装日志已记录 `Performing Incremental Install`、`INSTALL_FAILED_MEDIA_UNAVAILABLE` 后回退流式成功；后一次同方式安装超时，设备boot ID变化，pstore确认 `DataLoaderManag` 在 `eventfd_write+0x2f8/0x48c` 对地址 `ffffffffffffffe8` 的内核分页异常，随后panic。诊断包新hash未落盘，主程序仍594。这证明安装通道与崩溃时间/线程关联，不等于已定位内核源码根因，不能归咎于Mali或Harness业务代码。

在此PAD强制沿成熟文件安装路线：先核同机身份、原事务与实际包hash，再经仿真传APK到精确自有暂存文件、校验hash，然后 `pm install -r <已核验设备路径>`；探针、组件和主APK一视同仁，不能因文件小省略。禁止裸 `adb install` 自动选择incremental；保留idsig证据，不靠删除签名侧车规避方法检查。遇到任何incremental/incfs/DataLoader失败，即使随后Success也要记录并更正后续安装方式，不能仅看最终exit0。

超时后先用独立已验证备用通道读原包版本/hash和启动原因，不重复未知安装。kernel panic证据留存后，不复现同一增量风险路径；继续不受影响的源码工作与普通文件安装验收。必须验证原ID、真实ADB、实际功能及数据连续性，不能把重新开机当作修复完成。

## PAD597：上下文诊断查询干扰空闲备份（2026-10-10）

597生产工具桥的context_status handler返回状态后，通用invoke仍写活动审计；该store注册settings producer，可取消正在进行的idle snapshot并递增完成epoch。真实bridge/store/scheduler隔离红控已复现一次查询使在途备份取消；不是此前未发布的changes订阅回读缺陷。连续读到saving不能证明同一flight卡住，收到held=true回复后再提交任务也不能证明任务本身触发了原cut的预抢占。UI导航设置保存同样属于真实producer，不能称无查询期间一定空闲。

此项归入evidence-integrity、resource-lifecycle和runtime-functions：仅固定上下文诊断接口保持纯观测，不写活动文件、不发布work-status、不创建producer或改变epoch，仍执行原工具定义与授权校验；普通工具继续审计。以真实invoke+store+scheduler证明查询前后token未取消、epoch不变、备份可完成，保留旧实现红控；最终包补无扰动状态观察→真实任务入口的并发回归。首代真实saved仍有效，尚未提交的新一代及普通卸载恢复不可冒称通过。修复及实机复验状态另记，不把本条新增当作修复完成。

原失败证据：resources-dev523-20261005/snapshot-context-observer597/observer-before.log。

## PAD598诊断探针：正式包类名不可直接反射（2026-10-10）

独立V2只读probe在完整wire/front读取后，于native_live_readback报ClassNotFoundException，INSTRUMENTATION_CODE=2；不能当作备份损坏或验真通过。598实际R8 mapping证明PadSnapshotNativeReadback.verify已合并/改名至其他类，测试使用构建前class成功不证明Release宿主保留原类名。原失败与93b1e6d7开头probe包保留。

仅针对使用宿主反射的诊断工具：执行前核对最终签名包的实际可解析类/方法及依赖；不能以Java/Kotlin源码或未混淆classes代替。优先将已验证实际校验源码和依赖在诊断包中隔离封装，并验证D8闭包、正负读回规则；不为探针给正式应用随意加Keep，不硬编码某一版混淆名，不以弱化元数据验证代替文件字节校验。实际Instrumentation终态和业务断言均通过才计入设备证据。host-target操作须已确认无用户任务/持久队列/实际备份持锁并有独立恢复；只读诊断不自动授权卸载。

证据：resources-dev523-20261005/device598-acceptance/v2-readback/instrumentation.log及source598/build/app/outputs/mapping/release/mapping.txt。未卸载主程序或删除数据，之后通过独立LAN恢复D0。

## PAD会话等待预算与诊断纯读（599实机，2026-10-10）

598的session_wait传15/30秒时，控制端普通tools/call的8秒传输预算先触发mcp_timeout；任务本身仍在同session完成。599仅Android将目录及handler最大/默认改5秒，status/history/wait不写活动审计或忙状态，授权验证与prompt/cancel/普通工具审计保留。真实默认等待6.792秒返回changed=false，不能把无变化当失败或重复提交请求。发布回归须同时核目录、默认/钳制与实际传输，不只验证Broker本地等待。

## 运行时退出确认与诊断分流（600未实装候选）

真实线程红控确认旧Native在worker自身尚存活时发回复；Dart100ms额外status确认可因调度迟滞误拒已完成proof。候选以原worker真实join后同requestId的known/exitConfirmed证明交付，旧回复保留原有界fallback；不得用取消标志、工作函数返回或模拟true代替线程退出。永久回归tool/pad_runtime_verification_jobs/run.py覆盖真实线程、延迟取消与拒绝overlap，Dart对应fence及完整V2 coordinator回归保留。预算与未确认退出持锁保护不扩大；现场根因需实机复验，不能用此红控直接宣称已解决599所有失败。

仅诊断修订不得改变控制分流。未实装v1曾覆盖scope_incomplete令原终止变可重试；v2已仅对两种合并异常补固定runtime类别，scope缺失仍terminal、不重试。验证诊断时必须检查成功、缺范围、未确认退出三路的原状态机语义，不能只检查新字段出现。

## PAD600～601：完整运行目录串行校验超过单次预算（2026-10-10）

600首轮曾真实saved/gen6并读回20消息；探针结束恢复主界面后的三次备份分别在full_readback、runtime_verify等阶段记录runtime_timeout，锁释放后有界重试，不能用首轮成功代替生命周期稳定。只读重编译诊断在同63量到：warm33.599秒，单次完整验证94.222秒；当前和旧目录各55074个文件、约971MB。归档SHA3.374秒、当前树及晚期检查约35.365秒、旧树及晚期检查约55.471秒。超出生产90秒是可重现实证；这是非R8/非生产prepareLock的诊断，不等价最终APK通过。最早冻结593已存在串行双树结构，不把593所有其他范围/准入错误统归此原因。

最小修复固定最多两个工作线程：归档认证先行，两树保持全部字节、集合、链接、marker与晚期变化校验；原Job必须真实join唯一子线程才返回/释放。取消未退出仍保持原保护，预算不增加，不删除旧目录或缓存实际树结果。相同设备、相同文件/字节数的只读对比38.797秒，全量验证通过；正式601首轮自动备份已saved，再由独立helper V2读回gen9、26文件、20消息与live逐字节一致。模型、重装及三轮生命周期等剩余验收仍未完成，未正式发布。

永久回归：tool/pad_runtime_verification_jobs/run.py --suite all。实际双线程屏障、完整读字节/opens、两树晚期链接、长子线程不退出时原Job不能exit/接下个请求均需通过；最终签名APK还须至少三轮启动/任务抢占/自动保存与真实退出证据。成功一次或只读probe性能不能免除最终包验收。

证据：resources-dev523-20261005/device600-acceptance/restart-runtime-timeout/、runtime-phase-probe/metadata.json、runtime-parallel-probe/comparison.json、device601-acceptance/v2-readback/upgrade-proof.json。

## PAD同ID卸载后的名单继承与撤销持久化（601候选，2026-10-10）

旧removed路径删除pair同时删唯一consent，V2仅保存显示名；显示名回读不能冒充名单继承。直接保留旧ledger也受target公钥绑定拒绝。另有本地FFI撤销已提交、helper保存失败时旧Allow复活风险；单条unknown若全量撤销又会破坏无关有效授权。

601候选在现helper保存同硬件/签名下已明确的controller公钥与决策，正常卸载只删旧传输pair/active ledger，退休名单按同scope真实新target重绑；ID变化清旧设备名单。明确操作先持久化限定对象intent再FFI提交、同token/精确delta确认；unknown只关闭受影响Allow，其他有效授权保持，未确认新控制端不产生Allow。同步明确拒绝且原字节未变才精确abort，迟到不得清新事务。完整scope核验到写入与迁移/卸载共用既有锁序，防旧AAD迟写新scope。

核心/真实移除路径/三入口及真实线程正负控已通过，真实helper25自动升级及cover原公开身份、会话/Key可用性已读回；普通卸载、实际新target认证及真实allow/deny/revoke/未知控制端尚未通过，不标名单恢复完成。永久回归tool/pad_consent_continuity_test/；最终包必须同时验证旧pair不存在、原允许/拒绝/黑名单/撤销按规则生效、新controller公钥未获授权、Key/聊天保持及后续Key替换。


## PAD601 首次授权被后台刷新打断（2026-10-10）

已复现旧助手25的 begin→后台loadConsent→finish 交错会把活授权事务当中断恢复，导致确认失效。串行及已有白名单设备不能代替新设备首次Allow并发验收。后续完整APK必须携带同签名助手及宿主配套修复；活事务使用明确Binder owner并正常/异常finally关闭，死亡/关闭/过期/未知仍failclosed。验证旧负控、至少三轮并发和最终包实际跨进程Allow→持久化→fresh connect→真实工具；JVM doubles不计实机通过。安装不得只看version，需签名及同版本APK内容匹配，保留合法较新组件。详见项目PAD601_FRESH_CONSENT_INCIDENT_20261010.md。

## PAD602 绑定服务提前返回后不能重试（2026-10-10）

完整2602正确安装主程序及助手27后，2075278498仍报告ANDROID_REGISTRATION_PENDING。实时ServiceRecord仍有主进程Binding，旧注册诊断PID不得冒充当前进程。源码onCreate失败标记/consumer lease失败后stopSelf提前返回；绑定服务不必被销毁，显式重试只清标记并发送START，而initialized=false的旧guard拒绝它，不能重新初始化。此前白名单修复不能冒称已修此注册故障。

必须验收：失败标记或暂不可用lease的bound service→条件恢复→第一次明确用户enable重走安全初始化；helper未就绪的异步singleflight不重复；实际新FFI启动使用新attempt时钟，不能沿用绑定数分钟前的旧截止；STATUS/页面刷新只读不复活失败事务，保留身份/Key/名单/数据。最终完整签名APK读回版本/hash/内嵌组件和当前PID/stage，再完成真实注册、用户首次白名单、fresh仿真及真实只读工具调用。修复未实测不得发布为已验证新机开箱可用。详见项目PAD602_BOUND_SERVICE_RETRY_INCIDENT_20261010.md。

## PAD603–607：新增永久检查（2026-10-10）

W55：身份以认证解密ID及完整pair核验。同身份不同nonce通过；坏MAC、不同ID/pair拒绝。读当前PID/stage，不无证据清认证或Key。

W56：新功能必须核最终APK完整插件资产、导入依赖与PAD ACP加载入口。2607起运行check_pad_scoped_invoke_closure.py；两asset逐SHA、pubspec、自有文件marker及原--patch链通过后，还须真实SDK和最终Android调用。原607缺包负控BLOCK且未部署，不放宽scope掩盖漏包。

W57：目录查询在prepend middleware中，SDK timeout-policy的next尚未进入。目录和风险body须共用同一有界预算，caller/agent/plugin卸载均结束，迟到批准零dispatch；readOnly正文原next，SDK核心不改。计时器缩放不是实际60秒墙钟验证。

取消测试必须区分生产退出与测试管道。生产cancelHTTP200、registryWithdrawn、SDK idle/disposed及writes/grants0已证明撤回；旧fixture resumed stdin令Node不退出，单独关父stdin便exit0。保首失败，关闭自有输入/读者，不加20秒或误改生产取消。

详见项目docs/acceptance/PAD2601_TO_2607_CHANGELOG_20261010.md及PAD607_GENERIC_PLUGIN_PACKAGING_INCIDENT_20261010.md。矩阵72项逐最终包证据验收；63当前2601与2075278498当前2606分开记录，不混算。

## PAD607 W58/W59：完整备份scope与fallback审批生命周期（2026-10-10）

W58：新增owned插件实际写入ACP私有目录后，Dart及helper固定scope同时缺两条脚本，2607实际自动备份返回host/unsupported_scope。只增加sdk/acp/vibekits-host/harness_scoped_tool_invocations.mjs和pad-scoped-tool-invocations.mjs两条精确白名单；原pad-native-attachments.patch.yml已覆盖。Dart捕获/编码/恢复、helper Producer/WireCodec/commit/load/restore必须同意同一集合，未知、链接、穿越、源变化仍拒绝。后续整包内置同签helper29，RemoteAdbBootstrap.requiredVersion与PadHostCredentialClient.MIN_HELPER均29；旧helper28负控拒绝，实际新helper、三轮saved及完整实收回读才计最终包通过，不以两端fixture代替实机。

W59：实际fallback审批在60秒过期或原任务结束后仍可见。审批绑定原request/任务与截止，完成/取消/失败/卸载上下文及时关闭本次route；迟到允许零旧handler/新增grant，无关新弹窗保留。Root安全拒绝旧min且独立音量100只证明本次拒绝安全；最终包须真实及时允许、拒绝、超时、任务终态及迟到点击，生命周期至少三轮。未实测不关闭此case。

两项已加入永久72项矩阵（59异常/风险、13需求），旧70case不删不改；不是59次故障，也不是全72项已通过。新增矩阵SHA使旧回执失效。当前2607这两项仍未闭合，不据本次文档宣称正式发布全部通过。

## PAD608：自动更新helper后宿主未恢复（W60，2026-10-10）

helper29安装替换旧provider时，Android installPackageLI终止其依赖relay与前台host；完成receiver在新进程里callbacks为空直接返回，原UI/仿真未自动恢复，Root再次打开才继续。不是独立业务崩溃，也不能以重新打开后工具可用关闭自动升级事故。

固定helper调用使用每次获取并关闭的unstable ContentProviderClient，死亡/不可用/null reply保持未知失败，不自动重放写/CAS，不生成新ID或清Key；原identity restoreFailed门禁不变。session/token/目标版本hash/boot/deadline/原enabled journal使用现有已覆盖simulator_service，成功且当前仍enabled才沿原KEEP_ALIVE一次恢复；失败/取消/pending不假ready，晚回不清新事务，用户关闭不复活。安装资格与恢复journal成功分开，STATUS_SUCCESS仍须实际包资格复核。pending系统确认UI未覆盖不能伪造通过。

最终签名包必须真实触发旧设备helper更新及新机自动准备，至少三轮验证原前台持续可用、当前用户意图、原身份/Key/会话/名单及fresh仿真/ADB；不得任意抢Dream/launcher或副屏。源码/JVM/受控Android doubles/API35编译不代表系统provider实际死亡链已修复。本轮609仍待实机，不放宽72项其它门禁，W60永久新增。详见项目PAD_HELPER_UPDATE_RECOVERY_INCIDENT_20261010.md。

## PAD-W61 workspace/build snapshot binding (2026-10-10)

2608 still reports host/unsupported_scope after the two owned plugin paths were fixed. The untruncated inventory includes private workspace source files and generated Builder APKs. Capture lacked physical-to-logical mapping; Dart restore and Native readback also lacked authenticated workspace-root binding. Do not delete these user files or admit arbitrary directories to obtain PASS.

Bind only authenticated v2 catalogue original UTF8 root hashes to the private default workspace root or explicitly registered descendants. Keep external catalogue references without reading their directories. Admit only generated host/builds/<taskId>.apk with taskId [A-Za-z0-9_-]{1,64}. Keep traversal/link/size/unknown binding/duplicate physical target rejection and publication conflict protection. Preserve old no-workspace snapshots, configuration, dedicated Key, sessions and operable main/Key entry.

Isolated old Dart and actual Native readback fail; the corrected seven new plus ten existing Dart cases pass, including actual helper codec and Native verification after Dart restore. Six actual Native fixture cases pass. Evidence: pad609-workspace-capture-restore/SEALED_RESULT.md, production-manifest.json, test-manifest.json, dart-native-restored-final.log, native-before-red.log and native-green.log. These are synthetic fixtures, not final-device PASS. Final full APK must include helper30 with host minimum30 and pass at least three actual complete-scope save/restore rounds while retaining original identity/Key/tools. Old helper29 and host608 cannot be claimed to restore the new scope. Matrix74 preserves all previous73 cases.

## PAD609：可选LAN发现失败阻断本机MCP目录（W62）

Android默认reusePort取!Platform.isWindows，故为true；现场报reusePort not supported。fallback工作区先await LAN discovery，再创建本机Bridge/Directory，可选发现失败即跳过必需目录初始化。旧真实Widget路径在模拟同一SocketException后本机bridge缺失，候选Android默认false、可选发现失败继续本机目录通过；其他平台及显式参数保留。LMCP exposure依赖发现，失败仍未就绪，不能伪running。

full仿真HTTP endpoint是独立启动链，只有3恢复工具与单条日志不足以证明唯一根因或Key丢失。最终同包需真实启动、原ID完整目录与工具/ADB至少三轮，保Key/会话。源码/widget与OS overlay不替代Android系统socket或最终全仿真。W62永久保留，原74项不变；详见PAD_OPTIONAL_LAN_MCP_STARTUP_INCIDENT_20261010.md。


## PAD609–610：首次凭据资格竞争与独立Key初读失败（W63）

609真实D0显示load_enabled读取失败；Main/relay及helper30活，手动原开关一次恢复完整工具与ADB且未清ID/Key。这不等于模型Key已通过：原session/ACP与42消息保留，但内层DEEPSEEK_API_KEY_REQUIRED，outer ok不能计模型成功。

native secure handler只核最低21，execute立即ensureHardwareScope要求30，旧helper29提前执行返回NATIVE_SECURE_STORE_UNVERIFIED。两处入口统一max(21,30)，仍用原installBundled singleflight及回调资格，失败/未知不执行，31不降级。原handler逐字抽取旧红，新原生产secure transaction/schema合成数据三轮等待30读回原bool/key；Android接口是受控替身，不是实机。

LEGACY Key的native资格本为30；独立widget首次失败仅缓存空controller，PlatformCredentialStore无sticky Future。新明确prompt/UI执行才对lookupFailed+空+未编辑做2秒singleflight重读原Key，不保存/清除/覆写凭据，不阻Key入口；再失败仍关闭，超时迟到、用户编辑、dispose保护。实际workspace与broker新六项加原Key保存控制七fixture绿，旧broker入口读一次红。证据pad610-native-secure-version-gate/key-widget-original-red.log、key-610-R62-combination.log、key-610-R62-combination-receipt.json及execution.json。七fixture不等于真实Key/模型成功，最终同签包冷覆盖与真实模型只读成功仍需实机证据；保所有原76门禁。


## PAD-W64：冷启动后传输配置副本不同步（2026-10-11）

2613 第二轮正常主 APK 重装的宿主 UID 只读比对，实证本地主配置与选项配置不同于受认证 helper 的当期字节，UUID 一致；暖重开后三者一致，完整快照第17代独立读回36文件和56条消息。冷启动每次 proof 快速返回本地比较失败，再耗尽预算；不能说是单次 RPC 卡死。四个身份文件不进入 V2 恢复 wire，不能指责旧快照覆盖新身份。具体 Native 变更字段未读取，名单正文未比对。

最终同签包至少三轮首次冷启动/正常重装，无人工重开、额外开关或重新输入Key即可完成注册、原会话/Key/授权及最新完整备份，并独立读回工作区与生成APK。真实注册/开启动作后的镜像同步沿用sameIdentity保护和精确字节读回；STATUS只读，未知写不重放，迟到/销毁/截止不能发布成功，并发合并。镜像完成通知只重验备份资格，不重做名单恢复、不放宽proof，桌面及nontrusted原行为保留。

项目固定矩阵新增W64后总77项，原76项逐项保留；旧回执须重新绑定矩阵SHA。当前614候选尚未实机验收，不标PASS。事故及证据边界见项目 `docs/acceptance/PAD612_REINSTALL_AND_READY_RECHECK_20261011.md`。


## PAD-W49 补充：616 提交后维护失败与 617 兼容验收（2026-10-11）

615 已观察自动续篇从 60 条到 5 条、同标题及真实模型找回旧构建结果；触发可来自字节阈值，不能表述为恰满 64 条。宿主/SDK 上下文压缩不证明 helper 加密 generations、chunks、completed uploads 或 exports 长期有界。

616 真机自动备份在 upload 返回 snapshot_retention_deadline；已封存 v1 回收计划后，在同一维护预算中立即续作并再次认证 current/previous，耗尽协作式截止。后续独立 Native 读回 generation 32、45 文件、585447 wire 字节、10 workspace/2 build/18 SDK，vaultReadbackComplete 与 liveMatchesSnapshot 均为 true。因此是提交已落盘后维护失败、ACK 未确认，不能宣称未提交或数据丢失，也不能重放未知结果写入。Native 回执未给消息数，不能附会早期 context 消息计数。

617 候选仅改维护闭包：兼容原 v1 journal；current 与 previous 共两完整认证代，保原 AEAD/逐字节 SHA 与锁保护；收集及续作分阶段有独立维护预算和边界检查，不扩大旧通用/Key/RPC 预算。每次发布须保旧红、新绿及最终同包实测：旧版封存计划续作、中途退出/部分删除、当前与回退完整字节不变、读取与提交并发、active upload、unknown、link、损坏计划/认证失败均安全保留或拒绝。未完成上传无退出证据不得凭年龄删除；STATUS 不写文件、不做 GC。必须对账维护前后代际/文件/字节及最新完整独立读回，再认定有界目标；历史迁移未完成不标 PASS。

受控 32MiB/768MiB 测试堆通过不等于所有 Android 大快照通过；512MiB 的 memory_budget 拒绝仍保留。单阶段认证大量旧 payload 仍可能安全截止，锁/Keystore 等待仍属协作式边界；不得拿预算放宽或只剩前端摘要冒称 W49/100 轮完成。617 签名与包闭包/DEX 已核，尚无本条记录对应实机覆盖/GC PASS。77 项原 case 与最终同 SHA 证据要求不变。

组件验收须另保真实首失败：616 缺 Builder 8 时安装仅提交一次，operationId 从 checking_market 到 installed_verified，并独立核 PM 版本和 APK SHA；首次冷 runtime 约 84 秒含解包/自检，不能只用安装完成替代 buildReady。原 Key/原会话的首个编译调用 aborted 且无 taskId；查询旧任务 not_found 不能推断新任务未提交。第二个有明确 accepted taskId 的任务才以独立状态和产物包名/8595 字节/SHA 验证完成。未安装产物、未触副屏/GPU不计这些功能 PASS。原始聊天、Key、wire 和私有日志不上传，公开记录仅固定结果与证据 SHA。


### W49 第二次现场失败：617 收集阶段重复全扫（2026-10-11）

617/helper33 实际覆盖后，原 Key 与会话真实模型两工具完成，当前 15 条消息；独立 Native 读回已认证 generation35、46 文件、724937 wire 字节（10 workspace/3 build/18 SDK），vaultReadbackComplete=true，但 liveMatchesSnapshot=false。最新数据尚未完整备份，不是证明数据丢失。helper 实际在 BEGIN 的 collect/export metadata/exactFiles 路径报 snapshot_retention_deadline，区别于 616 的已封计划后嵌套续作失败；旧 v1 journal 已真实续作，不能把这次失败归为旧 journal 从未兼容。

W49 必须增加同一 case 下的持久收集进度控制：历史多代及 completed/export 元数据使旧版每次从头扫描耗尽预算；候选需在原 5 秒单元/30 秒 RPC 约束内认证并持久推进，只有完整封存计划才有删除权。测试中断、next 写入未 rename、已封 plan 未清 checkpoint、篡改、当前代/树变化、活动上传真实变化、未知/partial/link，以及失败 BEGIN 不新增 upload/重复 generation。过期的已认证派生 checkpoint 可撤销并本次拒绝，后续明确请求重新资格检查；不能删除未知业务数据或重放未知提交。

618 单 Transfer 候选已有旧红/新推进绿、旧 v1 兼容、原安全控制及 API35 资格；5f75ecafe88f2a8f7a30a2301d3c54d598303e2978b534a24d2ab55cf4f928a1 是该候选补丁 SHA，不是 APK 或实机 PASS。初末 stat census、单目录认证仍有协作截止限制，不宣称任意慢设备、长期容量或全部 W49 完成。不得把后续构建完成冒充已封最终包、已合主线运行代码或设备结果。77 项矩阵不改。


## MAC618：重复封包及源码排除错误（2026-10-11）

首次源码复制用了未锚定 build/ 排除，误删 human-signals 等依赖内部 build 目录，构建完整性检查失败 exit65。只排除 /build/ 等根构建目录，依赖目录必须完整保留；修正后双架构构建通过。

公证后最终ZIP又错误沿用 --sequesterRsrc，update_stage返回staged但原617接收端apply拒绝根外条目，原App未停止、未替换。578/605文档及严格archive检查器已存在，这次是执行未复用既定流程，不能归咎于新服务端。重封同一已签名/装订APP为 --norsrc 包；严格检查旧错误包失败、新包invalidEntries=0；独立解压的三项检查真实exit0后才暂存应用。2617→2618实际事务COMMITTED/PASS，设备ID保持1554650784，运行桥及安装版本均2618。只证明此次本机覆盖，不是完整H01–H06/六机/发布PASS。

证据：项目docs/acceptance/HARNESS618_BIND_DIAGNOSTICS_20261011.md及外盘native-bind-diagnostics-618-20261011-v1/evidence的archive-negative-v1.json、archive-v2.json、extracted-checks-v2.json、local-transactions.json。私有token回执不入Git。每次暂存前强制严格archive检查，公证ZIP与更新ZIP分别生成、记录SHA，不允许为通过放宽旧接收端合同。


## PAD-W54：公共框架依赖缺失与合同升级（2026-10-12）

Builder8实际编译AOSP HelloActivity通过resources后，javac报XmlPullParser缺失；不能修改样例绕过inflate或用假平台类冒充完整接口。Builder9/10真实ROM转换在原120秒截止失败，旧失败保留。Builder11复用设备API对应官方公共android.jar（31–36），原始SHA和内部NOTICE保留，jar仅编译classpath，不进入生成APK；其他SDK旧转换路线未验证。正式分发需逐组件来源和NOTICE闭包，不能笼统宣称整个SDK允许重分发。

W54仍原case，77项不缩减：精确7/8/11及各自精确toolchainSHA，未知9/10/12和错误SHA拒绝；旧7/8全部字段兼容，Desktop不添加PAD合同。支持仍Java8/app-src-main/Manifest/res，无任意Gradle/Kotlin/JNI/依赖解析或完整desugar。未知事务查原operation/task，不重复构建。Main624合同实机source_verified/buildReadytrue；实际AOSP编译、PAD自写Receiver编译/安装/调用回执与MODEL/API独立对照通过，仅这些受控任务。Builder11按需商城组件未内嵌Main，新机商城和全77项仍未通过。

覆盖前完整读回曾gen80 live不匹配，差异精准映射工具活动审计195896→196808B；工具查询会追加且已纳入排它，不能仅凭该差异断言丢失/漏锁，也不能排除该文件放宽验证。原失败保存，任务对账后gen81、覆盖后gen82全字节liveMATCH。快照与当前数据不同须定位并取得新完整保护，不能反复重装掩盖。


## PAD-W61：共享恢复集成遗漏与成功清理负控（2026-10-12）

本轮当前共享源码再次发现：Dart恢复workspace直接拒绝，host/builds走通用host路径被写到Harness/builds；NativeVerifier只核验已发布数据，不能补复制。helper wire/完整live备份通过不代表Dart恢复通过。沿已验证正式624最小集成认证catalog原路径hash→私有root映射，并贯穿捕获、stage、publish、final readback和confirmed reconcile；保peer同源与unknown回执保护。

独立实际文件I/O负控RUN/workspace-success-cleanup-independent-red/RED_RECEIPT.json证明：ack回调晚到stage文件，在restored=true后被旧success finally递归删除。成功清理同样必须逐项核owned字节且非递归，未知/新内容保留；清理失败不回滚已经确认的live数据。永久回归增加到既有W61证据范围，不删原77case、不伪造正式包通过；必须保正常清理、lateunknown保护、unknownack原代续作及完整workspace/build/spill字节恢复。修复绿、共享应用和最终包实机仍需独立证明。


### PAD scoped instrumentation package visibility (62528, 2026-10-12)

Original self-target probe lacked explicit Main package queries under targetSDK31; getPackageInfo produced NameNotFound/SecurityException although actual Main2625/C8 was installed. The approval observer repeated this probe failure; the original build aborted with no new native operation. Preserve this as test-instrument failure, not host crash or registration defect. Fixed62529 explicitly queries only Main, returns bounded guard-error metadata, strictly rejects trailing JSON and stops observer immediately on instrumentation error. Before release/device approvals, prove actual installed identity and probe visibility independently, retain scope negatives and original operation reconciliation. No broad visibility permission, identity-check removal, blind clicks or unknown task redispatch. This supplements existing instrumentation/Builder cases; no matrix PASS or new case-count claim.


### W43: stable-state notifications and 625 physical CPU FAIL (2026-10-12)

625 original310.376s/62interval idle window measured single-core median6.3941% above5%; retain FAIL in device63-idle625/strict-gate-receipt.json. Constant resumed-activity metadata does not prove uninterrupted visible Main window; later ownAX saw Dream, not proof of the whole window. Thread names/tick deltas do not prove unique cause.

Actual TargetRuntime emitted identical normalized target and consent values on every real poll, rebuilding subscribed widgets without state changes. Minimal shared fix compares all12target fields plus captured globalenabled; consent compares revision and all7immutable request fields/order, preserving first event/removal/sameRIDkey/deadline changes. Native network/ADB/consent polling frequency unchanged. Old actual refreshReadiness negative control failed; current-source permanent runner and frozen626 runner each passed37 cases. Run tool/target_runtime_idle_test/run.py with exact reviewed source SHA and a fresh owned output, keeping private test forwarders outside shipping source/default test discovery. These controls do not close physical CPU gate: final signed artifact still needs the original full idle measurement and lifecycle/readiness/authorization regressions before publication. Do not weaken threshold, suppress real connection checks, claim unique cause or erase old failures.

### PAD628: live simulation state and ADB recovery disagree

New device2315315560 had live simulator enabled/ready=true, but adb.ensure repeatedly returned simulation_not_enabled. Main read MODE_PRIVATE preferences while the separate relay process wrote them. Read the live simulator gate through the existing CONNECTIONS IPC instead of treating a Main-process cached preference as authority. Actual STATUS carries JSON without an outer ok=true, but does not supply the gate used by this repair:629 passed16 synthetic-payload controls yet actual recovery returned simulation_state_unknown. Preserve both the incorrect outer-field candidate and this real wire-source failure. Verify Main→Client→CONNECTIONS→native harnessConnections, not just a supplied JSON fixture. The dedicated reader must not bind/queue/start a missing relay; unknown/off/identity-initializing states, timeout, late and duplicate replies fail closed. Keep helper signature, snapshot and RSA boundaries. The initial RSA failure is not proved to have this sole cause.

Before release execute tool/pad_adb_relay_status_test/run.py against the actual source with a new qualified output. Preserve fixed original and wrong-shape RED and the current strict known/source controls. Also run tool/pad_adb_relay_wire_test/run.py:630 actual ensure still returned unknown; the installed C6 connection shape is an array, not the assumed object with an enabled field. The corrected PAD adapter projects only a same-process successful native setter ACK through existing private read-only IPC, with explicit known/source/Boolean. Initial, failed setter, destroyed and uninitialized states remain unknown; never substitute preferences or mirror-file verification for this ACK. Preserve real629/630 failures, old-runner failures, actual-method wire and lifecycle negatives. Android substitutes and mocked setter ACKs are not real C6/Binder proof. Final same-signer APK must additionally prove live status/recovery consistency and actual simulation ADB, including normal-off and bounded failure behavior. New-device first resources task completed167.408223s and the second17.735414s; H5 auto-installed before execution, so a pre-preparation missing-component observation is not final installation failure. Keep the original77 gates and separate factory-baseline, market-component, cold-start and data-protection evidence. Project incident: docs/acceptance/PAD628_NEW_DEVICE_ADB_STATE_INCIDENT_20261012.md. A built candidate is not a deployed fix or publication PASS.

### W64: first-save registration metadata publication gap (2026-10-13)

Actual new PAD2315315560/Main2628: same-signer read-only metadata probe verified trusted helper registration48B for the actual ID, but Host file absent; Main/relay PIDs preserved before and after. Startup prepare runs before first identity save; first save creates helper registration but did not publish Host metadata afterward. Strict transport proof correctly rejects absence. This explains this device transport_proof qualification gap, not every server/authentication failure.

Existing W64 must test initially absent helper registration -> first save -> Host publication -> strict proof, equal existing Host unchanged, conflicting Host rejected, concurrent publication, expired owner, helper death/null/unknown replies, unconfirmed writes and restart reconciliation. Publish only existing trusted helper bytes; never regenerate UUID, replay unknown writes, mutate STATUS or clear Key. Keep server/SDK/Core unchanged. At least three lifecycle/concurrency rounds plus final same-signer APK new-device/old-overlay/data continuity evidence remain required. JVM atomic-write PASS does not prove Android/f2fs behavior: actual publication and independent complete backup readback are required. Candidate not yet deployed on new PAD; fixed77 unchanged, no release PASS. Project incident: PAD628_NEW_DEVICE_ADB_STATE_INCIDENT_20261012.md; actual receipt REGISTRATION_METADATA_LIVE_RECEIPT_20261013.json.


### UI-STOPWATCH-01: controls below the usable viewport (2026-10-13)

User reported the developer-tools stopwatch Start/Lap/Reset row too low and obscured at the bottom. Existing fixed250 dial plus gaps/digital text placed the controls outside a short viewport. Actual old633 widget negative:320x320, bottom safe inset48, button bottom534 exceeds usable272. Preserve this failure; do not call a scrolled or offscreen button visible.

Current shared fix keeps digital time/actions in the upper fixed group, scrolls only lap records, shrinks/hides the optional analog dial according to available height, and keeps a bottom safe margin. Run existing test/stopwatch_workspace_test.dart including short viewport/bottom inset and20 laps; controls must remain inside usable bounds with no overflow and unchanged position while laps scroll. Existing stopwatch formatting/start/pause/lap/reset assertions stay. Isolated real Flutter4 PASS, old implementation RED, format/analyze PASS bind sourcef766793394410758c1d2ddd597002ae92b303cda279d9fde8a3c91f0be9b0704 and testb6f2b225710ab2e76c313ba603901395b8bbb80546292abc8348cea1cf490253; RUN/stopwatch-layout634/FINAL.json. This is a source/widget qualification, not physical PAD deployment or whole77 PASS. Verify final same-signed APK navigation/control visibility on authorized D0 without GPU capture on known-unsafe firmware. Keep fixed77 cases and extend the existing UI evidence; do not drop other cases or invent a passed release.


Latest user refinement: the stopwatch main page must not scroll. The intermediate independent-lap scrolling implementation above is historical and is superseded. Final UI qualification must assert zero main-page Scrollable, complete digital glyph bottom padding, stable visible controls/precision, adaptive remaining-space dial, bounded recent laps and a separate all-records dialog. Current no-scroll6 tests cover320x320,640x280,720x800 with bottom inset48 and20laps each; the previous scrolling implementation fails the new assertions. Bind widgetf6fcd6dcba21b96afdbdb76bb0edfc57b4cc4a070209b2d0b13ae42cf636fa89/test1a1cba72f0099224762f89d715619e02f21bb583e635c8f6fafd42f8aac28cb1 and RUN/stopwatch-no-scroll634/FINAL.json. Source test PASS is not physical deployment or release PASS.


### PAD W49：第二次压缩后的最近用户记忆错误（2026-10-14）

实测635自有单会话100轮验收：61轮完成，第62轮在第二次自然rollover后真实工具调用成功，但返回了第60轮的编号和标记，未返回最近已完成第61轮。原任务终态和失败证据保留；这不是第二轮已修正的fan字段别名observer误差。首次rollover记忆/标题/cleanup通过及同PID内存下降，均不能替代后续长稳通过。当前根因未证，须区分输入/持久化/SDK绑定中缺失最近用户信息，和模型误取先前助手答复。

复验沿固定W49，不新增或删除矩阵case：在同一逻辑会话完成真实100轮，跨每次自然rollover逐轮核最近用户输入的编号及独立标识、同标题、新旧SID谱系、真实工具调用和最终清理。不得把期望标识重新塞进新任务伪造记忆，不能重发失败任务后覆盖首失败；修复后记录新请求独立复验。前文summary/tail存在不证明真实请求已发送这些内容；当前official ACP绑定不证明失败请求前绑定。

后台状态须按当前清理事务判断：上一轮backendCleanupComplete=true不能证明当前quarantine完成；压缩Future、persist和cleanup gate需退出后才继续。物理SDK目录统计和helper vault分别验收，前端消息下降或单次census数值不代表长期磁盘有界。新metadata reader只返回限定QA目标的角色/字节/匹配布尔值，不输出正文、Key或其他客户会话。


### PAD：受保护 Main＋H5 重装与 PM absence observer（2026-10-14）

63728在fresh gen127完整保护后实际卸载Main成功，但 observer 用check_output读取pm path，把合法empty/exit1当异常；产品数据恢复不能因此归类失败，也不能重发卸载。原Success/PM absence对账后72767只继续未发生的H5卸载及同签636安装。复用真实subprocess解析：exit0或1且stdout为空、stderr为空才接受absence；exit0的package:列表表示present；offline/transport stderr、未知退出和异常stdout必须UNKNOWN并禁止重放。9控制含旧check_output对合法absence RED，永久入口tool/pad_pm_path_observer.py与tool/test_pad_pm_path_observer.py（运行python3 tool/test_pad_pm_path_observer.py）；原RUN/device63-main-h5-reinstall636保留首失败及实际回执。

删除前明确仅Main＋H5、保helper保险库/Builder及其独立JKS：上传大包后必须立即再次strict已知quiet与native execution退出核验，不用上传前旧状态；绑定Main/helper/H5最终包hash，fresh独立wire/live/frontend/workspace/build/spill与Key槽保护证明后直接下一步，禁止先warm旧Main触发新save。原spill内容SHA与Builder UID/version/baseSHA实际相同；Main/H5 PM absent真实且no-k，helper不卸不清工厂。H5为确切asset-only合同，不能声称未跨UID读的H5私有目录物理为空。

普通新Main UID动态，H5必须由真实启动自动准备；不ADB补H5、不先发模型促prepare掩盖首启动缺项。确认原会话/聊天/工作区/build/spill/名单及配置实际恢复后，唯一固定RID旧Key模型任务证明Main能用原Key，不把helper槽presence当Main解密/模型可用。636本轮原SID任务8records资源成功、H5先自动准备、原ID真实MCP/ADB恢复，但不等于新系统R11或全77发布。

原gen127严格byteVerifier恢复后liveFAIL保留：限定原wire/manifest的全118诊断证明117一致，唯一names385B目标摘要改变，2records的ID+key映射/姓名hash/顺序全部保持。新target匹配实际当前ledger；无时间字段，不是仅排序。helper.previousTargetDigest独立绑定仍UNKNOWN，不能以文件名像cache、新snapshot saved或原MAC ID相同冒称pubkey身份延续/全恢复PASS。生产Verifier不弱化、不删除原失败；每个允许的派生变化须有具体语义与安全绑定证据，正文/workspace/build/spill损失必须修复，不归类格式差异。固定77/G1–G5/PAD-D01–D19不减。


### PAD W49/W64：后台 SDK 子进程 CPU 超限连带杀宿主（2639，2026-10-14）

63 的2639真实100轮原序列完成53轮，第54轮已accepted，查询返回remote_harness_not_ready。独立ADB确认Main消失、整机uptime未重启、包仍2639/UID10133。Android ApplicationExitInfo reason9/subreason7；AMS明确PhantomProcess PID16847（runtime5 node经ld-linux）CPU9240ms/300002ms、limit2，连带杀父Main27469/adj700。该PID在杀前约26秒才exec；日志dur3160018不是子进程寿命。不能把这次故障归为OOM、编译器异常或仅网络断联，也不能据此断言长期空闲泄漏。

原51207终态失败，53轮、两次实际转代及所有原回执保留；第54轮不重发。一次普通启动只带前台任务的warning不证明进程已启动；自有D0 AX确认Dream后一次BACK恢复Main19096及原ID。恢复后原QA标题/已知谱系/historyLoaded保持，但原status/history返回HARNESS_SESSION_NOT_FOUND；第54轮结果仍未知，不能用前端44消息或原SDK文件存在充当请求完成。证据RUN/sdk-retirement639-live-plan/actual-100-639-after-backup139/R054_OS_CPU_KILL_PUBLIC_INCIDENT.json及私有exit/events/ams日志。

固定77项中补W49/W64生命周期回归，不新增计数：最终包必须在真实后台/Dream条件下执行SDK准备、模型任务、工具及后续自然压缩，核子进程/宿主仍活、原RID结果、最近记忆和物理存储。若使用任务重要性租约，必须是真实模型任务用途、在SDK准备/启动前实际OS确认并保持至子进程真实退出；失败不得先启动子进程或假称已前台。开机/空闲不得借模型任务制造通知，不能冒用backup服务标签与权限，不能关闭Phantom CPU约束、改系统性能策略、伪造前台或修改官方SDK来掩盖。实际启动权限/拒绝、并发、已知spawn失败、未知退出和真实终态释放均须测试；受控fixture不替代最终同签实机。

当前修复仅在自有运行时隔离候选设计/实施中；未构建交付、不标全100或发布PASS。


### W49：观察器公开字段与控制桥中断续作（2640，2026-10-14）

原100序列第7轮额外调用内置describe_tool，原提示不遵守记录必须保留；精确生产路由及源码证明其只读取公开定义，不执行目标业务后，W49业务/记忆结果可分别核验，不能伪称完全遵守提示。其他业务操作及第二次业务调用仍拒绝。

第20、31轮已完成时控制端工具桥换进程/端口，状态或历史读取出现reset/EOF。观察器停止不证明PAD或原任务停止；通过原ID正常重连，只读取原ACK绑定的status/history，核完整原user SHA、序号、真实工具与事实/最近记忆后继续下一轮。只读原调用最多一次恢复；写请求未知不重发、不重启其他任务的App。每段续作保留所有首次失败、原179198KB基线与完整旧转代事件，新增RESUME前缀输出，不覆写旧证据。

第38轮风扇接口原生公开字段为debug、observedPwm、rpm、temperatureCelsius；观察器遗漏observedPwm→report、temperatureCelsius→temperatureC而误拒。发布验收须与精确本包公开字段契约对齐，保旧mapper真实RED及新GREEN；同值合并、冲突值与无关额外字段拒绝，不改产品或重发已完成任务掩盖误差。原debugPwm/reportPwm旧别名及current number/marker严格配对验证保留。

上述不增加或删减77项，也不授予100轮、物理SDK目录退休、helper存储、新机商城或正式发布PASS。证据RUN/sdk-retirement640-live-plan及r007/r020/r031/r038-resume-candidate。


### W43：请求场景与实际屏保状态不一致的无效对照（2644，2026-10-14）

2644严格五分钟进程族CPU中位8.236235%，61条、300.229988秒、读取错误0，5%门槛失败；Main约3.20109%、native进程约5.07355%、helper0。签名/覆盖/原Key/完整字节通过不替代此失败，结果公开归档main0b148684add088319f19bb50f05b547fee69a4f1。

随后两个同PID60秒原窗口各有host/consent/ADB60次、失败0。请求的第一段“前台”实际为Dreaming且Main未聚焦，第二段不是Dreaming，不能称有效前后台因果对照，也不能从相近CPU数值排除渲染或证明native唯一根因。保留两个原测量与设施误差；主屏正常恢复后自身AX66节点、foreign0确认。证据RUN/performance644-home-comparison/ROOT_COMPARISON_PUBLIC.json及RESTORE_PUBLIC.json。

后续对照必须分别核实际场景/电源、PID/startticks、当前包SHA、空闲owner及查询次数；请求标签和操作命令不是实际场景证明。唤醒后的自动备份等待可能再次进入屏保，必须以采样期真实状态决定比较是否成立。失效对照不重分类PASS，不关闭服务/授权检查、弱化CPU门槛或修改OS性能策略来取得低数值。本补充保留固定77项，不新增case。


### 工作流：跨版本脚本遗留 requestId（650，执行前拦截）

650完整包之后，安装执行器虽通过AST与审批关闭测试，仍残留649的模型requestId、跨脚本读写文件名及结果版本。复用旧requestId可能读到旧任务，不能算新包验证；本次在任何设备动作前拦截，保留原准备字节，未造成设备安装/任务重放。永久矩阵仍77项，不把执行器设施错误说成APK故障。

复用执行器须同时核对生产者/消费者的事务、备份与模型结果文件名，旧包仅在覆盖前版本断言允许；安装后版本、探针版本和新requestId必须绑定本轮。执行真实契约负控：原遗留脚本必须失败，修后必须通过；再注入旧requestId、旧结果版本和断开的读写引用，均须拒绝。AST、字符串替换完成、审批关闭或文件存在不能代替该语义检查。最终绑定APK哈希后再核一次；保留未知写不重放和同签数据保护。

### W15/W54：正式包完整不等于已解压运行目录完整（2655审计）

2655生产源码的既有root复用分支只核版本摘要标记、manifest及node/node-real；正式manifest声明的CLI缺失或同长内容损坏时仍可返回ready。使用正式H5 manifest和真实文件的隔离负控已复现；普通Runner之后的存在检查只能报错，不能自动修复。此证据不证明设备文件被谁删除，也不证明APK漏包。完整验证器用于快照，不代表普通模型启动已经调用它。

每次涉及运行组件准备/复用的发布，分别证明：正式APK内组件闭包与签名、冷解包、已有目录完整性、故障后恢复。沿生产启动入口验证必需文件缺失、同长损坏、并发准备、取消/重入、原事务失败后再次缺文件；不能仅直接测试修复helper。保留旧实现负控。真实任务必须在最终包上通过，STATUS不得启动修复，失败终止忙状态且Key入口可操作。

恢复仅处理经过正式组件身份和摘要认证的可再生运行文件，保护活跃reader、Key、会话与未知文件；不得用全root删除/替换掩盖缺陷。持久事务必须对账原结果，不能因残留标记永久阻塞后续恢复，也不能盲重放未知写。单独记录正常快路径与修复路径的设备耗时/内存；本机JVM全量校验约37秒不是PAD性能PASS。

保留既有dev418兼容：正式node/node-real缺执行位原本能恢复，新校验不得退化为永久拒绝。先认证当前组件及目标完整字节/NOFOLLOW资格，再恢复正式成员执行位并读回；未认证字节或未知文件不可借此改权限。

2656候选新增联合回归：成功补文件后，修复事务/锁/历史/stage位于`files/harness-runtime`父级会被实际快照扫描拒为`host/runtime_extra_uncovered`；原生产capture基线通过、加入这些siblings后失败已复现（RUN/runtime657-control-location-candidate/CAPTURE_OLD_RED.log），未在设备执行故障注入。修复成功必须继续验证完整自动快照和独立读回，不能只验证模型能启动。非用户数据的控制记录须使用经OS Context核验的适当位置，验证清缓存、冷重启和未知writer，不为放行修复产物而泛排除未知文件，也不把用户日志/输出迁回易失缓存。

证据定位：RUN/runtime655-h5-reuse-audit、runtime655-missing-only-candidate。后者仅隔离候选，正式H5 55074文件校验及补齐通过不代表生产已接入、设备已修或可发布。沿用固定77项，不增加/删除case或授予PASS。


### PAD测试设施：系统AndroidID与应用SSAID不可混比（65701）

65701受控缺文件探针在构造fixture之前，以Main上下文Settings.Secure.ANDROID_ID摘要比较shell/global摘要，触发physical_device拒绝；实际未移动/删除SDK文件、未执行模型。此为探针身份范围错误，不是Main缺文件或修复失败，也不得记为恢复通过。保留原INSTRUMENTATION_CODE=2和原事务，不重放mutation。

此类host-target故障注入须分别绑定：外层shell物理设备定位、最终Main整包SHA/包名/UID/签名，以及同应用上下文的SSAID。先执行不构造fixture、不写文件的只读qualification取得同scope摘要，再将它冻结到新版本探针；不得移除身份守卫或用系统摘要冒充应用摘要。核对实际事务终态后恢复主程序正常运行，不让测试设施失败留下长时间停机。原77项保持。

65703演练执行器审查另发现：原guard要求实际探针从未返回的`phase`字段，会在真实hold成功后误报失败。已在设备动作前修正，原guard对实际字段形状的RED及新正负控保留。读取固定探针结果时，先核实际源码和最终DEX的输出合同；动作阶段来自持久原argv、同transaction及原进程终态/远端CODE，不向raw metadata补造字段。不同阶段分别核真实state、身份、安全字段和文件计数，未知返回码不得认成功。证据：RUN/prehold657-fresh-protection-prepared/guards-FIRST-PHASE-CONTRACT-ERROR.py与ACTUAL_CONTRACT_CONTROLS。

安装回执沿本轮原始事务查找，不假设每轮都有分离的public与PM文件。65701实际使用同一combined journal；只有精确包SHA/版本资格、terminal、一次PM成功、远端及实装SHA、Main未重启等原事实齐全时才适配其形状，不伪造缺失version或returncode。原事务缺失/未知仍拒绝，适配须保留原字节SHA及负控。
