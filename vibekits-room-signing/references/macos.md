# 使用房间 Mac 签名与公证能力

## 找到合适节点

加入指定房间后，从当前成员能力与验证证据发现具备 Xcode、项目 Developer ID、Keychain 和公证资格的 Mac。核原仿真身份、实际平台/架构、系统版本、磁盘、负载及签名权限。管理员维护可用设备清单，公开网页不发布私钥、Keychain密码、Apple账号或私有设备清单。

Developer ID 直发、公证 ZIP/DMG、Mac App Store 是不同渠道；本手册的直发流程不能当作 App Store 已提交。App Store 使用对应独立发布技能与账号授权。

## 完整合同与材料

写清项目、源码 commit/锁、版本、CPU架构、最低macOS、Bundle ID、签名团队/完整指定要求、entitlements/helper身份、精确输入 SHA、分发渠道、回滚和验收。另一个 App 不能复用 VibeKits 的 Bundle ID、helper身份或已授权凭据标识。

冻结源码和可再生输出按该节点本机规则放置；不要在共享脏树运行 pub get、升级依赖或覆盖别人的生成状态。同一工作区只一个构建。先核当前忙碌会话、构建/公证/升级进程与实际SDK工作，未知不强停。

## 使用已有签名能力

1. 凭有效房间任务/唯一分配/本机 grant/operation permit，或明确同范围授权，连接原节点并读取实际 catalog。
2. 在独立目录暂存输入、核哈希与来源；复用该项目已批准的构建和签名脚本、现有签名身份与公证 profile。不要把证书、P12、私钥、Apple密码或公证凭据导出给请求方。
3. 编译完整同源 Release。Universal 要分别验证 arm64/x86_64 及最低系统；不混不同版本的可执行文件、Flutter AOT或资源。
4. 内层 Mach-O、原生插件、helper、framework 在外层 App 之前签。权限与指定要求来自项目合同，不盲用 ad-hoc 或通用 --deep 签名掩盖顺序/身份错误。
5. 核旧安装与候选 Bundle ID、Team、完整指定要求、entitlements、helper和凭据标识一致。Keychain被锁或系统要求本人认证时由设备持有人在系统窗口完成，不在聊天发送密码。

## 公证与最终包

使用节点现有获批准 profile 提交一次精确归档，保存 submissionId。观察超时先查同一 ID；In Progress 继续跟踪，不能重复提交。Accepted 后 staple，再生成最终标准分发 ZIP。

```sh
codesign --verify --deep --strict --all-architectures "<完整候选App路径>"
xcrun stapler validate "<完整候选App路径>"
spctl --assess --type execute --verbose=2 "<完整候选App路径>"
```

这些是只读核验示例，路径必须来自本次真实候选。项目最终更新 ZIP 使用既定单 App 根检查，排除 __MACOSX 等接收端拒绝条目。独立解压后再次核签名、票据、Gatekeeper、实际版本和架构；记录精确字节与 SHA。

## 同签名覆盖验收

先准备完整新包和可回滚旧包，再短时正常退出原App与原路径完整替换。不能合并复制签名App。升级后核真实新PID、原ID/原指纹、旧Key/登录/系统权限、工作区/会话、真实模型与只读工具、房间新心跳。首次点击/中文输入/粘贴、旧系统兼容、CPU/RSS与helper释放按项目门禁验收。

签名、公证、CLI help、进程存在或目录数量不等于应用可用。正式上传和商城/商店发布仍需独立授权与完整发布门禁。完成后只关闭本任务不再使用的连接/临时进程，保留来源、证据、正式包与必要回滚。

## 完整技能与深入阅读

- [房间签名能力](https://github.com/caucy2026/skills-group/blob/main/vibekits-room-signing/SKILL.md)
- [签名与覆盖门禁](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-fleet-compatibility/GUIDE.md)
- [Mac原子更新经验](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/remote-macos-overwrite.md)
