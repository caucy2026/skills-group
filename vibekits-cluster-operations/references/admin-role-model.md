# 账号管理员与房间设备管理员

2026-10-22更新。采用前核对服务实际源码和OpenAPI；历史global等级不是新角色授权。管理入口与个人账号登录继续隔离。

- 超级管理员仅为默认admin。只有它能为注册账号设置客户管理员或通用管理员、1–10级；普通注册默认会员。
- 通用管理员作用于本服务器所有customer，无需选择客户；不等于超级管理员，不能任命其他账号管理员。
- 客户管理员限定所授权customer，可管理其全部房间，不能跨客户；customerId不是roomId。
- 房间的管理员叫设备管理员。客户/通用管理员可将已批准设备设为不超过自己等级的设备管理员，0表示撤销手工授权。不能覆盖更高有效等级的设备。
- 账号登录的设备在已加入的相应范围房间继承账号权限。必须验证当前账号绑定、会话、安装与原生身份，不信任客户端自报角色。登录不等于自动加入全部房间。
- 同房间设备管理员访问同级/低级设备不需要额外逐台白名单；高级目标仍需独立审批。已有工具范围、目标房间授权、签名委托、本机安全限制保持，管理员身份不是任意业务执行许可。
- 手工房间授权绑定原安装指纹与成员版本；退房、换身份后失效。账号绑定/等级/撤权/连接代数变更使旧账号委托失效。无账号的手工设备管理员也必须有可信原生broker的在线身份。
- 通用售后房：普通设备只见有效管理员，彼此不可见、不可仿真；有权设备管理员可见相应设备。普通协作房保留原成员协作。

## 后台操作

admin登录管理入口，展开账号目录并搜索，打开单独权限弹窗，选择客户管理员或通用管理员及等级。客户管理员选择对应客户上下文；通用管理员不用先选客户。通用授权与已明确存在的客户授权独立保存，撤销通用授权不会自动清除已有客户授权；降权时必须核对所有仍有效的授权来源。

在目标customer房间展开设备，点击“设备管理员”，选择0至自己的等级并保存。重开弹窗读取实际等级、刷新设备行标签。不要把旧版“管理员登记”标签或原全局设备等级当成新账号授权。

## API与验收

先GET取得版本再PUT，cookie写入携带CSRF；不保存密码、cookie或令牌到技能/证据。

- `/api/v1/manage/users/{userId}/general-administrator`：GET/PUT，administratorLevel为1–10或null、expectedRevision，仅admin。
- `/api/v1/manage/customers/{customerId}/managers/{userId}/level`：原客户授权接口；客户授权原版本与通用授权版本分别核验。
- `/api/v1/manage/rooms/{roomId}/members/{deviceId}/device-administrator`：GET/PUT，deviceAdministratorLevel为0–10、expectedRevision，受当前客户管理等级上限约束。

核验普通会员后台拒绝、跨客户拒绝、通用管理员所有客户可见但不能任命账号、10×10等级矩阵、并发版本冲突、退房/换身份/撤权失效，以及最终设备真实房间仿真。单测、浏览器fixture与真实设备证据分开报告。

### 页面权限诊断先读当前客户的真实响应

管理页选择客户后会读取`GET /api/v1/manage/account?customerId=<当前客户>`。`generalAdministratorLevel`表示独立的服务器通用授权；该响应的`customerAdministratorLevel`是**在当前客户可用于管理的有效等级**，通用管理员即使没有`customer_managers`客户授予记录，这里也可返回其通用等级。独立客户授予须另看`GET /api/v1/manage/customers/{customerId}/managers/{userId}/level`，不凭这个有效等级字段判断授权来源。页面的房间设备控件原本就使用有效等级；排查“通用管理员看不到按钮”时，先核选定customer、真实账号响应、当前房间和页面渲染，再判断是否是前端缺陷。

2026-10-27本项目曾只看`web/app.js`字段名误判缺入口，提交冗余修改和模拟了不真实响应的测试；真实管理登录/HTTP合同证明原页面字段可用，前端已按原字节撤回，生产运行文件也与原字节相同。见[误判纠正及生产读回](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G07_GENERAL_ADMIN_ROOM_DEVICE_UI_SOURCE_FIX_20261027.md)。这项经验不替代真实浏览器保存/撤销矩阵。

