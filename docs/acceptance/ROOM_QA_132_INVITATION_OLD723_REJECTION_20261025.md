# G08 专用QA房：132旧723邀请回应门禁（2026-10-25）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

专用QA房`5aaa0431b7666a8bb898c103bf226990`的只读生产记录：155为approved/revision3，原132为revoked/revision2，房间共两条成员记录。原132有一条仍有效的pending邀请，尚无与其绑定的新application；目标旧723客户端的实时`cluster.rooms`也显示该房邀请`awaiting_response`，房间成员`revoked`。

在原ID1321656264、原G73指纹和两间正式房仍可用的前提下，本会话只尝试一次以目标自身签名身份响应**当前唯一的新鲜邀请**。控制端`simulator.call`外层`ok=true`只是工具传输成功；目标`vibekits.harness.diagnostics`独立记录该`vibekits.cluster.apply`调用`status=failed`、耗时532毫秒、结果为“已有申请或决策，请联系管理员处理；不会自动重新申请”。随后只读后台核原QA成员仍revoked/revision2、原application仍approved/revision2、邀请仍pending/revision1且无新application；目标`cluster.rooms`也继续显示revoked/awaiting_response。**没有入房、审批、票据或仿真权限变更**，不得把外层ok冒充成功。

这是旧723客户端阻断邀请恢复的精确证据。主线后续源码已有`freshInvitation`和受邀请终态重申请分支，但源码存在不等于旧端实装；须先用包含该分支的新合格签名包完成132同身份覆盖，再以同一邀请原状态对账并按有效期回应，随后通过获授权管理入口审批、真实房间委派与撤销。当前邀请未消费，不重试旧端调用、不直接改生产SQLite、不放宽newlink售后房隔离。617继续按用户确认离线不连接。
