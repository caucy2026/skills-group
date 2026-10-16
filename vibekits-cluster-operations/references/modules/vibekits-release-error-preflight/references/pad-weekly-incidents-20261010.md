# PAD 整周异常与永久发布验收基线

覆盖最近七天 **2026-10-04—10**。日历周从10/05开始，这里多保留10/04以免遗漏。本基线永久保留，不随日期滚动删除。

当前共 **76个固定case：63项异常/风险、13项需求**。63项中，C51为已证实产品或实现缺陷（含未上线候选缺陷与继承历史门禁），U6为用户报告/现场异常但唯一根因未证，T6为测试、观测或执行设施问题。**这不是63次故障，也不是51项均已修复的现场事故。**复发总次数未知，不用日志行数、测试循环数或版本数代替。一个问题跨版本只计一类。

当前2607fixed作为测试更新接受验收，W58/W59仍未闭合，不代表72项正式发布验收通过。所有适用永久门禁必须绑定同一最终签名包PASS；旧包局部通过、源码正负控、一次saved、独立probe或已有白名单设备都不能替代新机首次授权及全生命周期验收。

## 异常与风险：63项

|caseID|类|版本/事实|根因及证据边界|彻底解决措施与永久验收|当前状态/证据|
|---|---|---|---|---|---|
|PAD-W01-version|C|522：源码常量/包版本不一致|版本门禁事故已记录，不能凭文件名判版本|构建前源码/生成配置/argv一致，签后实际Manifest版本；保坏包负控|查 PAD522_VERSION_GATE_INCIDENT_2026-10-05.md；每个最终包重验|
|PAD-W02-package|C|既有漏运行依赖、FFmpeg/JNI、helper低于宿主门槛；本周必须防复发|旧427/458事故早于本周，不计本周新增次数；开发机预装掩盖新机风险|最终APK逐组件版本/同签名/内容hash/资源/真实入口；新机自动准备与功能，不靠侧载|579、601、602包完整性局部PASS；不替代首次注册|
|PAD-W03-key-gcm|C|570：保险库empty slots、mirror not_started|Keystore要求随机IV却传调用者IV，已证|Cipher生成IV，保alias/AAD/版本；真实保存读回与错误负控|571起修复；后续slot可用，但完整重装矩阵不能据此关闭|
|PAD-W04-key-replacement|C|保存新Key后官方SDK仍用旧Key，迟到镜像风险|legacy/official双源及提交顺序问题；不能以某一slot存在替代resolve|两个保存入口、正式SDK resolve、新值持久读回、CAS/晚读防覆盖；普通卸载后仍最新|凭据修复已集成；整周最终包完整重装仍未验完|
|PAD-W05-identity-policy|C|513起另一型号信任判断/固定MAC身份与型号变更问题|MODEL/MANUFACTURER精确名单不足；数字ID、pair、注册UUID不等价|按真实签名/能力和稳定硬件scope，升级不改ID/key，清组件不动核心身份，ID变化隔离旧绑定|PAD_REQUIREMENTS D05/D07/D10；全部型号矩阵待验|
|PAD-W06-uuid-rejection|C|582：同数字ID注册uuid mismatch|服务器207条拒绝是日志数量非失败次数；同硬件新pair不同认证UUID已证|保覆盖pair；真实卸载依最新约定删除旧传输pair后重新认证，保同硬件Key/聊天；禁止服务器放宽|10/09后续588稳定公开UUID与轮换pair分离，589/590真实原ID连接和工具PASS；跨网同时换PK与普通卸载全矩阵仍未完；PAD_CHANGELOG_20261005_09.md|
|PAD-W07-apk-exec|C|582：恢复链Process.start(APK)报Permission denied|Android掉入桌面takeover已证，原生离线原因另案|Android服务/JNI恢复；所有入口禁止APK/桌面stop执行；原默认指纹路径测试|修复已集成；必须断线重新进入实测|
|PAD-W08-status-revive|C|585：停止后2秒STATUS查询仍重启认证|BIND_AUTO_CREATE复活relay，外层有限retry不足，已证|STATUS不创建PID；截止后3次轮询/重入不复活；显式用户重试才新事务|PAD585_STARTUP_RECOVERABILITY；旧585 FAIL保留|
|PAD-W09-passive-path|C|586：暂停手动开报File.openRead android://|被动payload漏executable，fixture替换指纹漏检，已证|各idle/paused/failed/live返回当前PM真实路径，生产默认指纹和启动组合回归|pad-identity-startup表；不得用mock-only通过|
|PAD-W10-startup-shell|C|启动恢复/认证检查阻塞主界面与Key入口|UI入口和数据首次访问次序不满足要求|runApp前数据屏障、shell/Key独立；恢复在仓库首次读写前；失败显式重试，不假空历史|startup594已集成；全新、partial、无备份/离线最终包矩阵待完整复验|
|PAD-W11-online-state|C|无网络/只注册却显示在线或一直开启|缓存/开关/真实在线语义混淆|online/reachable/offline/unknown区分；真实断网恢复；一个动作一个忙态|579弹窗局部实证；物理断网全矩阵未闭环|
|PAD-W12-uninstall-pair|C|旧host/helper/legacy副本或失败标记导致卸载后身份复活/持续暂停|清理范围和scope顺序不一致；与数字ID算法分开|只清精确旧pair/失败绑定，旧进程真实退出；同ID保最新Key，ID变化清旧绑定；不清无关聊天|585部分实际清理/slot相同；不能冒称普通卸载恢复全PASS|
|PAD-W13-consent-retirement|C|旧removed删唯一consent；旧target ledger不能直接重绑|仅V2显示名不是名单；FFI撤销成功/helper失败有旧Allow复活风险|同硬件退休controller决策，真实新target重绑；精确intent/CAS，unknown只关闭受影响Allow；allow/deny/revoke/陌生公钥逐测|601候选已集成helper25；普通卸载名单全过程仍待验|
|PAD-W14-runtime-budget|C|578—582全目录12秒持续超时|55074文件971MB实际58.009秒；尾部小读/重复分配有证据，单项优化未达12秒|全字节等价批量读取/局部缓冲；明确idle90秒新契约、用户20秒准入，不能改称旧门槛PASS|PAD580_RUNTIME_RECHECK、PAD_IDLE_RUNTIME_VALIDATION_CONTRACT|
|PAD-W15-activity-scope|C|592 snapshot legacy_home_not_covered|activity HOME落code_cache，真实写queue未纳cut，已证|持久files迁移，保原字节archive+receipt；全异步写/替换/清理纳准入；未知legacy拒绝|store已集成，旧592首败保留|
|PAD-W16-reputation-scope|C|594：reputation/log/temp/空目录导致scope不完整|metadata确认真实producer路径，不能整目录跳过|信誉持久迁移+receipt；固定可再生路径按代码分类；附件/未知/link拒绝，空目录不假数据|device594 continuity-probe；595精准映射已集成|
|PAD-W17-root-alias|C|596：reputation_migration阻断；UI reputation_live_parent|app私有根路径alias与严格父检查不兼容，实机同码红控|只规范可信private root；业务子目录/文件link仍拒；Android形态回归|597首代saved；device596 reputation-ui/error.xml|
|PAD-W18-task-cut|C|593：任务接受后2ms host_snapshot_cut_pending|前置保存先于agent预抢占预约，已证|同requestId先登记、保存与SDK共预约、真实退出后开始；无重复任务；未知不强解|598三轮真实cut任务完成、18消息保留；固定入口回归|
|PAD-W19-store-read-notify|C|594开发候选：读→changes→模拟监听回读循环|仅隔离模拟订阅检出，未发现生产订阅，不能称已部署UI事故|读不emit、真写按原语义；有界红控/正控|未上线缺陷已修，保12项原测试|
|PAD-W20-admission-wait|C|594开发候选：cut拒活动被吞、多个waiter活锁|同步拒绝与互相requestAdmission唤醒，真实并发fixture证明|一次需求取消、仅真实release唤醒；原操作单次提交，3waiter/SDK-held/超时/嵌套drain|runtime/store已集成；不取消20秒边界|
|PAD-W21-stage-cleanup|C|594开发候选：清理删一项中断，下次要求全部存在永久拒|幂等边界代码已证；不是实机数据丢失报告|同源ledger已缺expected允许，余项核hash；未知/变化/link/newer保留，空stage末步亦补测|恢复器最小补丁已集成|
|PAD-W22-observer-write|C|597：context_status读完又写audit取消备份|真实bridge/store/scheduler红控已证，非W19|固定诊断纯读保授权，无producer/epoch变化；真正saved及失败handler回归|598集成；连续saving不能倒推同flight卡死|
|PAD-W23-wait-transport|C|598：session_wait15/30秒被8秒transport先超时|等待预算大于真实tools/call已证，任务本身继续|Android目录/handler默认最大5秒；真实传输回包，不重发原任务|599真实默认6.792秒回包；固定负控|
|PAD-W24-diagnostic-loss|C|598：失败reason丢失，saving难区分阶段|scheduler投影丢类别已证|固定reason/phase/attempt白名单，release不盖失败阶段，敏感异常未知过滤|599诊断实机定位full_readback/runtime_verify|
|PAD-W25-exit-race|C|599→600：worker活着发成功回包/100ms确认竞态|真实线程红控证明风险，不能归为全部现场失败唯一因|Native真实join后同ID exitproof；旧fallback，超时未知保cut；原terminal语义不变|600集成；tool/pad_runtime_verification_jobs+fence|
|PAD-W26-reason-terminal|C|600未上线候选：诊断覆盖scope_incomplete变可重试|review及fixture已证|只两合并异常映射runtime分类；scope仍terminal不重试|v2修正后集成；旧seal留存|
|PAD-W27-two-tree|C|600：单次双完整树94.222秒超过90秒|同63只读probe确测；非R8不等最终包PASS|最多2线程全字节+latewalk，父join子才exit，取消未知保owner；不删旧树/缓存proof|601首代gen9完整读回PASS；永久parallel runner|
|PAD-W28-background|U|601：Dream后台22消息备份timeout|background cpuset，线程等待约50/49秒；支持调度瓶颈但非唯一根因已证|合法前台Activity发起dataSync执行租约，Native私有worker真实spawn/exit；不增90秒/不动CPU策略|FGS/Native worker候选封存未集成；完整后台生命周期未PASS|
|PAD-W29-first-allow|C|601新8498：Allow后又回允许、revision0|helper25 begin→loadConsent→finish清活pending已红控；现场唯一根因轨迹不足|Binder owner+finally，死/过期failclosed；完整APK含配套helper；真机首次Allow并发3轮+fresh工具|602含helper27；新机最终授权未PASS；事故doc已上main|
|PAD-W30-bound-retry|C|602新8498：registration_pending、boundservice未初始化|602 stopSelf不必销毁bound service且initialized=false先拒START的代码缺陷已证；603实时DUMP/log另确证当前初始化阻塞为identity vault与local relay不一致。sameIdentity同时比较encCipher和pair，仅此不能断言公钥已变化|603显式manual START重入安全初始化、async singleflight、新attempt时钟；STATUS纯读|603 PID14118：stage identity_restore_failed、IllegalArgumentException PAD identity vault conflicts with local relay，随后identity_start_rejected；lock held且FFI initialized。旧603失败证据保留；604语义身份修复后fresh仿真、三轮重连及宿主冷重开通过，605覆盖后实际工具通过。仅此闭环通过，不代替全部启动故障矩阵；详见PAD_REGISTRATION_NONCE_INCIDENT_AND_RECOVERY_20261010.md|
|PAD-W31-install-kernel|U|10/08假Success但PM无包；10/10增量probe安装panic|pstore DataLoaderManag/eventfd_write证明路径关联，内核源码唯一根因未定；不是Mali结论|禁止裸adb incremental；同机hash后文件pm安装；超时先对账、不复现风险；实际ID数据功能复验|成熟文件安装已采用；内核根修未完成|
|PAD-W32-gpu|U|63 GPU采图已有系统卡死边界，本周持续规避|不同于DataLoader panic，不合并根因/次数|禁已证风险采图，用D0 AX/组件白盒；固件专案根修才可恢复该测试|历史风险未宣称根修；不将未测算PASS|
|PAD-W33-ime|C|577/579：搜索SPACE+DEL后IME只96px条|真实触发且重触恢复712px，观察已证，底层唯一因未定|实际点击/IME高度/输入/收起；不只读shown|577历史3轮，579本轮1次恢复，不虚报合格轮数|
|PAD-W34-touch-overlay|T|520：首次点击/滚动无变化|KBoard D0全屏触摸覆盖层，系统lastanr空；不是VibeKits ANR|原键盘收起后真实触摸/帧；检查焦点与遮挡|520导航500触摸、聊天帧有限窗口PASS，不外推全业务|
|PAD-W35-r8-probe|T|579/598探针ClassNotFoundException|R8内联/改名已证，不是正式包缺文件|真实已注册handler或独立生产校验闭包；最终mapping绑定，真实终态断言|修正probe后有真实组件/读回结果；首FAIL保留|
|PAD-W36-client-sha|U|601用户商城下载SHA失败|失败文件已删，客户端日志不足；公开metadata/CDN独立GET一致不排除客户端问题|保正确线上对象，获取客户端全下载hash/安装；不猜改SHA或重传|未闭环；PAD601_MARKET_VALIDATION_DELIVERY|
|PAD-W37-ax-url|T|602新SHA一度配AX旧href|fresh右击同一次上传更新新URL，旧AX迟到/缓存，非服务器事故实锤|核fresh链接+完整无auth GET；不发布错误组合|602 c749/377265024匹配；public71仍601，表单取消未发布|
|PAD-W38-component-install|U|历史组件点击安装无效果/状态不明确|用户体验故障需与包缺失、工具未就绪分别定位；不凭点击成功|真实商城下载进度、按钮忙态、PM版本/hash、实际编译/运行；原始root cause拆见W47，商城点击无响应与安装回包不混因|579 Builder8真实商城安装hash+编译PASS；不代表模型自主开发全链|
|PAD-W39-helper-content|C|同version仅版本门槛可保留旧字节|升级资格缺同版本内容校验是已证代码风险，非声称602漏helper|签名+版本+同版本内容核验，合法更新版本保留；已内嵌组件首次准备|602 content gate已集成；新机最终功能仍失败另案|
|PAD-W40-async-pm|C|601新机：10:53:50 PID21209实际NameNotFoundException com.vibekits.vibekits崩溃|crash与601 R8 mapping精确对应MainActivity1368异步PackageManager callback，现场崩溃已证；不能据此断言当前离线唯一原因|异步PM元数据消失时捕获NameNotFoundException并回固定PAD_PACKAGE_IDENTITY_UNAVAILABLE终态；不泄露路径、不吞一般异常；旧红控和最终包真实回调/生命周期验收|urgent602/crash-before.log；Root读取实际crash及601 mapping；603 catch已集成，当前离线原因另案|
|PAD-W41-api-cancel|C|501开发期：取消A后发B，A迟到异常清B忙态|catch仅mounted不核取消token，生产控件红控已证|Android迟到取消异常不覆新请求，保其它平台；取消/失败/离页真实回归|PAD75_API_CANCEL_RACE_2026-10-04.md：6+3源测试；最终候选慢API另验|
|PAD-W42-font-heap|C|511/512高频导航Native堆约600MiB，512断流|匹配引擎BuildID的有效heapprofd指向FreeType CFF；显式样式fallback及FilledButton文字样式缺口已证|Android静态TTF及实际按钮fallback，旧红控；相同最终包10000事件/PSS与独立CPU窗口|PAD75_CURRENT_TEST_REPORT、DEV513：513长导航双阈值局部PASS；不推广所有负载|
|PAD-W43-poll-cpu|U|507空闲CPU中位5.162%超过5%门槛|周期工作线程/KeyStore布尔解密/重复commit有实现开销；不能将某项直接称唯一CPU根因|复用查询线程、按加密值变更失效非敏感bool缓存，真实授权决定不缓存；严格空闲5分钟进程族|DEV507_RESOURCE_DIAGNOSIS；513独立307秒CPU4.67%窗口PASS，后版须复验|
|PAD-W44-adb-ready|C|545前MCP可用但ADB AUTH/系统开关未好|ready短路不恢复、daemonPresent含AUTH，代码已证|MCP独立helper正常平台权限恢复，分framework/daemon/controller认证；不写RSAkey或关闭安全|PAD_MCP_ADB_RECOVERY：547动态serial真实命令局部PASS|
|PAD-W45-adb-race|C|546显式关闭ADB后1.2秒后台ENSURE抢回|后台自动恢复与诊断关闭无共同窗口，真实实机已证|同helper30秒诊断hold、显式ensure解除，准确文案不是持久关闭；MCP仍活、身份hash不变|547本轮0保持→显式1→新握手命令PASS；新机RSA/跨网另验|
|PAD-W46-random-identity|C|542/543：trusted=false可能绕完整身份门槛；用户63换ID|缺candidate时Rust随机；签名false跳guard已证；本次ID变化现场唯一触发未证|JNI前无条件完整身份准入、strict10位candidate、旧pair不可覆盖，早OPEN_TUNNEL/pendingwatch禁随机路径|PAD_IDENTITY_CONTINUITY_FIX_20261007.md；源正负控；不能仅数字ID证明密钥连续|
|PAD-W47-install-reply|C|547自然任务误称所有安装需用户确认并停工|native成功null与系统UI请求被统一成installerOpened=true，实际INSTALL_PACKAGES具备，已证|安装后PM及runtime分离读回；真实pending_user_action保回调/Intent，不能把Dart文案改正冒充完整native处理|PAD_BUILDER_INSTALL_FLOW_AUDIT；579实际商城Builder成功，pending分支须独验|
|PAD-W48-background-launch|C|547双屏任务工具预算耗尽，后台Activity启动被Abort|日志明确UID后台启动拒绝；不是浏览器前台推断|正常平台签名权限+真实grant，沿operation display启动读回；不放大模型预算掩盖失败|548权限已grant；原双屏目标未全通过，GPU边界仍限制|
|PAD-W49-context-cleanup|C|旧链只隔离未永久清理/索引与跨引用保护缺口|源码清理闭包不等于模型完成；具体删除变体各有独立负控|新会话原子提交、SDK派生/全项目引用/真实FTS、同源事务续删、未知保留；最终100轮真实模型与磁盘有界|PAD_CONTEXT_FINALIZATION_INTEGRATION；563仅一链永久删除读回PASS，不称全旧历史清理|
|PAD-W50-input-freeze|T|519删native_assets输入；543/544/549冻结缺工具或错误选SHA；本期fixture缺cwd/classpath|当前生成so是必需输入；复制旧文件名/文档块和环境不完整已证，不是产品运行缺陷|冻结闭包/前后hash/实际argv与环境；失败未入断言不记PASS；不得删soleorigin|PAD_REQUIREMENTS dev519、PAD_DEV541_CHANGELOG及本RUN首败|
|PAD-W51-acceptance-process|T|未完成注册→连接→工具即反复交候选；局部测试替代新机|PAD_INCIDENT_REVIEW明确责任与9类台账；用户验证版发布另有授权不能当正式全验|最终包所有永久case PASS、原触发/负控/新机/覆盖；不让用户反复发现已知遗漏|本期601为明确用户验证版；602未发，603仍candidate|
|PAD-W52-server-scope|T|10/09越只改PAD目标投入服务器方案/临时文件|复盘确认执行范围错误；没有改认证DB/服务或程序|保持PAD最小修；不操作服务器掩盖客户端认证，临时4文件已清并回读|PAD_INCIDENT_REVIEW_20261008_09.md；本轮继续只读本地|
|PAD-W53-fresh-state-light|C|590状态弹窗只初查，颜色长期陈旧|初次unknown后未刷新，已定位；与online语义错误分开|弹窗前台2秒单flight/10秒截止，迟到不覆新状态，关闭停止；真实状态转换|591源码/候选修复和后续实机需绑定最终SHA；PAD_CHANGELOG_20261005_09|
|PAD-W54-builder-contract|C|Builder8使用旧v7限定导致未知/模型误判通用构建能力|producer版本合同落后；Java8不等于任意Gradle/Kotlin/完整desugar|只精确7/8+toolchainSHA承认合同，项目layout/Java8/无Gradle限制不抹去；错版本/hash红控|builder-contract8-601四文件已入21204d；真实8包hash及受控编译有证据|
|PAD-W55-identity-cipher|C|actual60302：local/vault完整keytuple相同，认证解密出的ID均2075278498，但encCipher不同，身份恢复被拒|PyNaCl认证解密及同完整keytuple比较已证明是密文字节比较误拒同一语义身份。仅报告认证结果，不输出private cipher或PK数组；独立于bound-service retry缺陷|复用BC1.79共享semantic comparer，认证解密后比较严格合法ID及完整keytuple；不得reset身份或改服务器。必须覆盖MAC tampered、different IDs、different pairs拒绝，multiline合法值、legacy zero nonce与V1 nonce合法等价，至少3轮；最终完整签名APK新机首次authorize、fresh connect和真实工具闭环|RUN/identity-conflict603-probe/cipher60302/semantic-proof.json；实际60302语义同一身份已证。604/605完整签名APK实机通过：282工具、实际audio、604三轮重连及冷重开；同身份不同nonce与坏MAC/不同ID/不同pair回归通过。证据urgent604/reconnect、cold-reopen及urgent605/full-apk-installed.json、ui-poll/receipt.json；全部70项最终包验收仍未完成|
|PAD-W56-generic-plugin-closure|C|607未部署候选：generic server已启用scope门禁，但owned plugin未打包及未接PAD ACP加载链|final APK缺agent_conversation_host_plugin asset，H5无owned @caucy/vibekits-agent-conversation包；实际PAD runner只装attachments，Node函数fixture不能证明真实SDK接通|最终签名包owned插件资产/生成包完整性及ACP真实注册加载；合法可信agent/session/turn/signal调用通过，缺scope/撤销/迟到批准拒绝；不修改官方SDK、不放宽门禁；缺任一closure阻断部署发布|prepare607失败包SHA1d2d850ac23d56c0cd7be1112695ca7d714a8dd589381c5e9f2b802f26b6bbc2未部署，pack/load链已BLOCK；修复待完整重建与真实链验收|
|PAD-W57-invoke-catalog-lifetime|C|607未部署scope候选：prepend middleware的/catalog在自有controller/60s timer及SDK next之前|真实SDK ToolRuntime/TimeoutPolicy与挂起HTTP证明单插件Fiber.dispose仍pending，需要额外callerAbort才结束；body0。SDK timeout policy在next中不能覆盖前置目录查询|真实SDK running-agent/原token验证目录查询与body共用同一有界预算；caller取消/plugin-only卸载/迟到目录响应均退出且零handler、不重放；正常readOnly仍走原next、不改变原SDK核心|sdk-catalog-deadline607/red-green-receipt.json：真实SDK/AgentLoop旧插件卸载和总截止失败，新ca79b6...三模式通过；timer60s缩为40ms测试，非60s墙钟证明。正文与invoke均0，最终APK实机仍待验收|