源码与验收索引：hbbv `docs/requirements/ACCOUNT_AND_DEVICE_ADMIN_ROLE_REPLAN_20261022.md` 与 `docs/acceptance/ACCOUNT_DEVICE_ADMIN_REPLAN_20261022.md`。使用源码main及实时服务回执，不把文档写入等同于当前环境已经部署。


## 售后房任务入口拒绝的判断（2026-10-23）

房间设备列表隔离不代表所有任务入口安全。公告/公告inbox、controller状态、组长租约、同步屏障以及附件下载均需核当前可见范围；历史任务ID、已签名envelope和旧ACK幂等回执不构成持续读取许可。遇到TASK_NOT_FOUND或ARTIFACT_NOT_FOUND，先核support标记、当前账号/设备权限、任务是否包含隐藏对端；不要靠重复邀请、临时白名单或自动提升等级“修复”有意的范围拒绝。

售后普通设备仅能下载当前可见任务明确引用的附件；有效管理员可读完整范围，普通协作房保留旧行为。隐藏公告翻页仍须推进扫描游标，否则旧条目可能阻塞后续本机合法工作。保留签名合同/历史审计原文，不改写envelope凑通过。

对应源码/实证：hbbv docs/acceptance/SUPPORT_TASK_SIDE_ROUTE_PRIVACY_20261023.md。11个新增侧路夹具、相关96项本地与Linux回归通过，不代表所有其他执行接口、真实设备全部撤权方向或原始G01–G10完成。


竞标与执行入口同样需要当前范围：offer列表过滤不可见任务；offer签收、claim、签名执行context及操作报告应在幂等缓存返回之前重新核权。设备曾合法领取，不意味着退出管理员权限或房间隔离规则变化后仍可取得旧签名回执。任务发行者读取操作状态时，也不能泄露当前不可见的历史worker。

外部操作一旦结果未知，保留原operationKey、generation、fence及审计记录，由当前有权管理端对账；不要删除幂等账本、换key或重发副作用。新增路线与实测边界见hbbv docs/acceptance/SUPPORT_TASK_EXECUTION_ROUTE_PRIVACY_20261023.md，线上是否生效以该文最新部署回执为准。

## 登录到期与独立设备授权分别核验（2026-10-25）

房间管理员继承依赖业务customer的当前客户登录会话、原安装/Native身份与授权修订；个人协同account-v2的短凭据另外核验。手机在线电脑为0而集群仍在线时，分别核目录心跳、协同凭据期限和当前绑定，不把功能声明或原MFA尚有效当在线证明，不改期限或重复登录掩盖自动恢复缺陷。

客户登录到期后，旧继承管理员快照必须重验失效；若设备另有有效显式2级授权，只能以独立设备管理员2级重新解析，不能沿用已到期账号的4级。撤销显式授权后该来源也失效；仍须受信broker、原Native在线身份、安装指纹和成员版本。不要把一次个人协同到期自动推断为所有独立房间授权都已撤销。

已加入永久回归：31个唯一相关用例通过，隔离忽略session expiry的负控被预期AssertionError拒绝；这是源码合同，不是最终GUI或真实未消费票据撤销通过。[完整证据与边界](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/ADMIN_INHERITANCE_SESSION_EXPIRY_CONTRACT_20261025.md)。

## 生产汇总与真实验收边界（2026-10-26）

生产只读核验见[G07角色范围回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G07_PRODUCTION_ROLE_SCOPE_READONLY_20261026.md)：4个用户中3个有注册会员标记，仅默认admin的超级管理员授权有效；另有活跃通用管理员记录1、客户管理员记录3，注册会员中1个没有任何管理授权。记录可能重叠，不可相加当独立人数。显式房间设备管理员和旧设备正等级记录均为0，但账号当前绑定仍可继承有效设备等级；账户基础level默认为1不代表客户或通用管理员授权。生产此时无2–10级活跃实例，20项相关源码测试通过也不证明真实十级升降级、最终UI或撤权旧票拒绝。专用QA房132成员仍revoked、申请pending，须经真实管理审批入口继续，不能写库绕过。
