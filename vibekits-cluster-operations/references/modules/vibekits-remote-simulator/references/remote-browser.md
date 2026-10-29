# 经仿真通道操作远程浏览器

## 能力与已验证范围

本机 Harness 的模型通过 `vibekits.simulator.call` 使用目标 `vibekits.browser.session`，网页和浏览器实际运行在被控电脑，控制端传指令、接收页面结构、诊断和画面。不要改用本机浏览器冒充远端结果。

2026-10-22 有 Windows58 742（三轮）及 Mac743 Harness→Windows742（一次完整模型流程）的真实证据，分别见项目 `docs/acceptance/REMOTE_BROWSER_58_REAL742_AND_CLEANUP_20261022.md`、`HARNESS743_TO_WINDOWS742_BROWSER_REAL_20261022.md`。这是历史版本证据；最新包必须复验。2026-10-29 读取 main 的默认启动器仍为 Windows，Mac/Linux 被控端会返回 `BROWSER_PLATFORM_NOT_QUALIFIED`；Mac 作为控制端不等于 Mac 被控浏览器已支持。

## 操作顺序

1. 用目标仿真 ID connect，核实际身份、指纹及传输。然后 catalog 获取该端实时 schema。`connected/mcpReady` 是连接状态，不能代替一次真实工具响应。catalog 初始化超时先诊断当前桥、原事务与目标进程，沿已授权备用恢复路线排查；不反复启动浏览器。
2. 调用 `vibekits.simulator.call`，外层为 `routingId`、`toolId: "vibekits.browser.session"`、`arguments`。open 的 arguments 包括 `action: "open"`、唯一 `requestId`、用户网址 `url`、按设备规则选定的 `storageDirectory`。requestId 使用 8–64 个字母、数字、下划线或短横线；路径、平台能力和其他参数以实时 schema 为准。不得从例子猜返回的会话或标签 ID。
3. 保存 open 返回的真实 sessionId/targetId。超时用同 requestId 的 `action: "status"` 对账；重复 open 同 requestId 是对账，不应换 ID 重启。found=false 与已有会话未就绪分别处理。
4. `snapshot` 读标题、最终网址和控件；从当前快照选择 selector，再调用 click/hover/fill/key/scroll。普通动作带真实 sessionId；select/closeTab 带真实 targetId。输入后再次 snapshot 回读，点击后核状态变化。`tabs/newTab/select/navigate/closeTab` 管理自己的标签；`diagnostics` 读取有界控制台及网络故障；`screenshot` 后通过 download_file 取回并检查目标画面。按键和滚动字段（key/deltaY）从 schema 取得。
5. closeTab 后读取 tabs 确认该标签消失。返回 `BROWSER_TARGET_CLOSE_PENDING` 时只对账原会话。close 后 status 应 closed/channelOpen=false，再独立核自有进程与临时 profile 回收。cleanup_pending 继续对原 session close，不改 ACL、不删除别人的浏览器锁、不启动新会话掩盖残留。

## 隔离、限制与验收

默认使用独立临时 profile，调试协议只绑定目标 loopback，经原仿真授权传输；不占用用户个人 profile，不公开 CDP 地址，不忽略证书警告。当前实现每个服务实例维护一个活动浏览器会话；多标签并非多独立会话。多设备是否可同时操作要按控制端和实际连接实现测试，不能从单目标成功推导并发支持。始终按 routingId 保存各自 requestId/sessionId/targetId，避免串设备。

业务登录、发送或提交仍按用户授权；测试输入放在自建无业务页。密码交安全输入，不记录 cookie、授权头、输入正文或完整敏感 URL。只关闭自己的标签、浏览器进程和测试服务。

新签名最终包至少核指定网址、中文 fill/Enter、点击后读回、滚动、双标签切换、真实 console/网络失败、目标截图、关闭和资源回收。Harness 自主操作必须有实际模型工具轨迹，外部脚本成功不能替代；版本、源/目标身份及最终包哈希要匹配。Windows 三轮和 Harness 端到端门禁沿用项目验收合同，不将旧包或源码单测标成新包通过。