|PAD-W58-owned-plugin-snapshot-scope|C|63实际2607fixed：28消息自动备份attempt1返回scope_incomplete / host/unsupported_scope；新owned脚本已实际安装但未纳snapshot白名单|installer新增harness_scoped_tool_invocations.mjs与pad-scoped-tool-invocations.mjs；Dart支持清单及helper中央pathAllowed均缺这2条。实机目录visited6无截断；旧Dart/Java红控复现。原attachment patch已覆盖，不是cache、Key或SDK坏损的证明|仅两条固定逻辑路径同步Dart capture/wire/restore与helper Producer/WireCodec/commit/load/restore；真实installer字节捕获及跨Dart/Java回读，未知同级/穿越/link/源变化仍拒绝；最终整包内置同签helper29且宿主最低29，覆盖安装确认实际新helper；最终包至少三轮自动saved新generation、完整scope及实收字节/正常恢复，保原Key/身份/会话。只修Dart不得关闭|upgrade607/context-postpublish.json、plugin-filename-inventory-reconnected.json：两脚本7191/396B；pad608-owned-plugin-snapshot-scope旧双端红、新Dart23项及helper真实加密commit/load/restore绿。当前607未修复，候选未实机PASS|
|PAD-W59-fallback-approval-lifetime|C|63实际2607fixed：PAD fallback人工审批超过60秒/原任务完成后仍显示过期音量确认弹窗|实际volume-ui及模型history/status共同证实任务终态与可见审批生命周期不一致；Root安全拒绝过期min后独立音量仍100。弹窗遗留已证，不把拒绝安全结果冒称生命周期修复，具体修复仍在进行|真实fallback审批绑定原任务/request及原截止；60秒过期、完成、取消、失败、上下文销毁必须关闭本次route并失效；迟到允许不得调用旧handler或新增grant，未知保持failclosed；不得关闭无关/新事务弹窗。正常及时允许/拒绝保原确认链；一动作一处busy。最终完整签名包至少三轮真实超时/任务结束/取消及迟到点击，记录UI关闭、原操作计数0与独立音量无变化；新请求可继续|upgrade607/volume-ui.xml + model-volume-history2/status3；Root安全拒绝旧min，独立音量100。源码候选由审批修复执行者处理，未标最终包PASS|

