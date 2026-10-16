# 真机仿真与ADB调试

出现完整快照预算失败或旧包无法保护新数据时，读取[快照容量与覆盖前保护](snapshot-capacity-migration.md)。

CPU 基线及受限系统栈采样读取 [CPU定位路线](cpu-profiling.md)；先核精确产物和当前系统能力，不提权、不改全局策略，不把短时采样当发布通过。

## 最短白盒路线

先确认控制端桥、目标routingId、外层结果与内层structuredContent，再查实际版本、进程、当前工具目录、窄日志及原operation/session。绿色状态/PID/目录不是实际执行证据。工具ID从源码常量或catalog取得：`vibekits.harness.context_status`，不是臆造的`vibekits.device.harness.context_status`。

外部Mac没有已注册MCP时使用remote-simulator技能invoke.rb：
```sh
ruby /Users/newlink/.codex/skills/vibekits-remote-simulator/scripts/invoke.rb vibekits.simulator.connect '{"routingId":"2075278468"}'
```
这只是当前授权63示例；同事必须核身份与当前授权。connect返回新的本地ADBserial后按指南在对应server `adb -P <port> connect <serial>`，再执行命令。没有注册serial不能把device not found说成PAD故障。覆盖后disconnect→connect，不能沿用旧动态端口。

调用示例只读：
```json
{"routingId":"2075278468","toolId":"vibekits.harness.context_status","arguments":{}}
```
模型提交前保存RID/SID及请求；session_status/history按原SID/RID有界分页到hasMore=false，不输出reasoning_delta/聊天正文。unknown/超时先对账，不再发同一任务。工具schema以当前catalog为准。

## 通道失败恢复

1. 先读原事务回执和控制桥，核本机正确App进程/版本、目标仿真开关和授权。
2. 用已登记、已授权同机远程桌面/可信ADB备用通道恢复，分别记录黑屏、输入无响应、认证失败；不要统称离线。普通确认核设备与请求来源后自主操作。
3. 恢复后原ID重新连接、真实工具调用和实际ADB成功；只房间心跳不算。
4. 历史75离线不连接限制已由用户于2026-10-12撤回：允许重新连接75（旧ID9464730211）；必须核当前身份及授权，不把旧设备当新机。没有许可的PIN/陌生控制端/系统拒绝不绕过。通道原事务未知不能重复安装。

## 63设施的精确边界

诊断守卫必须区分身份作用域：`adb shell settings get secure android_id` 的全局值不等于普通应用 `Settings.Secure.ANDROID_ID` 的 SSAID，平台签名也不能当作两者相同的证据。物理设备可由Root通过既有独立LAN核全局摘要；APK内核自己的精确包版本、完整SHA、UID和C8，不把shell摘要直接硬比appSSAID。65106及65025审阅中已在执行前拦截这种测试守卫误判；它不是设备ID迁移或产品认证失败，不清身份/Key来迎合测试。

可信LAN救援：`adb -P 5041 -s 192.168.3.63:5555`，要实时核目标；历史仿真5039动态端口不能照抄。仅D0，先唤醒再读实际AX，梦屏首点可能被吞。自身AX probe self-target不停止Main；bootstrap InventoryInstrumentation host-target会停止Main。

禁止63截图/GPU抓取、增量安装、su/root、改MAC、清ADB授权。D2外来com.swdol.client.nativegpu不动。授权受控停机不允许中断在途SDK/快照。

## 覆盖/完整读回前静默检查

读fresh context：inflightUiRuns/inflightWorkspaceUiRuns=0、persistencePending=false、compaction/cleanup无在途、hostSnapshotCutPendingOrHeld=false、sdkSnapshotAdmissionHeld=false、activeOwner=0，再核native服务/任务实际状态。otherProducerCount=null只是未知，不写成全局0。

`com.vibekits.bootstrapprobe/.InventoryInstrumentation`完整读回host-target，仅使用与当前host/helper匹配且签名/DEX完整的探针。调用带`action snapshot-v2-readback`与当前`expectedVersion`，保存0600原日志，提取元数据；检查allWireEntriesVerified、restorePathCoverageComplete、frontAndReferencedSdkShapeVerified、liveMatchesSnapshot、修订一致、Key slot仅available/revision。不要读取Key值或导出聊天/wire。

返回liveMatchesSnapshot=false不能覆盖/卸载。保留首次失败，定位生产NativeVerifier的失败条目，仅返回逻辑路径hash/类型/长度/hash，不打印内容。instrument退出后沿原Main启动恢复；新快照后再次完整读回仍须定位而非无证据重试。

## 组件的真实验收

默认PAD目录现仅Builder79、Proxy80；Proxy80被PadProxyDebugGate默认过滤并非目录丢失，debug解锁只能使用原正式UI路线。每次核公网现有记录，不把ID永久写死。

