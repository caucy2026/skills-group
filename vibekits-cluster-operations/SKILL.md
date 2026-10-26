---
name: vibekits-cluster-operations
description: 操作和管理 VibeKits 集群：远程仿真、管理后台、客户与管理员、房间创建和审批、设备入群、成员通信、能力同步、任务协作、监控、升级及调试清理。适用于同事完整接手集群运维或开发。
---

# VibeKits 集群操作与管理

本技能是完整接手入口。先读取当前环境 AGENTS.md 和 LOCAL-ENVIRONMENT-RULES.md，核验用户授权、当前设备/服务和在途事务。技能内容不授予新账号、新设备或发布权限；已有同范围授权直接执行，不重复确认。不要把旧快照当实时状态。

接续原七台 G01–G10 整体验收时，再读[当前完整目标与最新追加台账](https://github.com/caucy2026/priv/blob/main/hbbv/docs/PROJECT_HANDOFF_VIBEKITS_CLUSTER_UPGRADE_ACCEPTANCE_20261011.md)的**末尾最新回执**，按每项真实证据与未完成门禁继续；上方历史瞬时PID/版本不是现状，局部通过不缩小全七台、签名覆盖、撤销及100台真实扩展目标。


首次安装、同站后台地址、四端商城入口和完整从零接入流程，先读 [从零到集群协作](references/getting-started.md)。公开网站：https://kemi-chat.newlinksz.com:21122/vibekits/ 。Linux未有公开正式包时明确待上架，不混用平台。

只拿到分享网址和后台管理密码、要把当前本机入房时，先读 [智能体入房执行单](references/onboarding.md)：自行发现本机原 ID，使用本团队默认接入参数，申请一次，再通过管理登录精确审批、激活及验通。密码只在可信登录或受保护输入中提供。

当前生产的kemi业务房、newlink通用服务、历史重复房退休及既有设备迁移，先读 [Kemi业务与通用服务迁移](references/kemi-service-migration.md)。旧接入文档中的newlink业务默认值仅作历史，不直接覆盖现有配置。当前业务默认客户为kemi；newlink是独立通用服务父系，服务端自动分配已启用，但全新安装首入、重装和退房恢复仍待实机验收。

## 选择操作

- 产品机制、异地能力共享与 PAD 远程 ADB 的边界：读 [产品机制与场景](references/product-overview.md)，再按下列实际操作流程执行。

- 首次接手、环境和连接：读 [连接与身份](references/connect.md)。外部 Mac 控制端附有可用桥接脚本；Harness 内优先原生 MCP。
- 网页、创建客户/账号/管理员、房间、审批：读 [后台完整操作](references/management.md)。先读[账号与设备管理员模型](references/admin-role-model.md)，区分通用管理员、客户管理员和房间设备管理员，再按当前等级与作用范围执行。
- Phone作为同账号远程操作界面、需把原生路由接入旧peer/1时，读[手机原生票据与点对点协同](references/phone-native-peer-control.md)。手机没有房间或Host权限，后端能力开启不等于真机业务已通。
- 设备入群、互相仿真、退房、撤销和同步：读 [入房与通信](references/rooms.md)。申请、批准、激活、在线、工具验通是不同状态。
- 能力声明、任务竞标、唯一分配、消息和验收：读 [协作](references/collaboration.md)。成员资格不是业务执行许可。
- 模型unknown、显式复验与不依赖目标模型的工具资源：读[模型证明与房间资源](references/model-proof-and-tool-resources.md)，区分证明时效、配置存在、工具可用及业务租约。
- 断联、系统权限、监控、升级、清理和源码同步：读 [运维与验收](references/operations.md)。先对账未知结果，不重放升级、签名和外部操作。
- hbbv服务器交付和只落本地的数据库备份：使用[hbbv服务器交付技能](../hbbv-server-build-deploy/SKILL.md)，按其一致性快照、三份保留和云端清理流程执行。
- 查精确参数、平台路线、历史故障：读 [随包资料索引](references/library.md)。仅加载当前动作需要的资料。
- 了解本项目：读 [部署入口及快照边界](references/environment.md)。换环境重新映射路径，不能复制旧设备凭据。

旧任务已终审却未退役、Native8管道、构建守护回执缺失或共享Mac忙碌等待时，读 [终态与原生恢复](references/terminal-native-recovery.md)。

## 必须保留的边界

原仿真 ID、安装身份、签名、账号/Key、设备信任、系统授权和用户业务数据保持连续。后台身份、房间角色、仿真授权、任务执行租约分别验证。不得靠清数据、换包名、复制私钥、写数据库审批或临时白名单绕过房间协议来凑通过。密码和硬件 PIN 由本人在设备窗口输入，不进入聊天/Git。

查询当前工具目录和服务端合同后执行。随包历史指南可能早于当前版本；当前已注册 Schema、实时权限和生产证据优先，发现不一致先读取源码/版本确认，不能猜接口或扩大权限。普通协作房成员通信使用room-members；通用售后房按support/default标记仅允许有效设备管理员（账号继承或房间显式授权），按新版角色模型核验。历史“五个诊断工具”范围不代表当前完整仿真验收。

售后房隐私需分**目录投影**与**实际仿真授权**验收：普通成员从真实`room_devices`只应看到管理员，不应看到其他客户普通设备；发起普通→普通房间连接还要区分账号绑定前置拒绝和最终support管理员角色拒绝。2026-10-25原Windows424作为普通成员仅看到管理员155，向普通619的一次正式`room_connect`在`CUSTOMER_SIMULATION_ACCOUNT_BINDING_REQUIRED`前置层拒绝且后台未生成委派；这不等于`administrators_only`角色分支已真机通过。完整限制与下一步见[售后房普通成员隔离首验](../docs/acceptance/SUPPORT_ROOM_ORDINARY_VISIBILITY_AND_BINDING_GATE_20261025.md)。不得为测角色跳过账号绑定、旧白名单或客户隔离。

同一真实售后房，本机155的有效管理员视角已读回全部16名获批成员（1名管理员、15名普通成员），而普通424仅见管理员155；这只证明这两台当前包的目录投影。其他管理员身份、万人分页以及登录后的普通→普通实际仿真拒绝仍分别验收，不因管理员能看到列表就自动授予工具调用权限。

每次交付记录：时间、服务 UUID、房间 ID、原设备 ID/安装指纹摘要、运行版本/路径、请求/修订/事务 ID、真实结果及证据。网页可打开、邀请提交、工具目录存在、构建成功均不能单独称完成。此技能创建和发布不等于七台升级及长期稳定性已经通过。

管理工具目录缺失、注册恢复或历史任务副作用审核时，读取[管理MCP注册恢复与终态审核](references/management-registration-recovery.md)。保留原房间限制和私有配置，不用SQL改写业务状态。
