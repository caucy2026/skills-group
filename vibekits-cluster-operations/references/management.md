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

## 注册、超级管理员与等级

当前生产网页已提供“验证码注册”和“忘记密码”：手机号 → 图片验证码 → 短信验证码 → 设置/确认密码 → 返回登录。验证码与新密码按当前操作工具要求由本人完成；不通过程序解题、日志读取验证码或注入数据库代替真实验收。

默认启动账号 `admin` 在本部署由受信启动入口设为超级管理员；不是任意注册同名账号就获得权限。首次空库的 `--admin-user` / `--password-file` 只初始化首个账号，已有库不得借此重置密码、另启空库或换服务身份。`--customer-super-admin-user` 是主机侧显式指定的已有账号；只在确有授权的部署变更中使用。

旧后台账号迁移和新注册账号默认一级。超级管理员是独立角色，可在“我的账号 → 用户与管理员等级”查看用户、选择1–10级并保存；普通账号只能看到自己的等级。账号等级、客户管理权、房间成员角色和设备等级相互独立，不随注册、邀请或房间管理员角色自动提高。

详细 UI/API、设备提级、等级仿真与失败处理见 [注册及账号/设备分级](account-device-levels.md)。2026-10-18生产切换、旧数据副本迁移/回退、375项服务器测试和已有账号网页登录已验证；真实短信注册与新账号登录、默认一级显示及超级管理员十级选项已另行实测；找回密码、真实生产提级/降级和跨等级设备仿真仍须分别验收，不能据此称全部完成。

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

## 文件邀请预览

支持手工输入或 UTF-8 TXT（BOM兼容、每行一个ID、64KiB以内）。6–16位数字、去重后1–100台；无效内容整批拒绝，不覆盖原输入。先列目标房名/ID及每台ID，核实后确认发送；换房阻止旧预览。响应未知沿用原请求ID先对账。记录展示逐台状态、电脑名、平台、版本、实时心跳，未知标待上报。2026-10-16源码及交互测试通过；部署与真实浏览器验收单独核验。
