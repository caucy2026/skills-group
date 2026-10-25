> 最新角色模型：[账号与房间设备管理员](admin-role-model.md)。本页历史“房间管理员不可由客户管理员委派”规则已被替代；账号管理员任免仍仅限admin。

# 后台、账号与客户管理员

## 登录和账号边界

个人注册/登录入口：https://kemi-chat.newlinksz.com:21122/account 。独立管理入口：https://kemi-chat.newlinksz.com:21122/manage 。客户端serverOrigin仍为同站Origin，不带/account、/manage或/vibekits路径。

注册只建立普通会员账号，没有自动客户、房间、设备或管理员绑定。一个账号可在支持的客户端登录多台设备，可信设备绑定与账号管理权限独立；同账号能力仍按实际版本及验收记录使用。普通个人账号页不显示客户/房间管理列表。

只有保留的内置admin为超级管理员，按认证用户ID及服务器记录判定。admin在明确customerId下授予/撤销1–10级客户管理员；客户管理员仅管理获授客户，不能转授管理员。房间管理员、设备等级、资源owner和旧全局数字等级都不能代替当前客户授权。

API个人登录POST /api/v1/account/login；管理登录POST /api/v1/manage/login。API请求头X-Hbbv-Client: api，响应实际accessToken仅留内存；后续Bearer。旧/auth/login仅兼容历史路线，不作为普通注册账号取得管理会话的方法。浏览器HttpOnly cookie写入还要求同源和X-CSRF-Token。不得把密码/token放URL、命令参数、报告或Git。

## 账号分级与迁移

管理员授权以serverId/customerId/userId为范围。先选客户，再在“用户与管理员等级”核用户ID、当前客户等级及授权revision。PUT /api/v1/manage/customers/{customerId}/managers/{userId}/level，body为administratorLevel（1–10，或null撤销）及expectedRevision；首次授权也先GET同一路径，不能假定revision。仅admin可写，409读回后重新决定，不重放未知结果。

旧自动一级不再是有效客户管理员；旧全局等级保留兼容/历史但不授新权限。无法确认的旧授权只显示待核提示，由admin明确决定，不能凭数字、手机号或房间owner自动补授。超级管理员不是普通10级；配置/升级不重置密码、身份或原设备授权。

注册短信、图片验证码、新密码按平台要求由本人在可信网页完成。hbbv独立数据库，不读取HBBC用户库。当前规则覆盖2026-10-18曾采用的默认一级规则，历史验收数字不当作新规则验收。详细接口与验收边界见[账号/设备分级](account-device-levels.md)。

## 售后房

本团队原roomId f450c684b868292f67c534b793e26314现为newlink“通用服务1”，已持久设置support/default/pinned。最多8槽、每槽10000台；后续槽由服务器按原生身份和容量分配，不能给所有机器硬编码槽1。普通成员不因同房互访；有效设备管理员仍需账号绑定或显式授权、真实原生身份、目标许可和票据。普通业务房在kemi保留原成员协作规则。服务端自动分配已启用且4台既有真实设备签名resolve；新装首入、重装、退房恢复、多后台及全客户端真实验收未完成。

只有admin可通过PUT /api/v1/manage/rooms/{roomId}设置supportRoom布尔值，连同name/description/expectedRevision提交；newlink通用服务由服务端最多8槽容量策略管理，不能创建同名房间代替自动分配。名称不是标记。先读当前房间和修订，保留成员/任务/积分，未知结果核原事务后再决定。管理列表用view=summary，展开读取原完整详情。

## 房间生命周期

1. 选对客户→“创建房间”→名称、类型、说明、允许客户端发现。类型 general（通用）、pipeline（流水线）、dedicated（指定设备）、synchronized（多机同步）。读取新 roomId/customerId/owner/revision。
2. 卡片进入房间，名称和 ID 明示；“修改名称”用最新 expectedRevision；冲突刷新并合并，不能覆盖别人修改。复制名称与复制房间 ID 分开核验。
3. 关闭发现只影响目录可见性，不是退房、停用设备或删除历史。不要把“隐藏”当成员撤销。删除/转让如当前目录未提供，不能直写数据库实现。
4. 卡片选中态使用浅色底、清晰边框与选中标记；标题保持可读。每个房间入口直接展示待审批数量，点击查看申请设备信息并批准/拒绝，不要求进入多层菜单。此为验收目标，未部署部分不能称已实现。

## 管理员与成员

仅内置admin可授予或撤销管理员资格；房间“加入房间”中分“加入普通成员”和“加入管理员”，输入原仿真 ID，可批量。尚未批准的设备仍需邀请、安装身份签名申请、审批、激活；登记角色不等于已入房。

- 新增：POST `/api/v1/manage/rooms/{roomId}/members/add`，`{deviceIds:["原ID"],role:"member"或"administrator",requestId:"稳定唯一请求ID"}`。
- 现有成员升降级：PUT `/api/v1/manage/rooms/{roomId}/members/{deviceId}/role`，`{role,expectedRevision:当前策略修订}`；降为成员不移出房间。
- 高级全量名单：GET/PUT `/api/v1/manage/rooms/{roomId}/simulation-administrator`；PUT `{administratorSimulationIds:[...],expectedRevision}`，最多100个不重复6–16位原 ID；空数组清空全部。日常优先单成员升降级，避免全量覆盖别人更新。

保存后读回管理员徽标、identityVerified、策略修订，并在另一客户端检查同步。失配身份不显示已验证管理员。角色管理成功与实际仿真调用成功分开报告。

## 审批

在对应房间卡片“待审批 N”打开申请详情，显示电脑名、平台、原仿真 ID、办公 ID（存在时）、安装指纹、申请时间/状态、自述能力。核对原登记身份与入房范围后“批准加入并自动接入”或“拒绝申请”。提交时禁重复操作，未知结果先查原 applicationId。

GET `/api/v1/manage/rooms/{roomId}/join-applications`；POST `.../join-applications/{applicationId}/decision`，`{decision:"approve"或"reject"或"revoke",expectedRevision:申请当前revision}`。旧成员撤销另走 `.../members/{deviceId}/decision` 与成员 revision，不能混用。处理后读回申请终态、卡片计数、客户端状态及服务端心跳。失败不将数量清零或显示假成功。

## 文件邀请预览

支持手工输入或 UTF-8 TXT（BOM兼容、每行一个ID、64KiB以内）。6–16位数字、去重后1–100台；无效内容整批拒绝，不覆盖原输入。先列目标房名/ID及每台ID，核实后确认发送；换房阻止旧预览。响应未知沿用原请求ID先对账。记录展示逐台状态、电脑名、平台、版本、实时心跳，未知标待上报。2026-10-16源码及交互测试通过；部署与真实浏览器验收单独核验。
