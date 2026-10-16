# Windows直接入房与未执行领取恢复：2026-10-04

## 真实入房证据

用户指定6175875975（LAPTOP-RQNVQ34M），原ID新握手、原主机指纹、SSH/MCP均通过；实际dev446，原办公388630819。最初集群关闭且未配置。经服务端仿真ID载体发现反向consent_pending时未代点确认。直接HTTPS仍失败，Windows明确Failed host lookup/11001，不能据此报物理机器离线。

核对服务端当前实际接口地址和既有证书SAN，确认当前局域网IP被证书覆盖，才配置该精确HTTPS origin、可信host与既有公开CA。不能照抄本文历史IP；不能写hosts、忽略TLS、扩展系统信任或复制服务私钥。局域网直连是独立的集群HTTPS接入，不代表获准反向仿真访问，也不是跨网自动恢复方案。

通过原ID的cluster.apply创建申请后，管理端读取具体申请、核对deviceId及installationKeySha256，再用其实际revision批准。仅授予membership/capability-report/heartbeat。客户端报告approved/roomsAreLive/connected/simulationReady且资料版本被接收；独立管理API核对同一ID在线，心跳3.324秒。入房完成不等于模型、业务授权或任务执行已通过。

新增成员令房间批准名单由六变七；下一次全员广播必须重新查询实际批准名单并冻结合同、重新取得对应发布证明，不能沿用六人合同或为了凑数移除现有成员。

项目证据：WINDOWS_6175875975_CLUSTER_JOIN_2026-10-04.md。

## 严格恢复已证明未启动的领取

实际Windows58旧步骤字段缺陷在SDK会话创建前拒绝，服务端操作为空、结果为空且会话owner不存在。经过实际管理reconcile及已绑定证据hash，服务器保留同一fence/worker的proved_no_effect历史并释放worker/lease/offer。合同随后过期，不允许重放或把它改回有效。

客户端可保留审计并归档无SDKsession、无待提交结果、无output/evidence的本机记录，但必须使用认证协议返回的服务器detail：room/task/instance/fence/device匹配、current worker/lease/offer/result/review为空、operations为空、恰好一条对应proved_no_effect历史、review同决策且reason非空、证据hash有效。任一缺失、不同fence、模糊历史或可能副作用均不归档，不能用超时或缺回执推导未执行。旧服务历史不能删除。

实际认证历史及22个不安全变体回归通过，另有33项既有Flutter回归。新Windows447-v3冻结包直接提取代码再验同一22项通过；仍未传输/构建/安装。因此这是源码/归档证据，真实设备的旧日记恢复尚未通过。


## Windows448 runtime与执行路径实证

签名PASS不能代替完整成品语义验证：本次447最终签名/243PE/外壳都通过，但实际缓存client.js没有必须的rename/delete钩子，未安装。448只补当前准备入口及实际installed检查，保持SDK/Flutter/锁不变；缓存、候选和真实安装各层分别核验。Windows file URI必须用url2pathname转系统路径；项目相关测试明确工作目录，不能把默认用户目录的ENOENT称为产品回归。

仿真上传localPath在App进程中解释；发送端必须先resolve为实际绝对路径。Windows upload返回的remotePath可能是SSH用户目录下相对路径，ScheduledTask不要直接引用。按当前已授权用户核对绝对路径与hash，或显式设置WorkingDirectory；不是改全局shell、服务或安全策略。官方任务动作文档确认未指定目录默认System32；官方Windows OpenSSH确认默认cmd和sshd -f合法自定义配置：
- https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/new-scheduledtaskaction?view=windowsserver2025-ps
- https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-server-configuration

原58本次448守护06:11:54Z verified_committed，完整回退点保留，原ID/SSH指纹/原公钥/授权/房间都保持，MCP/SFTP和安装完整55资源/live relay通过。最初控制器相对路径探针被拒绝，改绝对路径后在同一守护期限内完成，没有重装/续期。xzl备份首个任务Ready/exit1、没有恢复目录，实际原因相对脚本路径不可达；仅在确认首败终态后用同脚本绝对路径启动独立v2，保留旧日志。当前后续断联，v2终态未读，不能再次复制或冒报成功。

同次未启动任务在448中依据认证服务端的proved_no_effect自动退休；保留原room/task/instance/fence和服务端摘要审计，业务未重新执行，也未复活过期合同。该逻辑有真实部署证据，不授权清除其他记录。


