# 已授权管理MCP注册恢复与旧任务审核

管理任务MCP在服务端存在、但本机三层目录local为空时，先区分本地注册缺失、当前目录位置变化、显式禁用和真实鉴权拒绝。不要把目录缺失误认成服务器没有审核接口；也不要恢复明确已禁用的注册。

1. 读取当前MCP目录，只取instanceId、工具名和精确schema。大型JSON用结构化投影，不用rg把整条压缩JSON输出。
2. 找最近的正式注册回执/私有备份，核对instanceId、appId、transport、原可执行文件及参数文件存在。注册文件与私有操作员配置、口令文件均是受保护配置，即使旧版放在cache/mcp/registrations也不能当缓存清理；升级前后纳入精确文件哈希/工具数核验。
3. 复用既有client/harness_management_stdio.mjs的ManagementRelay和原私有配置：该适配器检查文件归属/权限、HTTPS、固定serverId和房间allowlist。只读tools/list验证实际鉴权。真实禁用、权限、密码、TLS或工具拒绝要保留，不改凭据/CA、不绕过或扩大房间范围。不得输出口令、token、cookie或请求头值。
4. 确认注册确实缺失时，以原字段和原已批准工具集合恢复，新增工具仅限本次任务已经批准的精确工具；使用当前服务schema并再次核对roomId.enum。私有配置、可执行身份和限制保持，目标存在则先对账不覆盖。文件600、目录700，写后读回、再用应用catalog_list确认真实实例。
5. 实际调用走恢复后的vibekits.mcp.tool_call，不以直接SQL修改业务状态代替审核。私有中继首次只读验证结束必须注销其临时管理会话。

2026-10-21的已授权通用房间管理注册恢复为16项，认证目录18项中只保留原12+已批准的file_upload/file_read/operation_status/operation_review四项。只证明该入口恢复，不代表整个集群验收通过；未查明注册何时丢失，不能归因某次升级或清理。

## 终态与副作用证据

- hbbv_task_detail的operations摘要可能不含evidenceRefs；需要精确原引用时用hbbv_task_operation_status。所有参数从当前schema取得。
- 区分工具receiptHash、任务outputHash、原始日志hash和独立证据文件hash。只有经核实且已登记房间artifact的独立证据，才能作verified_effect/proved_no_effect审核；unknown不等于未执行。
- 原任务已rejected、executionStopped、租约过期，并不意味着未决操作可以清零。保留原generation/fence/revision和回执，不重放下载、安装或提交结果，不将本地对账消失当业务成功。
- 旧操作evidenceRefs含原harness-session/harness-call，而最终result缺该session引用时，不能直接伪造result补引用。先核既有终态接口规则和原证据；未满足继续保留。缺文件或超时也不能证明没有过去副作用。
- 管理目录的running与deadline已过可以同时出现。先查实际mode：广播、竞争和DAG都需要按各自合同处理未开始实例超时；正在执行/不确定实例必须保留对账，已accepted记录及分数不能被覆盖。

## 大目录响应超限与摘要分页

`MANAGER_RESPONSE_TOO_LARGE`不等于权限失败或设备离线。先保留原工具/参数和错误，原房间、原权限下缩小limit；2026-10-22生产完整单台约198KB，limit30失败、limit1成功，按原cursor+固定筛选条件分页取得全部8台在线名册。不要提高响应大小限制、跳过失败页、换权限或把未取得页面当空集合；读取服务端名册不等于连接其中设备，仍遵守用户忽略/离线设备要求。

新源码支持`hbbv_room_devices(...,view="summary")`及REST同名参数：SQL只投影设备facts，工具/技能正文不随列表返回，仍按完整声明搜索；保留在线/等级/成员修订及就绪摘要。先核当前工具schema确实支持view并实际调用，不能把main源码当生产部署证明。summaryOnly不是执行授权，按deviceId取完整详情/工具及当前身份、授权后才能执行。旧默认full仍保留；摘要与完整视图cursor不可互换，翻页保持view/搜索/平台/状态不变。

本地10,000合成成员首100项约100KB，仅证明SQL分页/响应边界；不代表10,000真实设备、跨网稳定、真实GPU跑分或长期空闲通过。正式规模结论仍需实际设备、时长、资源与重连证据。

### 服务新schema与本机登记快照不同步

2026-10-22已验证：服务部署摘要参数后，本机catalog_list仍可能展示旧登记schema。复用原ManagementRelay和原私有配置，真实认证tools/list；对比旧schema，确认只新增获授权的可选view枚举，再原子更新该工具schema/catalogRevision。保留原工具名集合、房间enum、执行文件、参数及私有配置；检查写前文件未被并发修改、权限600和写后读回。临时管理探针会话在finally注销，随后通过App实际catalog_list及tool_call确认。无需重启共享App，也不提高响应限制。

本次生产limit30+summary真实返回15名成员约24KB，旧full单台仍有完整目录。此为历史实例证据；每次仍核当前schema、权限、房间及实际返回，不能将源码或登记写入成功等同于调用成功。

### 摘要网页与展开详情的权限分层

管理网页可以让折叠列表只请求summary，展开时再读原完整设备详情；摘要不含技能/工具正文时，应继续按需加载，保留原完整视图，不把未加载标成0。保持筛选、游标模式、失败快照和过期在线状态规则，并实际观察折叠后的请求，验证没有继续拉整页目录。

客户管理员可列出其他账号创建的本客户房间，却在展开时404，曾由内部全局积分接口的devices.owner断言触发。房间详情改为按已核实的客户/房间/成员权限读取，并把积分与冲正记录的SQL限制到当前房间；设备owner、原无room的全局积分接口和现有账目保持。验证授权管理员可读、撤销后拒绝、其他房间事件不返回，并用旧源码负控和真实浏览器复现。生产读现有积分只核账目与房间范围，不记作新增任务成绩或Office升级完成。
