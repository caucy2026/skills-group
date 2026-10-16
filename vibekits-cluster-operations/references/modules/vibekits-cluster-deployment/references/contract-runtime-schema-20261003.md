# 真实合同冻结、步骤字段与运行时启动证据（2026-10-03）

本次真实Harness通过管理MCP和原发布者身份发布六机办公合同，随后三设备自主竞标，Windows58真实claimed/context_issued。它仍未执行：会话启动失败且租约进入reconciling，无安装、消息结果、独立验收或评分。每个结论有不同证据，不混成“集群通过”。

## 证明绑定完整合同

第一次智能体challenge与设备应答使用同一对象，但publish多加description，服务器正确PUBLISHER_PROOF_REQUIRED。公开备注字段也是被签摘要的一部分，不可认为无害而在证明后追加。机械diff确认唯一差异后，保存同一canonical合同，真实核对businessDocument与packed合同SHA。旧证明已过期且发布失败已对账，才建立明确新尝试；challenge→原ID真实answer→publish只添加publisherProofId，移除此字段后deep-equal原对象。120秒证明窗口内不插入无关能力检查。固定requestId，响应未知先task_list/events对账，不能换请求身份盲重试。不要将本机尚无执行任务上下文误认为发布者身份验证失败。

## 测试要覆盖真实服务端schema

服务端task-contract/1的steps数组使用stepId，旧native运行时仅按id查找，真实已签上下文必然TOOL_CONTRACT_MISMATCH。历史fixture只给id，因而没有发现。新的回归直接读取本轮真实冻结合同，在相同官方SDK下旧源码实测失败；最小修复优先canonical stepId，兼容缺stepId的legacy id，拒绝冲突别名/重复匹配/超合同工具。新回归及既有runtime/official native tool/endpoint门禁通过，不等于已部署。Windows完整包门禁新增集群运行时必需文件、与冻结源码的摘要一致性及包内Node语法检查，防止构建时仍带旧脚本。真实受限会话、许可和租约仍需复验，不能改已签运行包冒充交付或清日记重领。

## 保留第一次错误，不被二次锁超时误导

xzl旧空凭据锁存在且当前没有Node，独占只读检查成功；在现有管理员授权下保留空锁，确认凭据不变并受控冷启动同一签名程序，原ID/SSH/MCP/房间恢复。随后看似仍是writer-lock timeout，但第一次SDK新启动日志先报EMFILE（too many open files），重新留下空锁，后面启动才锁超时。因此清锁不是充分修复，应定位完整SDK启动时的文件资源耗尽。

同一官方Node及dsh-atomic-write在独立工作目录、真实Harness目录的唯一探针名，原生wx写PID和withFileLock均通过；这排除普通目录权限或该锁库在所有Windows必然失败的结论。仅读锁元数据和启动错误，不读取凭据内容，不改当前有效锁/钥匙串/信任；不凭年龄或名字删除。不得重复清锁、反复重启、任意增超时或换依赖。原SDK首次失败与后续错误、独立夹具、原始回执均保留。

历史路径/IDs/版本仅指当时案例。当前新候选须重新冻结、原签名、原ID覆盖、实际完整任务验收。详细项目证据：CLUSTER_OFFICE_CONTRACT_RECOVERY_2026-10-03.md及OFFICE_*、XZL_FIRST_STARTUP_AFTER_LOCK_RECOVERY、两目录锁夹具回执。

## Verified model health success must still satisfy the heartbeat schema

Actual Windows446 produced a real Harness model description, then the client reported heartbeat HTTP422 and non-live rooms. The frozen client used credentialStatus=ready when modelProven=true. The unchanged device-capability/1 schema only accepts valid for this state; keyReady=true also requires valid. Service-side fresh presence did not prove the client's whole health/room synchronization succeeded.

The minimal serializer now emits valid only with actual credential presence, proven generation and a timestamp. Five actual Dart-generated states validate against the unchanged schema; the real server accepts the verified model and rejects the old ready status with SCHEMA_INVALID/422. This is source/in-process regression evidence, not deployed-device acceptance. Include the helper in the frozen source archive and check source parity; never relax schema or fake readiness.

The same Windows official SDK in an isolated home/workspace/cache ran90s, announced web, had no EMFILE/lock timeout and a sampled handle peak267; its diagnostic process/listener ended. The real App later generated a model description after retaining the empty lock, but this does not close the original first-EMFILE root cause. A parent-process NODE_OPTIONS diagnostic was overridden by the App's mandatory lifecycle watchdog; zero metrics mean no probe loaded, not zero file pressure. Preserve the watchdog and do not remove lifecycle/security protection for a diagnostic.

Project source/evidence: WINDOWS447_MODEL_HEALTH_PREPARATION_2026-10-03.md, model-health-schema-regression and XZL_STOCK_SDK_FS_PROBE_V2_TERMINAL_OBSERVATION. Source transfer to a specific build node may require platform approval even within the original build goal; retain the prepared exact archive and do not bypass a rejection by another route.


## 2026-10-05 实际455 Harness发布与JSON恢复

原424真实Harness在同一通用房间发布四台cooperative_dag合同。首次turn4只做目录/身份查询，在创建挑战前因DeepSeek工具参数无效JSON报MALFORMED_RESPONSE；不能据此宣称发布，也不能把目录首屏旧模型记录当本轮证据。先对照prompt接受时间，分页到新轮次；旧会话可跨重启保留大量历史，状态cursor不代表历史已清空。

一次恢复沿用同一个冻结合同、challenge/publish幂等ID，不再重复枚举巨大目录；真实模型事件327取得挑战、333由原424安装身份完成publisher.prove、339实际发布。独立管理task_detail核对task 0bb047efb96767069a493aba4521f1da、contractHash a1bac970772751ae3b904f72de125fb6c7cecbec3ca88a4616d888dadc6c96da、原c28e安装身份及四个bidding/fence0实例。这证明真实发布链，未证明竞标、分配、执行、双向消息或评分。超时未知时必须按原请求/合同查询，不能生成新发布ID重试。

Windows本机catalog_list曾tools/call超时；同身份跨设备155目录和原hbbv-authorized-room-manager实际管理读取成功。目录runtime.state=error/capacity0与callable=true并存时，不猜测调用结果，以实际只读调用判定并记录差异，不绕过授权或重启工作。没有降低requiresModel/Agent，也没有shell绕过任务工具。
