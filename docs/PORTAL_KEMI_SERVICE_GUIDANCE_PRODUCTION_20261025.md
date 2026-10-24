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


## 原生Chrome复验与首页补正V2

原浏览器DOM通道超时后，沿文档提供的CUA原生Chrome API核对本任务专用窗口：先见新标签页，再准确选择“VibeKits 指南验收”标签，读取真实指南弹窗并取得截图。新kemi业务房、独立newlink通用服务、普通会员及两类账号管理员/设备管理员说明均在实际页面可读，弹窗正常滚动、关闭后返回下载首页，四个平台版本/二维码入口及15篇文档可见。指南截图SHA256=6ea1ac468ee3edba50fe78ec1bc1823bac8860423f90a0ff2d957c3a58951c05，原始截图保留24小时，正式报告保留索引；没有读取管理密码或私人聊天。

原生首页复验发现两项残留文字：服务卡仍要求管理员必须有账号，未涵盖独立显式设备授权；页脚日期仍2026-10-22。另将给智能体的接手说明精确区分账号管理员任命和设备管理员授予。仅index.html文字修改，主线源码6190b5185bd4b3f7d3736e121e2c836ba1cc1819；其余28文件逐字保持。原15项HTTP/目录合同证据继续保留，受影响的公开资产与四端QR两项重验通过；两项是原15的子集，不相加成17个唯一测试。

V2第一次本地准备因缺baseline.json，在写deployment-intent与任何上传前失败；记录原exit1、上传数0，再从已经记录并核验的远端manifest恢复baseline投影，未重建/篡改原始基线。补齐输入后才进行原唯一范围事务，无未知上传/切换重放。新静态目录/opt/vibekits-distribution/releases/20261025-room-guidance-v2，原子current切换后28公开静态SHA、四端目录和原serverId/PID138154验证通过。外部控制机再读首页也匹配预期SHA，包含2026-10-25及独立授权新句，HTTP Cache-Control=no-store；未重启后台、启用自动服务或改数据库。

cloud-build-cleanup已删除V2全部6个暂存文件、61440分配字节，/opt可用152650612736→152650674176；stage、tar、激活器回读均不存在，当前正式门户和原服务保持。包含项目/门户/专属journal的总分配2723463168字节，未创建云端DB备份。

**最终首页视觉仍待前台确认：** 当前Chrome后台窗口AX能读取、地址栏编辑值可改变，但顶层window.URL没有提交到新导航，旧首页正文仍保留。正常刷新/硬刷新未作为成功证据。已向原Mac使用者协调约30秒前台窗口，未擅自Raise抢占；未读/填密码、未越过警告。指南内容在V1/V2相同，因此已取得的指南弹窗视觉结论有效；不把它扩大为V2首页、窄屏、所有交互或管理登录通过。原管理标签与新同站Chrome标签均显示登录管理台，不能继续沿用旧登录快照。

新增独立软件诊断：794正式路径build2794时本机system.info真实返回macOS26.5.2/PID77448，只证明该确定性工具和本机桥保留，未请求模型，不替代本机GUI/模型/个人协同全验收。最新只读后台Root155的原kemi binding8仍有约20198秒有效会话、个人v2 binding1无有效会话，原installation无已提交bootstrap记录；445两层均已自然到期，仅旧到期ready记录。没有已提交记录不能证明没有HTTP尝试。原恢复链继续由个人账号/手机版负责人定位，Root不替其反复登录或重发消息。

Linux新现场为cluster agent.deviceId长度0，同时原320仿真真实MCP仍可用。JOIN_REQUEST_INVALID发生在Dart发HTTP前；后端通用错误码为INVALID_JOIN_REQUEST。源码显示start单次identify空后，sync先_syncJoin而_register在后，可能形成重试环。Linux负责人保留原包，继续最小Linux-only源码/非交付合同；其101权限误替换事故已自行登记暂停资格，Root不接管其构建以绕过暂停。独立8项边界合同不代表完整agent、实际wire或新包。七台统一升级、撤销矩阵与长期/百台真实验收仍未完成。

报告发布脚本首轮把中文章节标记写成bytes字面量，Python解析阶段即拒绝，未执行Git操作；已改为明确UTF-8编码，保留首败哈希及修复回执。

新增证据目录portal-room-guidance-20261025-v2：manifest、candidate、html-contracts.log/verdict、predeploy-qualification、source-publications、local-preupload-input-failure、activation-result/receipt、cloud-cleanup-result、visual-proof-index；admin-expiry-contract-20261025-v1保留794-server-chain-current和794-local-tool-continuity。此补正没有改写先前失败或把候选发布到商城。