Builder私有builder-debug.jks/password是开发签名身份，不是可删除缓存。原“卸载组件”调用桌面目录服务且host包比较错，Android没有生产安全卸载流程。2623隐藏不支持按钮、直接service拒绝且0删除；不是实现Android卸载。经明确授权的`pm uninstall -k`仅诊断保数据路线，不得称用户生产卸载可用。实际商城单点安装→PM版本、APK bytes/hash、UID→真实Builder一次任务→原taskId独立APK验证；不以模型文字完成当成功。

## 模型敏感工具审批的时效（2623音量实测）

提交真实任务前准备好能识别当前固定公开title的自身AX probe；陌生或unlisted标题不能盲点。普通已授权操作出现新对话框时，核当前host/package/D0/title/范围/按钮后及时一次Allow。不要在待审批窗口内才开发探针；以实际调用链的截止为准。KEYCODE_WAKEUP后重读AX，dream窗口未退出时不点击旧坐标。

2623第一轮音量任务actual set被审批路径中止，独立读回99；保留失败，不能声称写入成功。任务terminal已确认后，新任务用固定“允许 设置PAD系统音量并读回？”title及新bounds确认一次，actual model set/status完成且独立99→100PASS。无已拒绝工具/平台审批可被该流程绕过；拒绝与超时/失效仍须区分，不把unknown重发。

## Scoped approval observers and dynamic session IDs

Before dispatch, prepare canonical and MCP-alias fixed titles for actual selected tools. A short-lived own-UI observer may approve an already-authorized ordinary request only if actual accepted request/user-text SHA match, Main D0 active/focused, exact tool+controlled target parameters, unique Allow once bounds and no overlapping foreign window/IME. Bound time/action count, stop on unknown/terminal; never grant a global mode or use a new tool to bypass an actual platform rejection. Test scope negatives offline before device execution. Existing sandbox file rights may permit SDK write without MCP approval; verify exact resulting bytes, do not require nonexistent UI clicks as proof.

App approval expiry was recorded as user denied despite Root not clicking deny. Preserve actual aborted results; do not claim source/build success or infer platform auto-review rejection. New actual approval requires a new fresh current window after terminal pre-dispatch outcome is reconciled.

Always use sessionId returned by actual accepted session_prompt. Real2623 automatic rollover changed1791707525979798 to1791731064545184; a client hard-coded SID assertion failed although dispatch was accepted. Reconcile that accepted RID and attach its returned SID; DO NOT resend because client assertion failed. Verify context cleanup separately; new SID is not hardware-ID change and must not clear device credentials.

Source compile-error workflow: original native terminal failure independently confirmed, only missing original file repaired, new RID without old operationId creates new source ZIP/task; old task unchanged. Unknown native build only observe original handle.


## Test-probe package visibility and failure isolation (62528/62529)

An Android11+ self-target probe can receive PackageManager.NameNotFound for an actually installed Main when its manifest omits explicit package visibility. Before scoped ordinary approvals, independently confirm installed Main via trusted ADB, then qualify probe getPackageInfo/version/certificate on device. Declare only the known host package in queries; do not add QUERY_ALL_PACKAGES or remove identity guards. Record SecurityException/INSTRUMENTATION_FAILED as probe failure, not Main crash/offline/authentication failure. Observer stops immediately on target-guard/parse/instrumentation errors rather than repeating blind attempts. Parse the entire JSON payload, reject trailing input, preserve first failure, and reconcile the accepted model request/returned SID/original operation before any retry. 62529 fixed these test-only defects; no product runtime fix is implied.


## Search IME acceptance through current public key metadata

On626 actualKBoard182, public AX reports keyFrameLayout -> android.view.ViewGroup -> android.widget.TextView, even when source implementation names ConstraintLayout. Read only the current exactIME/D0 keyboard guard below return-row-derived key area; fixed letters and contained depth2 safe leaves, no candidate/password/editable/private field text. Do not infer installed structure from newer source or fixed resource IDs (letter IDs absent). Include-not-important/report-view-ID flags only on short-lived ownUiAutomation can expose the needed structure; preserve node/depth bounds and other accessibility services.

Search hint disappears once a character exists. Controlled observation must be explicit, bound to the previously verified exact focusedMainsearchbounds and unique nonpassword editable node; output only empty/z/zi/zip/other, never unknown contents. Current source/guard is ui-nav-probe62633; package/signature stable. Touch each actually observed key, read controlled state before next touch, restore only own characters through observed backspace and close IME/restoreHarness. Evidence ime-fixed-key-readonly626/REAL_SEARCH_IME_ACCEPTANCE.json proves626 specific search open/printable touch input/cleanup, not everyIME/double-screen/gameplay requirement.