## 需求验收：13项（含下方三类仿真门禁）

新增需求不冒充已经发生的故障，也不因分类为需求而免验。未集成的FGS、approval-scope、UI-fold候选仍是未完项。

|caseID|必须保留的要求|当前边界|
|---|---|---|
|PAD-R01-navigation|按下即时淡背景；切回保上次工具/筛选/列表/计算器状态|514/515/520有限实机通过；最终候选再验|
|PAD-R02-calculator|单屏完整计算器，DEC/HEX/位运算/位宽/退格/清空|520有真实结果；桌面不回归|
|PAD-R03-ui-fold|回复下方过程、局部单动画/静态停止、字号、展开收起|部分569控件通过；新UI-fold候选未集成，不能声称最终完成|
|PAD-R04-ocr|取消旧agent/OCR开关，OCR移开发工具，图片/模型入口|569实际控件可见；真实识别/风险图形路径未全部通过|
|PAD-R05-consent-scope|允许/拒绝/撤销/黑名单/未知控制端；后台通知确认、不抢其他App|approval-scope候选未集成；必须真正到达授权关卡，离线不能冒充拒绝|
|PAD-R06-no-password|仿真开启不再另需密码，白名单仍须批准|旧设置密码/从未设置两配置×冷启/重开/失败手动重试；不能autoapprove|
|PAD-R07-dual-display|Harness D0、目标操作屏按真实displayPolicy，不影响副屏|所有动作遵守已授权显示边界；不得用危险采图补证|
|PAD-R08-full-restore|无备份/本地有效/partial/真正卸载：Key、聊天、SDK、设置、名单按最新scope契约恢复|独立Key保险库不是完整snapshot；local_current不冒充restored_full；新数据冲突保双方；仍待全矩阵|
|PAD-R09-resource|严格空闲CPU/RSS/线程/子进程/退出；任务抢占和后台保存有界|短窗口、单首代saved、非R8 probe不等稳定全PASS|
|PAD-R10-delivery|最终完整同签名APK、新机与覆盖、全异常门禁、商城客户端hash安装、源码云回读、现场清理|603是注册候选，整周gates全部PASS前不正式发布|

