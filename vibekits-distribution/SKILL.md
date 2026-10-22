---
name: vibekits-distribution
description: 维护和部署 VibeKits 四端下载与使用门户，核对商城版本、Linux架构、扫码入口、云端共用端口、分类文档及GitHub技能同步；不代替客户端构建、签名或商城发布。
---

# VibeKits 分发门户

先读项目 AGENTS.md、本机环境规则和当前发布回执。核对用户授权、现有服务、实际商城版本及在途部署。门户只分发现有正式包和说明，不授予设备、后台、签名或发布权限。

## 入口和源码

- 分发网站：https://kemi-chat.newlinksz.com:21122/vibekits/
- hbbv 管理后台：https://kemi-chat.newlinksz.com:21122/manage
- 客户端后台地址：https://kemi-chat.newlinksz.com:21122（不含网站路径）。
- 技能库：https://github.com/caucy2026/skills-group
- 网站规范源码在 hbbv 的 `web/vibekits/`；路由和动态商城目录在 `server/app.py`、`server/public_download_catalog.py`。按当前环境定位项目，不照搬同事本机外盘路径。

当前云端目录及无中断静态发布路线见 [部署与核验](references/deployment.md)。修改后台代码时另用 hbbv-server-build-deploy；只有静态页面变化时不重启集群服务。

## 更新下载记录

1. 读取实时 `/vibekits/downloads.json` 和官方不带类别筛选的商城列表，按平台与包名查唯一记录。Mac/Windows/Linux 为 `com.caucy.vibekits`，Android PAD 为 `com.vibekits.vibekits`。
2. 下载入口使用稳定商城分享页：`https://kemi.newlinksz.com/kd/s/{package}?os={macos|windows|linux|android}`。二维码编码同一入口，不固化每版 CDN 地址。四个平台都保留扫码入口。
3. 核版本名、整数版本码、实际架构、最低系统、字节数、SHA-256和可信 HTTPS CDN。测试候选不冒充商城发布。Linux amd64 不等于 arm64；ARM64包未实际发布时明确缺项。
4. 动态目录按访问刷新，成功缓存60秒，失败显示上次核验及时间，不启动持续后台轮询。用现有 `tool/refresh_public_download_catalog.py` 更新随源码的静态快照；不能只改网页文字或写死最新版本。
5. 核公开商城详情、CDN可获取和准确大小。完整下载hash证据来自同一正式包；HEAD只证明可获取/大小，不冒称完整校验或安装通过。

## 页面和文档

保留五张宣传图自动循环、点击图片下一张、暂停/恢复、键盘操作、窄屏布局和每端二维码。隐藏页面停止轮播；新版不破坏已有文档深链接。

`handbook.json`、15篇分类文档、`agent.json`、`llms.txt`和完整指南要相互一致。检查相对文档链接、GitHub路径、平台限制、安装/自更新、仿真/PAD远程ADB、入房和签名场景。实时工具Schema、实际授权和设备事实优先，不能将入房写成任意执行许可。

## 智能体凭管理登录接入本机

门户必须提供 agent.json/onboarding、默认用户名、serverOrigin、客户与房间、登录认证头及 accessToken 字段、精确申请审批的 applicationId/revision、激活和真实验通步骤。密码经可信登录/受保护输入提供，不放网页或脚本；默认账号存在与当前权限另核。首页复制说明和 rooms.md 必须能完整接续，不只写“等待管理员批准”。以隔离的真实 HTTP 登录→签名申请→只审批本机→激活→退出测试验证合同，不为文档核验向生产随意注册设备。

## 同步与交付

- 网站文档与 skills-group 的 `docs/`逐字一致；完整技能目录保留 scripts/references。使用 skill-creator 校验新增技能。
- 本机已安装技能与云端对应内容一起更新。只提交本任务明确路径，普通推送main并读回远端blob；不reset、force或覆盖共享脏树。
- 运行相关公共路由/目录测试、轮播行为测试；浏览器核真实版本、Linux架构、下载/二维码和文档。上线后重查正常受信HTTPS全部资源，静态SHA与清单一致，动态目录按合同核对而不比较旧JSON字节。
- 给出可分享网址、当前Linux版本/架构、主线和技能提交、实测结果及剩余限制。网站上线不等于七机升级、所有工具或商城新客户端已通过。

账号/售后说明按最新已验收规则：/account普通会员注册，/manage独立客户管理；只有admin可按customerId授予1–10级管理员。通用售后不允许凭同房成员互访，自动新装入房/多后台/万台真实在线未完成须明示；旧默认一级仅列历史。
