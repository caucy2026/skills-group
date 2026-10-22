# 入房、成员与十级管理

## 先注册个人账号

打开[个人账号](https://kemi-chat.newlinksz.com:21122/account)，通过本人手机号、图片与短信验证码注册并设置密码。验证码与新密码由本人在可信页面完成，不进聊天、脚本、URL或日志。

注册后的权限是**普通会员**：没有自动客户、房间、设备绑定或管理员资格。个人账号页只显示本人资料。设备需在支持的客户端另行登录并核验原安装/原生身份；浏览器登录不能代替设备绑定，同账号功能以实际版本及验收记录为准。

需要管理权限时，由唯一内置 `admin` 在明确的 `customerId` 下授予1–10级客户管理员；之后从[独立管理入口](https://kemi-chat.newlinksz.com:21122/manage)登录，只见获授客户。等级不跨客户，普通管理员不能转授管理资格。旧数字一级/全局等级不代表新客户授权。

## 通用售后与普通协作房

本团队原房间ID `f450c684b868292f67c534b793e26314` 已改名为 **vibekits通用售后**。服务端已设置support/default/pinned标记。加入售后房本身不授予设备互访；访问须有当前客户管理员账号绑定、真实原生身份、目标许可及有效票据。房间管理员ID、昵称或旧owner字段都不是管理凭据。

普通协作房仍按有效成员、原身份和目标许可协作；同账号个人协同是独立链路。不同客户的数据与权限隔离。设备默认普通0级，受邀入房不自动提级。

**交付边界：** 新安装自动入售后房、多后台多域名同时入房、跨后台一键退出和万台真实在线验收尚未完成。当前仍按原设备签名申请、审批和激活接入；旧客户端可能收到新标记但未把售后房置顶。不要把服务端default标记当成客户端已自动入房。

## 客户管理员分级

`admin`从/manage登录，先选择客户，再在用户列表核用户ID，授予该客户1–10级或撤销为普通会员，读回授权revision。只有admin能设置管理员及房间管理员资格；超级管理员是独立角色，10级客户管理员不是超级管理员。

设备提级需当前客户管理权和安装绑定；普通客户管理员只能提到自己在该客户的等级，超级管理员可选择提升后的1–10级。既有接口不提供设备降级。高级目标须走原同意审批；等级、成员关系或工具目录不能替代目标许可、系统权限、签名证明和任务执行租约。跨等级真机及全平台验收仍需分别确认。

## 入口与身份

客户端后台地址是 https://kemi-chat.newlinksz.com:21122 ，本团队 customerId=newlink。网页管理入口为 /manage，个人账号入口为 /account，使用个人注册且已获授权的账号正常登录。本服务只有原默认 `admin` 可为超级管理员，须读取服务器返回的 `superAdmin` 确认；普通1–10级账号、客户管理员与房间设备管理员相互独立，不能仅按名称或等级推断权限。

默认售后房是 vibekits通用售后（f450c684b868292f67c534b793e26314）。入房仍须本机原安装身份响应和管理员审批。

## 只给智能体这个网址和后台密码，怎样把本机加入房间

本团队的地址、默认账号、客户和目标房间已列在下表，智能体应自行读取，不必再让同事抄写设备 ID 或寻找后台。后台密码通过后台登录页或本机受保护的凭据入口输入，不填在本网页、聊天、URL、命令行参数或 Git 中。

| 项目 | 本团队接入值 |
|---|---|
| 分享网址 | https://kemi-chat.newlinksz.com:21122/vibekits/ |
| 客户端 serverOrigin / 后台 Origin | https://kemi-chat.newlinksz.com:21122 |
| 管理入口 | https://kemi-chat.newlinksz.com:21122/manage |
| 后台登录账号 | `admin`（本服务已核实存在的默认账号；若分配了专属账号，使用该账号） |
| 客户 ID | `newlink` |
| 默认房间 | vibekits通用售后 |
| roomId | `f450c684b868292f67c534b793e26314` |
| 机器可读清单 | [agent.json](../agent.json) 的 `onboarding` |
| 后台接口发现 | `GET /.well-known/hbbv-management` 或 `GET /api/v1/service-info` |

**可以直接交给智能体：**

> 阅读 https://kemi-chat.newlinksz.com:21122/vibekits/agent.json 和 rooms 文档，按本团队默认参数把我授权的这台本机加入默认房间。自行检查系统和正式客户端、取得本机原仿真 ID 与安装身份、开启必要的仿真和集群、配置服务、申请一次，然后使用我在后台登录页输入的管理密码，以 admin 登录核对并批准这台设备。不要批准其他设备，不自动提升为管理员。核对激活、新鲜心跳、原 ID 的真实只读工具调用后，报告房间名称、roomId、电脑名称、原 ID、角色与在线状态。保留原配置、凭据和有效授权；遇到首次系统认证按平台要求处理，不重装清数据或反复申请。密码不要写入聊天、脚本、日志或公开文件。

### A. 先在要入房的本机完成准备

1. 按 [安装](installation.md) 从对应平台商城安装并打开 VibeKits；已有客户端先保留原身份覆盖升级，不重新生成设备 ID。外部 Codex 未注册 VibeKits MCP 时，使用完整 [远程仿真技能](https://github.com/caucy2026/skills-group/tree/main/vibekits-remote-simulator) 的受保护本机桥，或操作本机 VibeKits 原界面。无需先连接另一台电脑。
2. 在“远程状态”读取**本机仿真 ID、电脑名称、系统和实际版本**。后台审批只使用这个本机 ID，不使用远程办公 ID、历史示例 ID 或别人的 ID。在本机开启远程仿真并确认就绪；首次系统安装、设备同意和 OS 认证若实际需要，由设备持有人在系统窗口完成。后台密码不替代操作系统密码。
3. 设置里开启集群，填写上表 serverOrigin 和 customerId；房间操作在外面的“远程状态 / 仿真信息”。有 MCP 时先用 `vibekits.system.describe_tool` 读取本版本实际 Schema，再调用下列工具；没有该工具时走同一原界面，不编造 API。

```json
{"tool":"vibekits.cluster.configure","arguments":{"serverOrigin":"https://kemi-chat.newlinksz.com:21122","customerId":"newlink","trustedHosts":["kemi-chat.newlinksz.com"]}}
{"tool":"vibekits.cluster.set_enabled","arguments":{"enabled":true}}
{"tool":"vibekits.cluster.rooms","arguments":{}}
```

保留同 Origin 既有可信配置；此公网地址使用受信 HTTPS，不关闭 TLS 验证，不导入别人的私钥。`roomsAreLive=false` / “发现中”时先完成原同步，不根据缓存提交新申请。

4. 核对默认房间名称和 roomId。若当前已经 approved，直接做第 C 段，不退出重加；若 pending，复用原 applicationId。未申请时只提交一次：

```json
{"tool":"vibekits.cluster.apply","arguments":{"roomId":"f450c684b868292f67c534b793e26314"}}
```

保存原申请的 applicationId、revision、本机 ID 和安装指纹摘要。挑战签名、设备凭据及激活由本机客户端完成，智能体不用导出私钥，也不手工给服务器伪造安装身份。

### B. 有权的账号审批自己的原申请

浏览器路线：打开上表管理入口 → 用已获客户/房间管理权的个人账号登录（只有明确授权的代办会话才能使用默认 `admin`） → 选择客户 `newlink` → 选择默认房间 → 点击房间入口的待审批消息 → 核对本机名称、仿真 ID、平台和安装指纹 → 批准**这一条申请**。账号只管理自身获授权的客户/房间；不要用另一客户的房间或从账号名推断权限。

接口路线适合已有受保护凭据入口的智能体：

1. `POST /api/v1/manage/login`，Header 为 `Content-Type: application/json`、`X-Hbbv-Client: api`，JSON 字段是 `username`、`password`。username 使用当前获授权账号；默认 `admin` 只用于明确获准的超级管理员操作。不要把真实密码写入命令行、文件或示例；通过受保护输入在内存组成请求。
2. HTTP 登录响应中的 `accessToken` 仅留本次进程内存。后续请求使用 `Authorization: Bearer <accessToken>`，不打印响应凭据。普通浏览器登录使用 HttpOnly Cookie；浏览器写请求还须同 Origin 和 `X-CSRF-Token`，不要混用两条认证路线。
3. 登录后读 `GET /api/v1/manage/agent-guide`、`GET /api/v1/manage/openapi.json`，以**线上合同**为准；管理 MCP 在 `/api/v1/manage/mcp`，使用现有管理会话，不把设备令牌当管理令牌。
4. `GET /api/v1/manage/rooms?customerId=newlink`，核对目标房间属于当前账号；再 `GET /api/v1/manage/rooms/{roomId}/join-applications`，按线上返回的 cursor 分页。精确找到第 A 段的本机 ID、安装指纹和 applicationId，禁止“批准全部待办”。
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
