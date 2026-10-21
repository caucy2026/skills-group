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