Windows真实回归进一步发现：Mac通过的仿真控制器fixture若使用无.exe的relay名，会被Windows生产HARNESS_HEADLESS_RELAY_REQUIRED正确拒绝。449首次17通过/13失败，保留失败且Release未开始；仅七个fixture路径按Platform选择正式Windows relay.exe，绝不放宽生产限制。保留Windows已有测试，使用独立候选回归名；重新核对全部982父输入、备份一个变更后，新独立任务回归exit0并进入Release。此时不能称签名、安装或机群稳定完成。


## Windows449：本人认证后同一签名事务与原ID守护升级

本人完成硬件令牌认证后，观察同一签名run的summary/state/exit、2轮及243内层通过，再独立验证最终外壳实际哈希、签名主体与时间戳；不能仅内层PASS就安装。58本轮外壳11:11:54Z完成，独立验签通过后用既有交互Limited计划任务一次启动守护覆盖，原448完整33029备份及不可变清单先核对。

默认PowerShell调用脚本可能被执行策略拒绝；保留原拒绝，沿项目已规定的进程级pwsh -ExecutionPolicy RemoteSigned，不使用Bypass或改全局策略。上传脚本核对字节哈希后立即移D；不能留下身份私钥或PIN。

升级停止原App后仿真与房间可短暂不可达；观察超时不代表事务终态。控制器持续核对原ID及可信SSH指纹，不重复安装/重签、不延长守护。原424于11:20:45Z真实恢复，449主签名/真实MCP/SFTP核验后11:21:19Z守护verified_committed；随后实际安装载荷/原生Relay、客户端实时approved房间及原安装身份、服务端实际449心跳均通过，安装exit0/任务Ready Last0/守护退出。固定守护证据不能当作长期自动进程守护或全部UI功能通过。

远程办公旧查看窗口可能固定旧时间帧；不能用陈旧PIN画面、桌面或在线灯证明当前安装过程。需要新的可信握手和实时数据；本轮最终成功以原ID SSH/MCP/传输/安装载荷/客户端与服务端房间证据为准。原其他三台仍offline、Mac完整门禁BLOCK时保持准备阶段，不开长稳计时，不以449版本整数认定Mac与Win同源。


## 隔离300节点60分钟服务协议负载

复用hbbv既有分组/协调者/逐人公告回执/屏障断言，通过独立loopback HTTP、独立外盘临时SQLite及测试身份执行；不向真实房间混入合成节点。先短时预检真实时间超时、旧epoch拒绝和服务进程重启，再一次启动3600秒正式事务；用具体driver/service PID证明live，不凭状态文件，不重启或延长在途测试。实际重启后读取新的servicePid，不能因旧PID不存在误判事务结束。

2026-10-04同一正式attempt实测3600.149秒、900轮4秒心跳、300合成节点、323210 HTTP，p95 0.022290秒、0非计划5xx/传输失败；30节点停发120秒，独立SQLite证明270在线/30离线，恢复后300在线与历史逐人300/300/300回执保留。旧98464正常退出、新73121保留冻结分母；终态PASS/full60Minutes=true且所有进程退出。来源与运行器逐哈希复核不变，原始收据保留。

该证据仅覆盖隔离服务协议负载和持久回执；不能外推WAN时延、100实际硬件、真实Harness执行或业务副作用，也不能替代原六台合格更新与入房、双向仿真消息、独立评分或真机长期稳定。真实六台前置未全通过时仍保持准备阶段。


## 2026-10-05：Windows451同一事务、现有空闲节点与版本合同

原424第二轮完成后沿已验证独立交互固定任务验签，最终外壳16EE35D7AB8A3F742416874A6557A4B16DBBB6029870A6F3839577060258C915/259721672B，签主165C80D71D39DF842FEC7C84F74B654059AAD759DEE220293BBB80B5C2B23FC1。旧450完整回退为33030文件/清单CA6D476E68B284857345CB3F382A2DFA1256B54D1A3FB3A17F590609FD8D486E，不可套旧449清单。单次独立守护覆盖后同原ID/指纹、实际451签名、真实MCP/SFTP健康提交；23:51:53Z守护终态，实际主18628/Session1、安装exit0/任务ReadyLast0、客户端房间和服务端451新心跳复验，载荷/liveRelay通过。固定回退守护不是长期自动进程守护。

