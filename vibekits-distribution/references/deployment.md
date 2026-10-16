# 云端同级目录、共用端口

2026-10-16部署结构：hbbv位于`/opt/vibekits-group`，分发网站位于同级`/opt/vibekits-distribution`。两者由现有`vibekits-cluster.service`在同一HTTPS21122提供服务：根路径是管理后台，`/vibekits/`是公开分发门户。不新增listener、UDP、防火墙或另一个Web服务。

分发文件存放在`/opt/vibekits-distribution/releases/<release>/`，`current`指向当前完整版本。hbbv实际工作目录的`web/vibekits`指向该`current`，现有精确公开路由读取这些文件。后台源码、数据目录、SQLite、服务UUID、签名私钥与账号保持原处；不得把数据或凭据拷入公开目录。

## 静态发布

1. 用已保存、获授权的VibeKits SSH/SFTP服务器profile核对主机指纹、当前工作目录、PID、真实链接目标和部署归属。新环境先发现，不能复制旧凭据。
2. 冻结整个`web/vibekits/`文件集合和逐文件SHA，核旧线上集合与预期基线一致。只上传无秘密静态文件与清单，拒绝绝对路径、`..`、外部链接和未知文件。
3. 上传唯一新release，校验每个文件、权限和目录完整性后，原子切换`current`；保留原目标可回退。首次把旧目录改成链接时使用已验证的Linux原子目录/链接交换，先记录意图与旧集合，不能先删旧目录造成空窗。
4. 静态变化不重启服务。核原PID不变、管理根页面仍可获取、公开资源SHA一致、动态四平台目录有效。失败恢复原链接目标；结果未知先读同一事务回执，不重复切换。

后端路由或目录读取器改变时，按hbbv服务器部署技能执行完整回归、原身份/数据库备份、活动租约核对和一次正常切换；不要把静态文件更新当Python模块重载。

## 当前Linux正式包快照

Linux 1.9.0-dev.684 / 2684，amd64 DEB，278567024字节，SHA-256 `b8e0ed0739c2e5ee62ab81345522d8b8578d81b7f48f1803cd0c13ec6cc954d2`。面向Ubuntu20.04 x86_64；不是ARM64包。此为日期快照，后续仍读实时商城目录。

稳定入口：https://kemi.newlinksz.com/kd/s/com.caucy.vibekits?os=linux
