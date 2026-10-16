# 开机恢复与静默服务

排查开机恢复、后台仿真或通知时读取本页。原详细方法在项目 `docs/acceptance/PAD_BOOT_SIMULATOR_SILENT_SERVICE_REFERENCE_20261010.md`；其中2611的实机读数是历史证据，不能当作624重新启动验收。

## 624源码的实际路线

1. 主清单声明 `RECEIVE_BOOT_COMPLETED`；`PadSimulatorBootReceiver`接收 `BOOT_COMPLETED` 和 `MY_PACKAGE_REPLACED`。
2. 在发布/恢复锁下读取原 `simulator_service.enabled`，关闭时返回，不重新开启或创建身份。
3. Android26+调用 `startForegroundService`，旧系统调用 `startService`；内部动作是 `HarnessRelayService.KEEP_ALIVE`。Receiver与Relay位于 `:vibekits_harness`，不是Flutter页面。
4. Relay使用低优先级、固定ID的静默前台服务通知，不因心跳创建新通知；原生初始化受身份恢复和发布锁保护。
5. system UID助手 `RemoteAdbBootReceiver` 按已保存意图执行有限异步ADB恢复。助手UID、签名和真实资格必须独立核，不把主程序的签名等同于system UID。

“没有弹窗/声音/抢屏”与“未向系统提交通知”是两个结果。当前成熟路线仍提交前台服务通知；沉浸界面隐藏状态栏不等于零通知。不删除通知或停止视频流冒称满足用户要求。

## 复验方法

- 真正重启后读取广播、Relay新PID/初始化阶段、真实注册和原ID仿真工具/动态ADB；不能先人工启动Activity再称开机自动恢复通过。
- 分别验证原开启意图恢复、原关闭意图不启动、离线有界终态、恢复联网后可继续；普通STATUS只读、不重启服务或重置注册截止。
- 核固定通知ID/channel、无声音/振动/启动弹窗、主副屏未抢占，以及至少三轮生命周期；服务存活不等于模型目录或真实任务可用。
- 严格零通知需要ROM认可的系统后台宿主或系统服务集成，必须真实验证。不能仅凭平台签名、manifest persistent或UID数字保证。当前授权仅PAD时不擅改ROM、服务器或系统白名单。
- D18的视频默认开启与通知要求单独验收。63有GPU故障历史，不为补视频证据抓图或启动流；75明确离线时不连接。设施限制不能取消产品目标或写PASS。

## 代码定位

`android/app/src/main/AndroidManifest.xml`、`PadSimulatorBootReceiver.kt`、`HarnessRelayService.kt`、`RemoteAdbBootstrap.kt`；助手 `android/adb_helper/src/main/java/com/vibekits/vibekits/component/adb/RemoteAdbBootReceiver.java`。Main与助手不得相互加载执行代码造成升级连带杀进程；沿W60已有隔离与原事务恢复门禁。
