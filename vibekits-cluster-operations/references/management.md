# 后台、账号和房间管理员

## 登录及范围

本项目入口： https://kemi-chat.newlinksz.com:21122/ 。用获授权原管理账号登录；页面地址不含 token。先选客户，再选房间，核对 customerId 和 roomId，不能只看同名标题。登录后的 `/api/v1/manage/agent-guide`、`/api/v1/manage/openapi.json` 为实时合同；管理 MCP 为 `/api/v1/manage/mcp`，调用 tools/list 后用实际目录。仅源码有接口而生产目录没有时，不声称可用。

浏览器使用同源 cookie，写操作还需要 X-CSRF-Token；API 登录 POST `/api/v1/auth/login`，请求头 `X-Hbbv-Client: api`，JSON username/password；使用响应实际 accessToken 字段（兼容旧版需查合同），后续 Bearer。秘密只从安全凭据入口读取，不放命令行、URL、源码、报告或技能。

## 三类管理身份

| 身份 | 设置方法 | 实际范围 |
|---|---|---|
| 后台登录账号 | 主机侧正式账号配置 | 账号所拥有的资源；不自动跨客户 |
| 客户总管理员/客户管理员 | 显式主机配置总管理；已有总管理分配客户权限 | 创建客户或管理指定客户；仍检查具体资源归属 |
| 房间设备管理员 | 房间内登记已批准设备的原仿真 ID | 房间角色；不是网页登录账号，也不自动授予设备工具控制 |

## 创建后台账号与总管理员

当前源码没有普通网页“注册账号”入口，不编造按钮或公开创建账号 API。`server/app.py --admin-user NAME --password-file PRIVATE_FILE` **仅数据库 users 为空时初始化首个账号**；不能用它向已有数据库添加第二个账号或重置密码。

已有部署要新增后台账号：由已授权主机运维在正式源码环境中使用 `Store.create_user(name,password)`；先核对实际数据库路径/服务 UUID、备份 SQLite、原服务维护窗口与无在途任务，使用密码交互输入，检查同名账号不得覆盖，在事务中调用并 commit，异常 rollback，关闭 Store。实现入口在 `server/app.py`，先读当前签名；不要直接 SQL 写密码或输出 hash。此操作仅在明确要求新增该账号时实施，不为阅读技能创建账号。账号创建后由本人登录验证；新账号不会继承旧账号房间所有权。

总管理仅主机侧支持 `--customer-super-admin-user EXISTING_NAME`，必须是已存在且获授权的账号，保留原服务所有启动参数/数据库/私钥，经既有 supervisor 正常配置和重载。不是名为 admin 就自动总管理，也不能启动第二个服务器改空库。检查网页“创建客户”按钮和 API 权限；没有跨客户权限时不能自行提权。

创建客户：总管理首页“创建客户”→名称→提交→读回真实 customerId→进入客户空间，复制专属管理网址。精确 API 为 POST `/api/v1/manage/customers`，字段以实时合同为准；客户经理授予 POST `/api/v1/manage/customers/{customerId}/managers`，body `{userId:"已有账号32位ID"}`。仅总管理可授予；客户权限不等于接管其他账号已有房间。不能拿另一客户 token/设备凭据混用。

## 房间生命周期

1. 选对客户→“创建房间”→名称、类型、说明、允许客户端发现。类型 general（通用）、pipeline（流水线）、dedicated（指定设备）、synchronized（多机同步）。读取新 roomId/customerId/owner/revision。
2. 卡片进入房间，名称和 ID 明示；“修改名称”用最新 expectedRevision；冲突刷新并合并，不能覆盖别人修改。复制名称与复制房间 ID 分开核验。
3. 关闭发现只影响目录可见性，不是退房、停用设备或删除历史。不要把“隐藏”当成员撤销。删除/转让如当前目录未提供，不能直写数据库实现。
4. 卡片选中态使用浅色底、清晰边框与选中标记；标题保持可读。每个房间入口直接展示待审批数量，点击查看申请设备信息并批准/拒绝，不要求进入多层菜单。此为验收目标，未部署部分不能称已实现。

## 管理员与成员

房间“加入房间”中分“加入普通成员”和“加入管理员”，输入原仿真 ID，可批量。尚未批准的设备仍需邀请、安装身份签名申请、审批、激活；登记角色不等于已入房。

- 新增：POST `/api/v1/manage/rooms/{roomId}/members/add`，`{deviceIds:["原ID"],role:"member"或"administrator",requestId:"稳定唯一请求ID"}`。
- 现有成员升降级：PUT `/api/v1/manage/rooms/{roomId}/members/{deviceId}/role`，`{role,expectedRevision:当前策略修订}`；降为成员不移出房间。
- 高级全量名单：GET/PUT `/api/v1/manage/rooms/{roomId}/simulation-administrator`；PUT `{administratorSimulationIds:[...],expectedRevision}`，最多100个不重复6–16位原 ID；空数组清空全部。日常优先单成员升降级，避免全量覆盖别人更新。

保存后读回管理员徽标、identityVerified、策略修订，并在另一客户端检查同步。失配身份不显示已验证管理员。角色管理成功与实际仿真调用成功分开报告。

## 审批

在对应房间卡片“待审批 N”打开申请详情，显示电脑名、平台、原仿真 ID、办公 ID（存在时）、安装指纹、申请时间/状态、自述能力。核对原登记身份与入房范围后“批准加入并自动接入”或“拒绝申请”。提交时禁重复操作，未知结果先查原 applicationId。

GET `/api/v1/manage/rooms/{roomId}/join-applications`；POST `.../join-applications/{applicationId}/decision`，`{decision:"approve"或"reject"或"revoke",expectedRevision:申请当前revision}`。旧成员撤销另走 `.../members/{deviceId}/decision` 与成员 revision，不能混用。处理后读回申请终态、卡片计数、客户端状态及服务端心跳。失败不将数量清零或显示假成功。