用户允许利用现有空闲节点继续测试时，六机仍准备阶段，但不必阻塞同范围只读/真实任务预检；保留原六最终目标，补充617不替代原节点。实际605/617已入房且无taskSessions，任务发现显示旧合同failed，不能复用旧租约。原组长Harness status返回NOT_ACTIVE时，session_prompt只支持当前可见会话，不向同事当前会话误发。此处通过已验证空闲Windows451官方Harness收到accepted/busy=false开始新的只读组长预检，仍需实际工具轨迹、签名上下文及独立验收，accepted不等于闭环。

软件营销版本和实际EXE完整build分开：617实际384而登记仅1.4.127。官方商城与Common实际平台仍Mac383/Win384；Common顶层419本次只指PAD419，manifest MD5与实际CDN核对后才按targets分平台。已当前走already_current，不为测试重复安装或降级；不能把只读核验冒称发生更新。


## 2026-10-05：四在线中间验收的合同和真实执行范围

原Windows424与补充617已签452原路径升级、原ID/指纹/实际版本/MCP/SFTP及独立回退健康提交真实通过。617必须恢复原`D:\vibecoding\Vibekits`快捷方式/卸载登记和实际加载CRT，不能将诊断路径能运行称原安装路径升级。其旧232和健康446分别完整备份，不能用旧232崩溃版本作正常可运行回退。后续版本需重新验证，不套旧文件数/清单/hash。

当前只验四在线时，原六最终目标和离线批准成员保留。`broadcast_each`的`expectedDeviceIds`须等于全部批准成员，不能删离线成员或加补充冒充原六来使验证过关。中间四设备任务可用原`cooperative_dag`加各step `requirements.deviceId`固定；工具、模型、代理、槽位、签名上下文、唯一租约及操作许可要求不降低。

匿名`service-info`按设备token隐藏授权，空`allowedExecutionTools`不表示全局关闭。用正确已授权身份或管理guide读取实际范围。此次已配置11工具含下载/安装/消息ACK，但devices仍原六、不含617；未正常追加范围时617不能执行。Root只准备带原六+617的配置候选，未应用/重载，不从候选宣称授权完成。

四固定步骤的完整Office核验/必要更新合同已按运行中AuthenticatedOpenAPI验证Schema，仍未发布。缺模型Key、当前包/实际工具观察/签名上下文等保持待验；同版或高版走`already_current`并独立留证，不降级、不重装来造升级正例，不据此完成实际自更新目标。管理目录修复及HTTP成功也不能替代持久双向全文ACK、独立review和评分。


## 2026-10-05：四台观察与617正常执行范围补齐

- 用户要求先完成当前155/529/424/617四台，不等待原六齐全；独立记录四台观察段，保留原六成员和最终目标。59次五秒采样只证明该五分钟段；维护、掉线和采样间未知时间不能计作连续在线。
- 已批准入房及匿名service-info不能证明业务资格。原执行scope确实只有原六、没有617；在原身份、公钥、签名版本及实时房间核验后，按用户授权仅追加617，原六及原11工具保持，签名上下文、本机grant和操作permit不变。
- 先核对全部9房间，无执行中业务租约；旧published任务仅bidding/fence0、无offers或operations，不删除或重放。读取原LaunchAgent的实际PID和日志路径；源码加载指纹写stderr，查stdout未找到不能判源码未加载。
- 正确stderr证明磁盘与已加载app.py同SHA后，仅改scope JSON、保留原文件证据，沿原supervisor重载一次。新PID38517、严格TLS/管理员认证、原服务UUID及管理execution-scope实际7设备/原11工具通过，随后四台新心跳恢复。不能改数据库绑定、手工置grant/identity验证位、删成员或放宽门禁。
- 资格补齐不提供模型密钥，也不证明发布/竞标/领取/执行/消息ACK/独立评分。617签后真实只读Harness仍报deepseek-official/deepseek-flash MISSING_CREDENTIAL，应走正常Models凭据流程，不能用维护SSH代替模型或复制其他设备秘密。

配置候选、正常生效与完整业务验收分别记录；正式证据EXECUTION_SCOPE_617_*及本轮两机原ID健康提交见VibeKits项目验收目录。
