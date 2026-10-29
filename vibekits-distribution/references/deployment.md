# 云端同级目录、共用端口

2026-10-16部署结构：hbbv位于`/opt/vibekits-group`，分发网站位于同级`/opt/vibekits-distribution`。两者由现有`vibekits-cluster.service`在同一HTTPS21122提供服务：/manage是管理后台，根路径及/account是个人账号，`/vibekits/`是公开分发门户。不新增listener、UDP、防火墙或另一个Web服务。

分发文件存放在`/opt/vibekits-distribution/releases/<release>/`，`current`指向当前完整版本。hbbv实际工作目录的`web/vibekits`指向该`current`，现有精确公开路由读取这些文件。后台源码、数据目录、SQLite、服务UUID、签名私钥与账号保持原处；不得把数据或凭据拷入公开目录。

## 静态发布

1. 用已保存、获授权的VibeKits SSH/SFTP服务器profile核对主机指纹、当前工作目录、PID、真实链接目标和部署归属。新环境先发现，不能复制旧凭据。
2. 冻结整个`web/vibekits/`文件集合和逐文件SHA，核旧线上集合与预期基线一致。只上传无秘密静态文件与清单，拒绝绝对路径、`..`、外部链接和未知文件。
3. 上传唯一新release，校验每个文件、权限和目录完整性后，原子切换`current`；保留原目标可回退。首次把旧目录改成链接时使用已验证的Linux原子目录/链接交换，先记录意图与旧集合，不能先删旧目录造成空窗。
4. 静态变化不重启服务。核原PID不变、管理根页面仍可获取、公开资源SHA一致、动态四平台目录有效。失败恢复原链接目标；结果未知先读同一事务回执，不重复切换。

公网逐文件验收按后端精确路由映射：源码`index.html`对应公开`/vibekits/`，**不是**`/vibekits/index.html`（当前后端白名单未开放该直链，直接请求返回401）；源码`downloads.json`是回退快照，公开同路径由实时商城目录生成，须按版本/平台/包名/SHA合同单独比较，不能要求与快照字节相等。其余静态文件按公开URL逐件比SHA。2026-10-29实际基线为28项静态中25项与待发布主线相同，差异仅`docs/installation.md`、`site.js`、`style.css`；该数字是切换前快照，后续需重新读取，不可当固定发布清单。

后端路由或目录读取器改变时，按hbbv服务器部署技能执行完整回归、原身份/数据库备份、活动租约核对和一次正常切换；不要把静态文件更新当Python模块重载。

以后创建新的hbbv后端release时，保留`web/vibekits -> /opt/vibekits-distribution/current`这个受管理链接，再核全部公开资源；普通copytree默认解引用可能把门户复制回后端，造成后续版本与目录脱节。链接目标只由已授权部署者设置，不从HTTP参数选择路径。

## 当前Linux正式包快照

Linux 1.9.0-dev.684 / 2684，amd64 DEB，278567024字节，SHA-256 `b8e0ed0739c2e5ee62ab81345522d8b8578d81b7f48f1803cd0c13ec6cc954d2`。面向Ubuntu20.04 x86_64；不是ARM64包。此为日期快照，后续仍读实时商城目录。

稳定入口：https://kemi.newlinksz.com/kd/s/com.caucy.vibekits?os=linux

## 注册与十级管理文档维护（2026-10-20）

首页按注册个人账号→权限分配→本机入房→仿真组织。注册/安装写入现有docs/installation.md，等级规则写入docs/rooms.md及simulation.md；首页access-levels说明四个独立维度、同低级规则和高级审批，十级表默认折叠。

保持原15个文档ID与公开路由，不为文档别名伪造不存在的raw路径。机器清单的新注册入口放onboarding.registration.guide，分级入口放accessPolicy.webGuide；documentation的键继续与handbook文档ID一一对应。客户端账号按实际候选及正式版本标明验收边界，不把浏览器登录当设备绑定。完整账号设备规则同步cluster-operations/references/account-device-levels.md及公开验收文档，禁止把“没有网页注册”的旧说明继续发布。

## 2026-10-25 通用服务状态与静态发布

后端同一正式release仅开启现有 `--enable-auto-service`，公网 service-info 实测 `automaticServiceAssignmentEnabled=true`、每槽10000台；4台既有真实设备签名resolve且原设备token/epoch/owner未变。新装、重装、退房恢复和万台真实在线仍需实机验收。公开门户当前release `20261025-service-auto-guidance-v1` 在同一HTTPS端口静态切换，后台PID2689633未重启；公开资源哈希读回通过，旧portal release保留回退。以后仍以实时 `current`、服务接口和商城目录为准。

只改静态内容时沿原current链接原子切换，保服务PID、身份和动态商城目录；不把源码或桌面测试候选版本写成商城已发布版本。
