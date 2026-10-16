# 源码、硬件能力和开发方法

## 从实际资源泛化客户需求

用户举查询 IP、风扇、音量、动漫等只是例子，不应针对一个词硬编码。Harness 先发现实际系统版本、硬件、系统权限、已装应用、工具目录和组件，再选工具，执行后读回；缺能力说明具体缺口并沿已有受信组件路线解决。基础硬件能力由每个会话继承，不依赖“硬件通用窗口”。首次默认会话名称“欢迎使用vibekits”；用户可在任何会话提出任务。

PAD Harness 需要可创造工具：先寻找兼容开源项目及许可、真实源码和工具链，再本机复用编译；有成熟项目不重复造轮子。Builder 必须先 status/buildReady；商城安装查原 operationId 到真实 PM 版本和 APK hash；源码在私有 workspace；build 单次提交，用原 taskId 查询 verified=true；任务要求安装/运行时再走真实系统安装核验和另一屏运行。控制端代编译或临时桥不能冒称 PAD 本机编译。

## 关键源码入口（相对冻结源码）

|功能|文件/目录|
|---|---|
|工具Schema、异步operation回执、调用|lib/features/dev_tools/domain/harness_tool_bridge.dart|
|命令路由、会话记录|harness_command_broker.dart（同domain）|
|模型规则与执行|deepseek_harness_service.dart、harness_official_acp_runner.dart|
|真实对话UI、Key读写、任务history|lib/features/local_models/presentation/deepseek_agent_workspace.dart|
|父界面身份、目录变化|lib/features/main_shell/presentation 下 MainShell；lib/features/local_models/presentation/local_models_tab.dart；用rg定位当前文件|
|组件商城目录/安装UI|lib/features/app_center/domain/app_center_service.dart、presentation/app_center_tab.dart|
|快照、恢复、资格、Native读回|rg PadHostSnapshotRestore/PadHostSnapshotSdkProbe/PadHostSnapshotRecovery；android/app/src/main/kotlin/com/vibekits/vibekits/Pad*Snapshot*|
|发布约定|tool/pad_release_incident_matrix.json、tool/check_release_error_preflight.py、tool/check_pad_embedded_helper.py|

只读实际方法与调用者，不依据文件名猜根因。固定输入/触发→源码因果→原红/故障注入→最小修复→新绿→最终 APK 真实动作。真实I/O测试须有界runAsync等待文件写入，fake clock推进不能替代真实写完成；保留原功能断言。

## UI与状态需求

开机恢复、系统权限与通知实现读 [开机恢复与静默服务](boot-service.md)，区分静默前台通知和严格零通知，复用既有源码方法。

- 智能体/OCR顶级切换取消；OCR移开发工具，MAC/Windows相关UI保持一致。
- 远程状态占顶部空白处一个按钮，点击弹窗；本机ID只出现一次，仿真/传输/服务器状态详细均匀布局，服务器有指示灯。
- 服务器在线必须基于实际连接证据；“可达”不等于“注册”或“通道可调用”。PAD展示ADB，电脑展示SSHD，不能跨平台混用。
- 一个动作一个动画，忙状态有真实事务和终态；不重复占空间。白/黑名单默认折叠。推理详情空白处长按2秒折叠，折叠后可见按钮可再展开。
- PAD开发工具搜索点击应弹实际IME；AX焦点、真实IME显示/关闭、实体输入分别验收，adb input text不是实体键盘输入证据。
- 双屏：智能体自身主屏，其他应用按实际需求另一屏；63当前副屏保护/GPU禁令是测试设施限制，不是取消产品双屏目标。

## 身份、认证、Key

PAD稳定ID依据真实WiFi工厂MAC后4byte算法及明确版本，不随机；不改其他端算法。当前计算ID、算法版本、身份scope、最后真实注册成功记录分开保存。ID/算法明确变化执行一次持久阶段迁移，仅清旧设备绑定认证/配置；pending或重启不得反复删新身份。未知旧版本标unknown，断网/超时不是服务器拒绝。

