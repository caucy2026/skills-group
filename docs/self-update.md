# 自更新、覆盖与回滚

## 使用客户端自更新

在应用中心检查同平台商城版本。比较整数 versionCode；已是当前或更高版本时不重复安装、不降级。下载完整正式包，校验精确大小、SHA-256、应用身份和签名，保留旧完整包与恢复入口。

覆盖升级必须延续原 Bundle ID/包名、签名团队与指定要求、entitlements、helper 身份和凭据标识。系统权限开关存在不代表新包确实继承，必须用真实功能复验。不要通过卸载、清钥匙串、重置 TCC、删除配置或要求重新登录掩盖打包错误。

## 智能体远程更新

1. 连接用户授权的原 ID，核主机、指纹、实际版本、路径、空间和当前工作。实际 Harness 会话、持久队列与在途构建/签名都要对账，不能仅靠旧队列目录不存在判空闲。
2. 查询当前工具目录与 update_stage/update_apply/update_status 的真实 Schema；旧客户端可能不支持。房间业务任务还须有效合同、唯一实例/租约、本地 grant 与 operation permit。
3. 暂存唯一候选并核大小/哈希/签名，准备完整回滚，再正常退出精确原实例。更新器必须在旧 App 退出后仍活着；Windows 的 detached 标记不能证明脱离 Job。
4. scheduled、staged、安装器 exit0 都不是完成。新进程起来后以原 ID、原指纹重连，核版本/路径/PID、真实只读工具、旧 Key/登录/权限、房间角色和新鲜心跳。
5. 失败回滚原完整包；结果未知查原 attemptId、PID/出生时间、日志和回执，不重启第二个安装事务。

## 平台重点

- Mac：最终更新 ZIP 必须只有一个 App 根；公证提交 ZIP 与最终分发 ZIP 分开。使用项目严格归档检查，签名、公证 Accepted、staple、Gatekeeper 及解压后复验都需同一最终 SHA。
- Windows：完整同源 Release，自有 PE 内层签完再制作并签外壳；官方 CRT 与原厂文件按项目检查。守护、安装器、注册信息和原路径要能恢复；不要混新 AOT 与旧 EXE/DLL。
- PAD：如果主 APK 承载唯一 ADB/仿真通道，必须先验证独立救援通道在主进程停止后仍可联系原设备、读取身份并恢复，且同签旧包本地可用。没有救援证明就不远程覆盖宿主。先传 APK、核哈希，再 pm install；禁止裸 adb install 的增量路径。

## 同步网页版本

网页目录按访问向商城公开接口核对，成功缓存最多约一分钟；商城正式变更后再次打开或点“同步商城”可读取更新。失败显示上次核验时间，不能称最新。商城分享页是稳定入口，CDN 下载地址、版本、大小与哈希来自对应平台的当前记录，不按版本号拼 URL。

## 完成证据

记录原 ID、旧/新版本、安装事务、候选 SHA、签名身份、实际进程、真实调用、房间心跳和回滚位置。不把另一个版本的测试结果借给新包。

## 完整技能与深入阅读

- [仿真商城更新](https://github.com/caucy2026/skills-group/blob/main/vibekits-remote-simulator/references/market-app-update.md)
- [真实升级兼容](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-fleet-compatibility/GUIDE.md)
- [历史错误门禁](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-release-error-preflight/GUIDE.md)
