# 当前主机环境与证据定位

这是2026-10-11原开发Mac的定位信息，同事应映射自己的环境；不能把不存在的外盘写成硬性要求。

- 共享源码：`/Volumes/ORICO/newlink-new/vibekits`，dirty与其他同事工作保留；工作会话cwd `/Users/newlink/kemi/RustDesk` 不是本轮冻结PAD源码。
- RUN：`/Volumes/ORICO/kemi-build-cache/app-release-gate/vibekits/pad/resources-dev523-20261005`；下文RUN均指这个目录。
- ADB：`/Users/newlink/android-sdk/platform-tools/adb`；build-tools35.0.0。
- JDK17：`/Users/newlink/jdk/jdk-17.0.19+10/Contents/Home`。
- Flutter：`/Volumes/ORICO/kemi-build-cache/shared/flutter-sdk/bin/flutter`。
- PUB_CACHE：`/Volumes/ORICO/kemi-build-cache/vk-pad-acp-dev442-20261002/pub-cache`。
- 签名只引用既有授权安全存储：`/Users/newlink/kemi/priv/xtqx.md`、`/Users/newlink/kemi/keystore/debug.keystore`，alias androiddebugkey；绝不把内容带入文档/日志/代码。路径名称不是证明签名资格，要核certificate。
- 外部Mac桥脚本：`/Users/newlink/.codex/skills/vibekits-remote-simulator/scripts/invoke.rb`。
- main host package `com.vibekits.vibekits`；Builder `com.vibekits.vibekits.component.builder`；历史Proxy `com.caucy.vibekits.component.network_proxy`。

## 当前完整签名组件身份

|组件|版本|SHA256|
|---|---|---|
|helper|36|f583c6f38deda88f910c99d744a728b15575ec2302806ab64a1f9d4e89506714|
|H5|5|8f35e6aff9b27c97bdcc4b5c0c1d0407096cf7fe6baff88d4505047cc8ed60fb|
|H5 runtime ZIP|5|52649d0ab84a441ffa9636361f24735f1b31311d5bc341339d46f9f0fdeeaa22|
|C6|既有|c6f6d5383bf110efc0fbb2ec9177687487df45e7c0014e8914663cee1a8dfcf8|
|C8 qualification|既有|c8a2e9bccf597c2fb6dc66bee293fc13f2fc47ec77bc6b2b0d52c11f51192ab8|
|商城Builder|1.0.7/8|982dc3e54f5764f739a279acfbc76eeebb713da81b69914a753a8e6ab0b75b49|

不要以表中旧值强行替代当前要求，新资格升级须读当前源码/manifest；不得降级helper36未排空的sealed-v2在途journal给旧35。

## 证据索引

- 构建：RUN/prepare623/release_driver.py、signing/receipt.json；source623；candidates/pad63-dev623-system-signed.apk。
- 2621 H5恢复修复：reinstall-h5-restore621-candidate/production.patch。
- 2622 UI生命周期修复：pad-workspace-retention622-candidate/production.patch、before-after.json。
- 2622真实覆盖：device63-upgrade622；三轮联合卸载：device63-reinstall622-cycle1/2/3；three-cycle-proof.json在owned622-source-backup-preparation。
- 2622真实键盘开关：device63-ui622/keyboard-opening-receipt.json，实体输入未证。
- 2622真实商城组件：device63-market-builder622/market-install-receipt.json、compile-status.json、compile-events.json；原taskId见current-handoff，未知最早观察保留。
- 2623 UI修复：android-component-uninstall623-candidate/production.patch、receipt；生产两个Dart文件。
- 2623覆盖前72快照失败：device63-upgrade623/pre-cover-full-readback.private.log，0600保存；不覆盖未知保护状态。
- 读回62201：native-readback62201/FINAL.json；62301：native-readback62301/FINAL.json，当前APK未装623则不可执行623guard。
- 自身AX probe：ui-nav-probe62215，目标com.vibekits.padprobe/.ProbeInstrumentation；仅固定公有词/metadata，不导出聊天。
- 原桌面真实I/O测试等待误差：desktop-ocr-listener622-audit/test-only.patch，旧红新绿24PASS，未改产品断言。

## 已读回的云端归档

私有GitHub同事需自己已有仓库访问权限；不得分享token。

- 622选定121源码+manifest+note共123 blobs：commit `572d209a32089795b63371d10feaf143a2a5d98e`，`docs/acceptance/releases/622/PARTIAL_ACCEPTANCE.md`，完整逐blob读回receipt本地owned622-source-backup-preparation/remote-readback-receipt.json。
- 622三轮证据+测试等待patch：commit `7409e38396ee0ee3455febcf83b8da46c07db831`。
- 621归档：`6f0ccc7dd09185e8b9981e3748a70977c526c7ca`。
- 620归档：`2c6009c8511de1f6a33077185c6d392687d0f1ef`。
- 云端技能目录 `docs/skills/`；本技能在独立目录vibekits-pad-development，不覆盖release-error-preflight。

归档选择文件不等于30,037-input构建闭包完整在云端；接手Mac仍需本地冻结源/完整依赖。任何新增commit先读回再记录成功。
