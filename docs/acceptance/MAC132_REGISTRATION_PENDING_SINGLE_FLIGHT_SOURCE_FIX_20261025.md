# Mac132 原生中继注册等待与并发启动修复（源码阶段）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 现场依据

原132的签名798覆盖在30秒仿真门禁失败后回滚；原生relay于目标本地00:48:20、00:48:28、00:48:30和00:48:38多次启动，其中00:48:30另一支遇到IPC `Address already in use`。同字节798 helper在Mac445仅一支、约0.95秒收到keep-alive，真实gate ready。132前三节点的`SERVER_ERROR`仍未取得服务端内部根因，不能把本修复当作整个升级已通过。详见[首败与同字节控制组](MAC132_798_SIMULATOR_GATE_ROLLBACK_20261025.md)。

源码`RustDeskHarnessShareService.ensureHostAvailable`原先在不可呼叫状态立即启动relay，默认只等8秒；即使状态仍是`registration_pending`，也会按“旧中继”执行stop与第二次launch。多个App入口还可并发执行相同流程。这个行为与132多支进程的时序吻合，且在隔离fake runner/launcher负控中真实复现：注册等待测试原本抛`HARNESS_RELAY_NOT_CALLABLE_AFTER_TAKEOVER`并执行第二次启动；并发测试原本启动2支，预期1支。

## 最小修复与非交付合同

- 原生`--status`从运行中IPC取得有效原ID时，`registration_pending`和服务器尚未确认的`offline`都保留现有单实例继续注册；超出本轮短探测窗口返回明确`HARNESS_REGISTRATION_PENDING`，不stop、不再次launch。仅从持久配置`--get-id`回读的ID不能冒充运行中IPC。后续调用仍先读取状态，等待同一实例。
- 同一组桌面启动参数在进程内共享一个在途Future，避免同时看到offline的入口各自启动helper；结算后移除Future，不缓存旧在线结论。Android启动路径和真实旧单实例离线接管路径保留。
- 隔离目录从当时VibeKits main提取这两个目标文件；直接导入的三个源码依赖与main SHA一致。`prebuild`执行资格检查返回`ELIGIBLE`，policyMain `023bff9b9f503c1c6f5afdafebeb085ba184bb83`。
- 新增三项历史回归，分别覆盖显式`registration_pending`、有实时IPC但暂时`offline`、并发启动。前两项主要负控和并发负控先按旧源码失败，再按修复通过；历史“无IPC的旧单实例”fixture明确使用`routingId=null`，保留原精确接管验收。`test/rustdesk_harness_share_service_test.dart`整份48项通过。定向`dart analyze`退出0，仅报告两条本次改动之外的info级提示。

**未完成的发布门禁**：这只是源码与模拟调用验收，尚无修复候选编译、Developer ID签名公证和旧723→新包在原132的真实覆盖。真实验收仍须证实原ID/公钥/授权、唯一helper进程与映射inode、原30秒gate、Safari15、房间心跳、MCP及失败回退；SERVER_ERROR服务器内部成因如继续复现要独立定位。132当前唯一混合中继不得因本次源码通过而停止或宣称恢复。