## 统计与证据边界

- W19/W20/W21/W26包含开发期候选缺陷，不能说已部署生产界面出过同样事故。W02保留427/458等早期包装门禁，W32保留历史图形风险，不伪造本周新增发生次数。
- W40已由真实crash与601 R8 mapping确认为异步PM回调崩溃；603已集成catch，但不能据此断言当前离线唯一原因。
- W30的绑定服务重试修复不关闭当前注册问题。603实际身份恢复报vault/local relay不一致；W55进一步证明同完整keytuple、认证解密ID相同而密文不同被误拒。W55语义比较已在604/605完整包实机闭环通过，未reset身份、未改服务器；605另修Android状态轮询等待闪动，六次实机采样稳定。完整72项验收仍未完成。
- 588稳定公开注册UUID与轮换pair分离后，589/590已有真实连接及工具通过；早期582失败不能被误读为始终不能注册。跨网同时换PK、普通卸载完整恢复仍未闭环。
- 602旧AX链接被fresh链接与完整GET纠正，不是已证服务器换错包；601用户商城客户端下载SHA失败仍是独立未闭环报告。
- Key保险库可用不等于聊天与SDK完整恢复；local_current不等于restored_full。新数据冲突须保双方。资源短窗口与首代备份成功不能替代严格空闲、任务抢占、Dream后台和所有worker真实退出。
- Mac/Windows同期的兼容入口、MCP收尾、ZIP资源叉、窗口断点、FD泄漏、空writer锁等属于各平台台账，不混入本次PAD数量。

