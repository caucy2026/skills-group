# 入房、成员与十级管理

## 先注册个人账号

打开[个人账号](https://kemi-chat.newlinksz.com:21122/account)，通过本人手机号、图片与短信验证码注册并设置密码。验证码与新密码由本人在可信页面完成，不进入聊天、脚本、URL或日志。

注册后是普通会员，不自动获得customer、房间、设备绑定或管理资格。浏览器注册和客户端原身份登录分别完成；同账号个人协同不要求先加入集群房间，最终能力以实际客户端和验收结果为准。

## kemi业务与newlink通用服务

本团队业务客户ID为 **kemi**，协作接入房为 **kemi 通用测试房**（`c0985cc4dfeedaf71515ae029fc4cc4f`）。已有approved成员直接核实时心跳和工具；未加入时按下方原安装身份申请、审批、激活流程操作。其他组织使用其管理员明确分配的customerId。

**newlink**保留独立通用服务关系。当前第一槽是 **通用服务1**（原ID `f450c684b868292f67c534b793e26314`）；它不是kemi业务客户，也不是所有设备必须硬编码加入的房间。客户端只展示自己已分配/加入的服务房，不列出其他服务槽。普通设备只见有效设备管理员，彼此不可见、不可互相仿真；有效设备管理员按当前等级及目标许可维护设备。业务普通协作房继续按有效成员和room-members规则协作。

最多8个服务槽、每槽10000台；服务器按原生签名身份找回既有关系，或分配下一有容量的槽。用户一键退出后保留退出决定，不会因普通刷新自动重新加入。**2026-10-25生产已启用自动服务分配**：4台真实已绑定设备完成签名resolve并保留原ID、令牌、epoch和客户归属；普通售后设备彼此仍不可见。全新安装首次入房、重装找回、真实退出/恢复及万台同时在线尚未完成实机验收。当前设备可在一个服务Origin下加入多个获授权房间，不宣传同时连接多个服务域名。

## 账号管理员与房间设备管理员

只有内置 **admin超级管理员**可任命注册账号为1–10级客户管理员或通用管理员。客户管理员选择customerId，只管理获授客户的全部房间；通用管理员管理本服务器所有客户，不等于超级管理员，也不能任命其他账号管理员。普通注册不再默认一级。

房间中的管理员是**设备管理员**。有权的客户/通用管理员可为已批准设备设置不超过自己等级的设备管理员，0表示撤销显式授权；有效更高权限不能被越权覆盖。账号当前登录的设备可在已加入的相应房间继承账号管理等级，必须核当前绑定、客户会话、原安装/Native身份和授权修订。后台管理员账号与设备管理员是不同对象，设备保护等级也不因普通入房而自动提升。

设备管理员访问同级/低级目标仍核原身份、成员、目标许可、工具范围和有效签名票据；更高目标按原同意审批处理。服务房成员资格不授予普通成员互访。房间身份不代替业务任务唯一租约、本机grant、系统权限或签名材料授权。

## 在线、登录到期与独立授权

集群心跳在线、个人协同在线、模型证明和工具可用分别核验。手机在线电脑0时，检查同账号Host当前绑定、目录心跳和协同凭据期限，不用原MFA尚有效或canHost声明替代在线证明；先对账原恢复事务，不改期限、反复登录或清数据掩盖问题。

客户登录到期后，旧继承管理员快照重验失效；另有有效显式2级设备授权时，只能以独立2级重新解析，不能沿用过期账号4级，撤销该显式来源后也失效。个人协同短凭据到期与房间独立设备授权分别处理。相关[31项合同与负控证据](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ADMIN_INHERITANCE_SESSION_EXPIRY_CONTRACT_20261025.md)不代表最终GUI、全舰队或真实未消费票据撤销矩阵通过。

## 入口与身份

客户端serverOrigin是 https://kemi-chat.newlinksz.com:21122 ，业务customerId=kemi。网页管理入口是/manage，普通个人账号入口是/account。管理登录后以返回的superAdmin、管理员类型、customerId和等级确认范围，不从账号名称、旧owner或等级数字猜权限。

本团队默认业务房为kemi 通用测试房（c0985cc4dfeedaf71515ae029fc4cc4f）。newlink通用服务关系独立保留；在普通业务房加入不代表已获售后管理员资格。

## 只给智能体这个网址和后台密码，怎样把本机加入房间

本团队的地址、默认账号、客户和目标房间已列在下表，智能体应自行读取，不必再让同事抄写设备 ID 或寻找后台。后台密码通过后台登录页或本机受保护的凭据入口输入，不填在本网页、聊天、URL、命令行参数或 Git 中。

| 项目 | 本团队接入值 |
|---|---|
| 分享网址 | https://kemi-chat.newlinksz.com:21122/vibekits/ |
| 客户端 serverOrigin / 后台 Origin | https://kemi-chat.newlinksz.com:21122 |
| 管理入口 | https://kemi-chat.newlinksz.com:21122/manage |
| 后台登录账号 | `admin`（本服务已核实存在的默认账号；若分配了专属账号，使用该账号） |
| 客户 ID | `kemi` |
| 默认房间 | kemi 通用测试房 |
| roomId | `c0985cc4dfeedaf71515ae029fc4cc4f` |
| 机器可读清单 | [agent.json](../agent.json) 的 `onboarding` |
| 后台接口发现 | `GET /.well-known/hbbv-management` 或 `GET /api/v1/service-info` |

**可以直接交给智能体：**

> 阅读 https://kemi-chat.newlinksz.com:21122/vibekits/agent.json 和 rooms 文档，按本团队默认参数把我授权的这台本机加入默认房间。自行检查系统和正式客户端、取得本机原仿真 ID 与安装身份、开启必要的仿真和集群、配置服务、申请一次，然后使用我在后台登录页输入的管理密码，以 admin 登录核对并批准这台设备。不要批准其他设备，不自动提升为管理员。核对激活、新鲜心跳、原 ID 的真实只读工具调用后，报告房间名称、roomId、电脑名称、原 ID、角色与在线状态。保留原配置、凭据和有效授权；遇到首次系统认证按平台要求处理，不重装清数据或反复申请。密码不要写入聊天、脚本、日志或公开文件。

### A. 先在要入房的本机完成准备

1. 按 [安装](installation.md) 从对应平台商城安装并打开 VibeKits；已有客户端先保留原身份覆盖升级，不重新生成设备 ID。外部 Codex 未注册 VibeKits MCP 时，使用完整 [远程仿真技能](https://github.com/caucy2026/skills-group/tree/main/vibekits-remote-simulator) 的受保护本机桥，或操作本机 VibeKits 原界面。无需先连接另一台电脑。
2. 在“远程状态”读取**本机仿真 ID、电脑名称、系统和实际版本**。后台审批只使用这个本机 ID，不使用远程办公 ID、历史示例 ID 或别人的 ID。在本机开启远程仿真并确认就绪；首次系统安装、设备同意和 OS 认证若实际需要，由设备持有人在系统窗口完成。后台密码不替代操作系统密码。
3. 设置里开启集群，填写上表 serverOrigin 和 customerId；房间操作在外面的“远程状态 / 仿真信息”。有 MCP 时先用 `vibekits.system.describe_tool` 读取本版本实际 Schema，再调用下列工具；没有该工具时走同一原界面，不编造 API。

```json
{"tool":"vibekits.cluster.configure","arguments":{"serverOrigin":"https://kemi-chat.newlinksz.com:21122","customerId":"kemi","trustedHosts":["kemi-chat.newlinksz.com"]}}
{"tool":"vibekits.cluster.set_enabled","arguments":{"enabled":true}}
{"tool":"vibekits.cluster.rooms","arguments":{}}
```

保留同 Origin 既有可信配置；此公网地址使用受信 HTTPS，不关闭 TLS 验证，不导入别人的私钥。`roomsAreLive=false` / “发现中”时先完成原同步，不根据缓存提交新申请。

4. 核对默认房间名称和 roomId。若当前已经 approved，直接做第 C 段，不退出重加；若 pending，复用原 applicationId。未申请时只提交一次：

```json
{"tool":"vibekits.cluster.apply","arguments":{"roomId":"c0985cc4dfeedaf71515ae029fc4cc4f"}}
```

保存原申请的 applicationId、revision、本机 ID 和安装指纹摘要。挑战签名、设备凭据及激活由本机客户端完成，智能体不用导出私钥，也不手工给服务器伪造安装身份。

### B. 有权的账号审批自己的原申请

浏览器路线：打开上表管理入口 → 用已获客户/房间管理权的个人账号登录（只有明确授权的代办会话才能使用默认 `admin`） → 选择客户 `kemi` → 选择默认房间 → 点击房间入口的待审批消息 → 核对本机名称、仿真 ID、平台和安装指纹 → 批准**这一条申请**。账号只管理自身获授权的客户/房间；不要用另一客户的房间或从账号名推断权限。

接口路线适合已有受保护凭据入口的智能体：

1. `POST /api/v1/manage/login`，Header 为 `Content-Type: application/json`、`X-Hbbv-Client: api`，JSON 字段是 `username`、`password`。username 使用当前获授权账号；默认 `admin` 只用于明确获准的超级管理员操作。不要把真实密码写入命令行、文件或示例；通过受保护输入在内存组成请求。
2. HTTP 登录响应中的 `accessToken` 仅留本次进程内存。后续请求使用 `Authorization: Bearer <accessToken>`，不打印响应凭据。普通浏览器登录使用 HttpOnly Cookie；浏览器写请求还须同 Origin 和 `X-CSRF-Token`，不要混用两条认证路线。
3. 登录后读 `GET /api/v1/manage/agent-guide`、`GET /api/v1/manage/openapi.json`，以**线上合同**为准；管理 MCP 在 `/api/v1/manage/mcp`，使用现有管理会话，不把设备令牌当管理令牌。
4. `GET /api/v1/manage/rooms?customerId=kemi`，核对目标房间属于当前账号；再 `GET /api/v1/manage/rooms/{roomId}/join-applications`，按线上返回的 cursor 分页。精确找到第 A 段的本机 ID、安装指纹和 applicationId，禁止“批准全部待办”。
5. `POST /api/v1/manage/rooms/{roomId}/join-applications/{applicationId}/decision`，JSON 为 `{"decision":"approve","expectedRevision":<刚读取的申请revision>}`。revision 是申请版本，不能拿房间版本代替。409 时重新读原申请；请求超时先查询其状态，不创建另一条申请或盲目重放。
6. 结束后 `POST /api/v1/auth/logout` 退出本次临时管理会话；已有同事会话不动。后台密码不保存进设备集群配置，客户端只保留自己的正常安装身份和凭据。

房间不显示时，先核客户/账号、实时目录及 discoverable。房主可在后台当前房间邀请第 A 段的**本机 ID**，设备读取自己的 invitationId 后响应原邀请再正常审批；邀请不代替设备响应。不要创建一个同名房间来掩盖权限或发现问题。

### C. 批准后再完成激活和实际验通

回到本机刷新 `vibekits.cluster.rooms`，让客户端按原安装身份自动激活。核对 `connected=true`、`roomsAreLive=true`、对应 membership 为 `approved`，并在后台设备列表看到本机的**新鲜心跳**、实际平台、版本和默认组员角色。仅出现“已邀请”“已批准”或缓存绿灯还不算接入完成。

从当前工具目录选择一个无副作用只读工具验证本机功能；验证同房间远程通信时，只选择已授权的在线成员，按 [仿真](simulation.md) 的 connect → 当前 catalog → 实际只读 call 操作，记录对方原 ID 和真实响应。双方可见与工具执行分别核验，不能为了验通擅自扩大对方设备权限。需要管理员角色时再按明确授权单独设置并读回，不把所有新成员默认升为管理员。

最终回执至少包含：设备名称 / 本机仿真 ID / 实际系统和版本 / 客户 ID / 房间名称与 ID / membership 和角色 / 激活与心跳时间 / 真实只读调用结果 / 尚未完成的系统确认。

### 卡住时按状态解决

- `401`：密码或会话无效；停止自动重试，重新通过受保护登录入口认证，不猜密码（登录有频率限制）。
- `403`：当前账号或客户/房间权限不匹配；不能用知道密码代替正确账号和权限。复查既有分配，不另建账号绕过。
- 一直“申请中”：查同一个 applicationId，确认后台选择的是本机的原 ID；先审批、后激活，勿反复点申请。
- 已批准但离线：分别核本机进程、仿真和集群开关、实际后台 Origin、客户、TLS 和本机当前网络；不清配置或重置身份。
- 首次设备确认、OS 密码或 PIN：在对应设备/系统窗口完成，后台管理密码不能替代它们。

## 客户端加入与退出

从主界面远程状态/仿真信息操作。选择房间核名称与 roomId，点击一次申请，保持申请中/等待审批；超时先查原 applicationId，不重复申请。管理员批准后等客户端激活、实时心跳，再做原 ID 的真实只读调用。退出后验证成员资格、旧票据与相应委托失效，而不只是隐藏条目。

列表和明细可折叠；折叠不停止同步。设备信息应显示名称、原 ID、办公 ID（有时）、平台/版本、角色、在线与最后更新时间。缓存或绿灯不是执行证明。

## 管理员邀请与审批

- 先选择当前客户与正确房间。入口待审批消息可直接查看设备基本资料、原身份与申请，批准或拒绝。
- 手工输入或 UTF-8 TXT 文件，每行一个 6–16 位原 ID；解析、去重、确认列表后才邀请。常规单批最多100台，当前限制以界面为准。
- 逐台查看等待身份、等待响应、待审批、等待激活、已加入、拒绝、撤销或过期。缺设备资料显示未知，不编造。
- 未入房设备的管理员意向不代替审批。现有成员升降角色核 revision；普通成员入口不能暗中降级现管理员。降为组员与移出房间分别处理。

## 查找可用能力

加入后从客户端/后台成员列表和实际 cluster 工具目录发现设备，不把历史 IP 或本网页当固定设备表。公开网页不提供私有凭据或固定个人设备清单。

查看平台事实、能力自述、验证证据、模型、工具/组件、当前负载、最近心跳。能力声明不等于实测，也不等于授权。无模型设备可提供已获准的确定性构建、签名、ADB或文件资源；开放推理任务须真实模型就绪。

## 借用设备完成任务

1. 写清应用/项目、目标平台、材料与 SHA、输出/签名要求、允许副作用、截止、回滚和独立验收。
2. 检查当前获批设备与能力，核原身份、当前工具 Schema、资源与运行中的工作；不停止其他同事任务。
3. 房间任务须冻结合同，发布、竞标、唯一有效分配、claim/fence/lease、本地 grant 和 operation permit 均有效才执行。
4. 任务正文、问题、进展与结果进入持久账本并双向 ACK。queued/received/processed 都不是业务通过。
5. 独立检查实际外部效果与产物 hash 后 review/评分。过期/failed旧任务不重放，未知结果先对账原实例。

当前工具未提供或服务执行未开启时，如实报告 task_execution_unavailable。文档描述协作合同，不代表任意版本、所有设备已完成全链路验收。

## 签名资源怎么使用

选择当前已批准且声明/实测具备硬件令牌签名的 Windows 节点，或具有项目 Developer ID/公证能力的 Mac 节点。按“Windows 签名”和“Mac 签名”手册准备完整合同；证书、Keychain 和 PIN 留在签名设备，不复制给请求方。房间成员身份不会自动授予证书使用、发布账号或任意工具权限。

## 完整技能与深入阅读

- [后台管理](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/management.md)
- [入房与角色](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/rooms.md)
- [任务协作](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-agent/GUIDE.md)
- [能力声明](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-capabilities/GUIDE.md)
