# VibeKits 自动通用服务说明网站上线回执（2026-10-25）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

公开入口：https://kemi-chat.newlinksz.com:21122/vibekits/ 。同域管理入口`/manage`、个人账号`/account`、客户端serverOrigin根地址不变；无新增端口、服务或下载包。源码`priv/main bbda242ca8dee4496e31825a8d51e7114f61eb25`提交了6处静态文档/机器清单更新及生产验收说明；公开网页内容与当前后台`automaticServiceAssignmentEnabled=true`一致，同时明示全新安装首次入房、重装找回、退出恢复及万台真实在线仍未验收。

2026-10-25 14:18:48（Asia/Shanghai），公开`current`从`/opt/vibekits-distribution/releases/20261025-phone-guidance-v1`原子切换到`/opt/vibekits-distribution/releases/20261025-service-auto-guidance-v1`。修改资源仅`agent.json`、`docs/installation.md`、`docs/rooms.md`、`guide.md`、`index.html`和`llms.txt`；全29个静态文件与冻结清单逐项SHA匹配，动态`downloads.json`仍有macOS/Windows/Linux/Android四端，未改商城版本或扫码入口。独立受信HTTPS再次核6个修改资源、机器清单字段`observedExistingClientResolves=4`和`finalFreshInstallAndReinstallAcceptanceComplete=false`，后台PID2689633、serverId`da3553a32048bfe691d99ad1a27a914b`不变；旧门户release保留回退。

首次静态激活在复制/切链接前因清单`servicePid`整数与既有脚本字符串比较而误报`SERVICE_CHANGED`。当次立即对账确认实际PID未变、旧current未变、新release不存在且只有自有stage解包；精确核7个暂存文件与两个上传文件后清理并回读不存在。新清单将PID改为字符串，重新冻结为r2并在同一正式候选目标上单次成功。未盲目重放未知切换，未覆盖现有运行服务；网页预检错误没有造成线上短暂空窗。r2终态后再清云端自有11个暂存文件、已分配196608字节；hbbv+门户+专属journal合计2730049536字节，低于3GB，无云端数据库备份。

`skills-group/main b42dd69ea3346f15286805200694e03a52b08ec2`同步了与网页逐字一致的15篇分类文档中本次变化的房间/安装说明、完整自动服务生产验收、通用服务操作技能及分发技能；修正原技能错误的`newlink`业务默认客户/旧售后房名/人工审批路线。GitHub远端blob和本机已安装两项技能逐字节读回，`skill-creator/quick_validate.py`双技能PASS。测试：本地当前源码`test_public_download_site`7项、`test_service_auto_assignment`17项通过，发布后公开静态和动态目录读回通过。

边界：静态文档与后台能力上线不等于全新设备实际安装、同账号全链路、七台统一最新版或G01–G10全部完成；Mac132旧包只提供售后可见数而不公开新版逐ID工具。浏览器可视化复验受本会话浏览器接口禁用限制，本轮以公共路由/合同、上一版未改布局和全部静态SHA为证据，不声称新截图验收。

本地私有回执位于`/Volumes/ORICO/kemi-build-cache/app-release-gate/hbbv/hbbv-main-deploy-20261024-v1/portal-service-auto-production-20261025-v1/`：冻结manifest、r1失败及对账/清理、r2激活回执、公共独立读回、云端清理结果；无密码、token或客户文件正文。