## 永久回执合同

现有发布检查器固定加载`tool/pad_release_incident_matrix.json`，回执`padIncidentMatrixSha256`绑定该矩阵SHA。每case必须`status=pass`、同一最终`artifactSha256`及带真实文件hash的证据；`currentEvidence`只是历史线索，不自动转PASS。分类没有免测作用，无日期过滤、disabled或自选矩阵绕过。当前清单不是合格发布回执。

涉及生命周期/并发的回归至少三轮；新机首次Allow必须经过真实跨进程持久化、fresh connect与真实工具，旧授权设备不能替代。最终完整包同时保身份、Key、名单和会话；商城必须完成实际客户端下载校验与安装、源码云端读回及现场清理。603后续单项成功只更新相应case，不自动关闭其余项目。

## 直接核阅来源

本机发布技能`references/errors.md`、`pad-identity-startup-20261009.md`；项目`docs/acceptance/`中的`BUILD_RELEASE_INCIDENTS_2026-10-03.md`、`PAD_REQUIREMENTS_2026-10-05.md`、`PAD522_VERSION_GATE_INCIDENT_2026-10-05.md`、`PAD75_CURRENT_TEST_REPORT_2026-10-04.md`、`PAD75_DEV507_RESOURCE_DIAGNOSIS_2026-10-04.md`、`PAD_IDENTITY_CONTINUITY_FIX_20261007.md`、`PAD_BUILDER_INSTALL_FLOW_AUDIT_20261007.md`、`PAD_MCP_ADB_RECOVERY_20261007.md`、`PAD_CONTEXT_FINALIZATION_INTEGRATION_20261007.md`、`PAD_CHANGELOG_20261005_09.md`、`PAD_INCIDENT_REVIEW_20261008_09.md`、`PAD63_DEV568_571_CHANGELOG_20261008.md`、`PAD_RUNTIME_PROOF_FOLLOWUP_20261008.md`、`PAD580_RUNTIME_RECHECK_20261009.md`、`PAD_IDLE_RUNTIME_VALIDATION_CONTRACT_20261009.md`、`PAD579_REAL_DEVICE_PROGRESS_20261009.md`、`PAD_SIMULATION_AND_CREDENTIAL_PRIORITY_20261009.md`、`PAD585_STARTUP_RECOVERABILITY_20261009.md`、`PAD601_MARKET_VALIDATION_DELIVERY_20261010.md`、`PAD601_FRESH_CONSENT_INCIDENT_20261010.md`、`PAD602_BOUND_SERVICE_RETRY_INCIDENT_20261010.md`；`docs/diagnostics/PAD63_FRESH_MACHINE_CLEAR_20261008.md`及表列RUN原始证据。