覆盖升级保原认证身份与授权。普通卸载主APK删除传输认证及helper身份副本；同硬件ID按用户要求保配置、模型Key、会话，重装走新设备认证；ID变化清旧绑定，进入可操作界面，必要重新输入Key。新Key覆盖旧值，旧备份不覆盖用户新编辑。必须用真实Key调用确认，不能只看设置不空。

启动进入可操作UI，检查后台执行。注册失败有截止、终态及明确人工重试，STATUS和页面轮询只读，不复活服务或重置截止。打开仿真不再弹密码，白名单确认仍真实强制。系统权限自动ADB必须复用native既有路线，并验证开关与重启真实通道，不能仅改灯。

## 数据恢复约束和已证修复

- H5缺失恢复死锁：Main+H5联合卸载后旧实现SdkProbe=null→sdk_layout_unknown。2621缺组件时调用既有可信内置prepare，再重新严格核布局；不跳验证、不改SDK。仅helper保险库保留，不等于出厂新机通过。
- PAD父Key变化导致State dispose，stop有效任务及丢内存requestId，磁盘SID仍在。2622固定PAD界面身份，目录更新给后续任务；迟到OCR结果/失败丢弃。实际现场具体触发尚未证实，不编造唯一原因。
- 旧code_cache spill正常覆盖可能丢失。先保存并独立字节验证后覆盖，不以Key/聊天通过替代。
- 完整快照含SDK、前端会话、绑定workspace、严格taskId的buildAPK和spill；线包AEAD+每文件+实际live字节+修订一致。liveMatchesSnapshot=false必须保留并定位，不能凭coverageComplete升级PASS。
- 回收helper上传必须认证后清理；当前/前代/可提交/未知保留，旧v1兼容，失败CAS/中途退出原事务恢复。有界上下文不等于存储有界。

## Actual open-source compile regression (2026-10-12)

AOSP HelloActivity pinned commit88f7870b2c652922dc2afb01c076737e8bc50130,4raw files, was fetched ON PAD through network.download, each exact byte/SHA independently recalculated. Preserve Apache2 headers, change only project paths/package namespace. Controller copies only verify provenance and do not prove PAD fetch capability.

Controlled missing strings first native task pad1791731919275000 really failed resources; repair copied exact original769B strings. New task pad1791733065544000 passed resources but failed javac missing org.xmlpull.v1.XmlPullParser. This is a real v8 component defect, not successful compilation. Device core-libart.jar defines public XmlPullParser/Exception and JSONObject; generator only framework.jar omitted other boot inputs. Cache only ROM fingerprint also masks upgrades. Do not rewrite sample to avoid inflate or insert fake platform stubs.

Owned Builder9 candidate fixes actual trusted bootclasspath conversion/orderedmerge, algorithm+input/output SHA cache, fresh staged activation, bounded own cleanup and actual LayoutInflater smoke. Five local regressions pass; full build/device/runtime and release remain separate. Source623/shared main untouched; official SDK/H5/C6/server untouched. User whole PAD component scope covers own Builder; earlier no-Builder edits was a stage boundary, not a sourced lifetime prohibition.

Runtime contract remains Java8 app/src/main, no Gradle/dependency resolution/invokedynamic desugaring; generated development APK does not inherit host system permissions.


### Builder修复路线的实际结论

Builder9逐个boot jar转换、Builder10单JVM多输入转换均真实超时，固定120秒截止未放宽。Builder11改为复用设备API对应完整官方公共编译接口，严格输入SHA及缓存版本，避免把全ROM转换当启动必要工作。原AOSP inflate调用不改、不塞假平台类；实际资源仍来自设备framework-res。Java编译classpath不是APK运行时依赖，平台stub不得打进生成APK；开发签名和系统权限分开。

API31–36公共jar按SDK_INT选择，其他版本保留旧路线且未验证。每个jar原始NOTICE/许可须逐项确认；SDK总协议不等于所有组件许可相同。Builder11真机成功不代表任意GitHub Gradle/Kotlin/JNI项目可直接构建。先匹配当前Java8/Manifest/res契约；缺dependency resolution必须明确缺能力，不能假装已执行。
