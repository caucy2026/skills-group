# PAD 远程 ADB 与双屏

## 连接条件

目标是已授权的 KEMI Android PAD，主应用与必需辅助组件已正确安装，原仿真已开启且首次同意完成。仅知道 ID 不能远程开启被拒绝的权限。控制端准备官方 Android platform-tools；不把 PAD 的 5555 开到公网，不要求同一 LAN。

完整逐命令手册：https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/mac-pad-remote-adb.md

## 取得本次动态串口

调用 simulator.connect，核原 ID、可信身份、connected=true、transport=p2p_or_relay、adbReady=true。adbSerial 必须来自这一轮返回，形如 127.0.0.1:动态端口。PAD 的 sshReady=false 正常，不以此判失败。

```text
PAD_ID=<用户授权的原ID>
ADB_SERIAL=<本次connect返回的127.0.0.1:端口>
ADB_SERVER_PORT=<已确认空闲的本机ADB服务端口>
```

不要手抄历史端口或固定为 PAD IP。每次连接可能换端口。

## 使用隔离的 ADB 服务

```sh
adb -P "$ADB_SERVER_PORT" connect "$ADB_SERIAL"
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" get-state
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" shell getprop ro.product.model
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" shell getprop ro.build.version.release
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" shell dumpsys package com.vibekits.vibekits
```

get-state 必须是 device，并核预期型号、版本与设备身份。独立端口示例 5039 不是固定要求；占用时选另一个空闲端口。始终指定 -s，不能对未知默认设备操作。

## 双屏定位

先读 dumpsys display 与 dumpsys activity activities，确认真实显示屏 ID、尺寸、前台 Activity。优先使用当前目录的 ui_inspect/ui_action。不同机型不能固定 display0/display2，也不能从默认屏 uiautomator 结果推断另一屏为空。只有核当前屏坐标后才能 input -d；截图仅作必要证据，不持续采集，已知 GPU 风险固件沿原安全路线。

## 授权安装 APK

先核包名、版本、签名和原数据保护。设备暂存路径须本任务独占，先传文件、核设备 SHA 与本地一致，再执行：

```sh
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" push /absolute/candidate.apk "$REMOTE_APK"
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" shell sha256sum "$REMOTE_APK"
# 比对通过才执行：
adb -P "$ADB_SERVER_PORT" -s "$ADB_SERIAL" shell pm install -r "$REMOTE_APK"
```

禁止裸 adb install 自动选择 incremental，已有 DataLoader/eventfd 内核异常实证。不卸载、不清数据、不加降级参数。主 APK 自更新须先通过独立救援演练，不能把旧 ADB 串口或系统 UID helper 当作独立救援。

## 断流与结果未知

安装超时不等于失败。查原事务与真实包版本、pm path、base.apk SHA、实际新进程；重连时重新提取 adbSerial，再核原 ID/指纹、MCP、ADB、原 Key/会话与功能。identity_mismatch 走已验证救援，不换号掩盖。

adbReady=false 时读状态与组件错误；只剩恢复工具不等于完整 Harness。不要常规执行 adb root、su、setprop 或重启 adbd，也不全局 adb kill-server。

## 结束

```sh
adb -P "$ADB_SERVER_PORT" disconnect "$ADB_SERIAL"
```

再断开本次仿真连接，保留必要脱敏证据，只清自己无占用的暂存文件。

## 完整技能与深入阅读

- [逐命令ADB手册](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/mac-pad-remote-adb.md)
- [PAD研发与验收](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-pad-development/GUIDE.md)