仅记录公开身份语义、固定错误码、版本及证据边界；不输出私钥、API Key、密文、PK数组或聊天正文。不以本次整理宣称全部故障已彻底解决。

## 三类仿真新增发布门禁

用户明确追加PAD-R11/R12/R13新机商城、旧机覆盖、ID变化自动恢复；三者分别同最终包实测，不能互代。详见PAD_THREE_SIMULATION_RELEASE_GATES_20261010.md。当前固定72case，不删任何旧项。


## 当前76项补充基线

旧表与历史证据永久保留，当前矩阵是唯一case集合；补充W60/W61/W62/W63逐项绑定最终包。C51/U6/T6合63异常/风险，原13需求保留。610编译及fixture通过不代表76项正式发布通过。

### W63 首次凭据准备资格与原Key恢复

native secure入口的两处helper资格必须取max(MIN_NATIVE_SECURE_HELPER, MIN_HELPER)，旧29不得因已满足21而提前执行要求30的硬件scope事务；复用原安装singleflight，成功回调再核资格，失败/未知不执行，较新版本不降级。原身份、配对及Key不清除。

独立LEGACY模型Key入口本已有完整MIN30，不能把首次读取失败后controller为空称为Key丢失。仅首次lookupFailed、空值且无用户编辑时，新明确prompt/UI执行前允许同原Key的singleflight重读，截止2秒；不写凭据，失败/超时保持failclosed，迟到、dispose及用户编辑不得覆盖。保正常Key保存可在启动恢复尚未完成时操作，桌面原行为不变。

必须保旧负控与新正控：实际生产workspace/HarnessCommandBroker路径用合成数据验证恢复、再失败、用户编辑、dispose、超时迟到和并发六项，加原启动Key保存/迟到读保护共七项；不是七轮实机或真实模型PASS。native原handler三轮29等待30及原合成布尔/secure credential保持另验。最终同签整包还须真实冷覆盖、原授权/Key/会话、full endpoint及真实模型只读调用；outer ok不能替代内层成功。当前永久矩阵76项（63异常/风险、13需求；C51/U6/T6），所有旧case与用户规则保留。
