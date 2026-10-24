# 分发门户业务/服务与权限指南更新实证

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2
日期：2026-10-25，Asia/Shanghai。

公开入口：https://kemi-chat.newlinksz.com:21122/vibekits/?doc=rooms 。原HTTPS21122共用端口不变。

## 修正内容

旧公开指南仍把业务默认customer写为newlink、服务房名写为vibekits通用售后，完整指南内还残留“初始为一级管理员”及“只有admin能设置房间管理员”的旧说法。本次统一7个公开资源：rooms、installation、guide、agent.json、llms.txt、index.html与handbook.json。

现接入业务客户kemi及kemi 通用测试房c0985cc4dfeedaf71515ae029fc4cc4f；独立newlink服务关系的当前第一槽为通用服务1/f450c684b868292f67c534b793e26314，不让智能体把所有设备硬编码入第一槽。服务普通成员彼此隔离、仅当前有效设备管理员维护；普通业务房保留原成员协作。规划8槽/每槽10000台与原身份找回、用户退出决定写明为政策与待验边界。真实service-info当前automaticServiceAssignmentEnabled=false、serviceRoomMemberLimit=10000，未为文档开启自动接入。

普通注册是会员；内置admin任命账号客户/通用管理员，获授权客户/通用管理员可在自己等级内设置房间设备管理员，0撤销显式来源。当前客户登录、原安装/Native身份及授权修订共同验证继承；个人协同短凭据与独立设备授权到期分别核对。同步31项继承到期合同与负控说明，未把其称作真实GUI/票据撤销或794恢复通过。产品当前一设备一个服务Origin、同Origin多个获授权房间，未宣传多域名同时在线。

## 源码与测试

hbbv源码main 22039c53e06a3fe0982e9fa620094357de9edcab；skills-group分类文档main 0d0037b20c61afba27714a462aba8ea445026306，两篇修改的分类文档逐字一致。全局集群技能admin-role-model到期说明另在skills-group main fffe835cb52fde0c697c443c314addc90e451d39，保持完整技能目录。

既有公开站点/目录15个唯一HTTP合同全过，零skip/FAIL/ERROR，进程exit0。含真实隔离管理登录→按新kemi上下文创建房间→原身份签名申请→只审批指定设备→激活/退出、普通会员管理隔离、私有路径拒绝、15文档路由、四端二维码、五张安全SVG，以及动态商城刷新/失败回退/单飞。未改site.js、二维码生成器、CSS或宣传图；旧完整指南的受保护目录“尚未上线”说明保留。公共页面验证不授予设备权限或改生产数据。

## 静态发布与外网实测

原目录20261024-protected-directory-docs-v1的29文件逐个SHA确认与本地一致，再冻结7文件覆盖，其余字节保持。最终归档SHA256 aa39d7dc27af000608c9630b0782818117eebbefd1b6b2805c1c88a96e2a378c，激活器SHA256 38c2d7408c81e3f3387faa1582d73efd6f2dc48e4569a5192045f532270e44bc。沿既定原子current符号链接切到/opt/vibekits-distribution/releases/20261025-room-guidance-v1，保留上一完整门户可回退。hbbv外部门户链接、运行源码、DB和账号配置不变，未重启服务。

服务器核验28静态公开资源SHA，外部控制机再经受信HTTPS、无代理/拒绝重定向独立读取28项全一致；动态downloads.json不与旧静态快照比字节，而核当前四端目录和checkedAt。原serverId=da3553a32048bfe691d99ad1a27a914b，PID138154保持，管理根200。

|平台|本轮实际商城目录版本|整数版本码|状态|
|---|---|---:|---|
|macos|1.9.0-dev.732|2732|current|
|windows|1.9.0-dev.732|2732|current|
|linux|1.9.0-dev.684|2684|current|
|android|1.9.0-dev.665|2665|current|

这些是本轮目录实收，不代表重新下载二进制/安装验收，也未把794或Linux756候选冒充商城已发布。原IAB浏览器公开页面DOM读取仍超时，未获得可用截图；本轮最终浏览器交互/视觉核验保留未通过，不用HTTP哈希冒充界面通过。

## 清理及剩余目标

执行cloud-build-cleanup：原静态事务终态后，核current/运行PID/29文件完整、精确目录文件集合、无/proc cwd/exe/fd引用；逐文件inode/SHA核验后删除本任务12个临时传输/覆盖副本、manifest及回执复制件，共208896分配字节，前后/opt可用152691421184→152691630080，回读stage、tar与激活器均不存在。正式新门户及上一门户、原hbbv服务/venv/DB/密钥、本地证据保留，未创建云端数据库备份。项目、门户及专属journal合计2723110912字节，低于3000000000字节。

原794冷启动协同、Linux房间JOIN_REQUEST_INVALID、正式舰队升级与撤销矩阵、长期和百台真实验收仍未完成。本文是公开指南及静态交付的有限结论，不是G01–G10整体验收通过。

证据索引：hbbv-main-deploy-20261024-v1/portal-room-guidance-20261025-v1下baseline、service-policy-public、source-changes、public-contracts.log/verdict、candidate、manifest、predeploy-qualification、source-publications、deployment-intent、activation-result/receipt、external-public-verification、cloud-cleanup-intent/result。本地原源码与必要证据保留，云端复制件已清。
