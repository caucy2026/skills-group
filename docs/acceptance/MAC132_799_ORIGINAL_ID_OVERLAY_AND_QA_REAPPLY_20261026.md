# Mac132 Intel 原ID覆盖799与受邀重申请（2026-10-26 本地时间）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 旧状态与保护

原仿真ID`1321656264`、macOS12.6.4 Intel、原SSH指纹`SHA256:G73XaZfXCAJjGB793rJdNXr+eHvfl7xbnXGAYZvf5ak`。旧723/build2723运行于`/Users/mac/Library/Caches/Vibekits 2.app`，主PID54977/主程序SHA `16881754b3b9336549d8eed849eccbaa1c29cb9bfeb9b0133e93c6b0e3306053`；旧正式relay PID12197实际`lsof txt`映射inode`12903573822`，与磁盘旧helper一致，helper SHA `59f2e2d3f2050d756d79d1d13bd2754d0b71b07f0b91a6af798210e3a83f80dc`。先前失败798混代relay已被精确恢复，旧守护PID11945不在运行。旧包深签名通过，Bundle ID`com.caucy.vibekits`、Team`26T5WV4GLP`及指定签名要求与最终799相同。kemi业务房和newlink售后房approved/live，QA专用房仍revoked2；无任务会话、无claims，唯一活动原生控制者为本机155。

正式799公证ZIP大小456875779字节、SHA-256 `43749b74fdf57e360164491e3a73b36065d020186613fdc794003baa451e9759`，已先在构建Mac155和Mac445原ID完成实际覆盖/基础功能验收。132卷最初可用7210252KiB。旧私有v1数据保护点90文件已有5个运行中变化；再建不覆盖前例的v2/v3，最新v3覆盖前90份共514884字节，源/副本逐项哈希90/90、目录700/manifest600，manifest SHA `bbdc1d8b32c98b1cdd9a83fd055517595d17ae329dab6a48811efe567c7d58ec`。应用前v3仅一份`consent-renew`运行消息键轮换、公共条目未改；未重置聊天、Keychain、TCC或身份。LAN地址192.168.3.74的Ed25519指纹独立匹配G73，但现有BatchMode SSH认证被拒，不能把同网当备用可写通道；登记的KEMI远程办公ID372799163服务器答复在线，实际桌面操控仍须当场核验。

## 单次更新事务

经原仿真通道上传同一799 ZIP，目标返回完整大小和SHA；`device.update_stage`再在目标更新暂存区生成另一份同SHA包。因磁盘紧张，核更新服务`staged=true`、暂存副本完整、原`/tmp`上传副本无打开句柄后只删后者，目标可用空间6311428→6754600KiB；本机正式ZIP、目标暂存包和旧签名App均保留。当前main执行者`predeploy`资格ELIGIBLE。只在新保护点、原PID/relay映射、唯一控制者、零任务/claims复核后，以私有token**一次**调用`update_apply`；token只在权限600文件与进程内存中，未上Git/聊天/命令行。控制端`schedule=true`不算完成。目标同一`update-extract-wc7bQX/transaction-public.json`于15:51:05Z先记录`STARTING_CANDIDATE`，15:51:54Z记录oldBuild2723→newBuild2799、`COMMITTED/PASS/rollback=NOT_ATTEMPTED`，oldPID54977/updaterPID81832。未重复安装或清旧用户数据。

## 外部回连与真实字节

控制端断开后由原ID重连，G73指纹、MCP和SSH就绪；`system.info`命中新主PID82188，`device.applications`读到同路径799/build2799。新主程序SHA `28c7cda317b996467ad85552099c48ef7e4760c109d6ebe7caef7e100ec4f691`、helper SHA `a2373e92cf064eaaf815f020a84731fc15353f6e73fafedf95a68923597e0517`均与正式包相同；两条真实relay PID82246/82672的映射inode均为当前磁盘helper inode`12906430133`，无重演旧版混代。目标`codesign --verify --deep --strict`和Gatekeeper均通过。真实`cluster.rooms`在一次只读外层失败后，经连接/身份对账和有界复读返回原serverId`da3553a32048bfe691d99ad1a27a914b`、原安装key摘要`0c6551f8f223347a2dcc56895f7acf287050495cbf87033c75921a8f56d4bbc1`、两房approved及`roomsAreLive=true`。生产心跳近1秒、设备档案更新`1.9.0-dev.799`，健康序号重启后重新计数但ID/绑定不变。

v3数据保护点对升级后源：90文件中85字节不变、5变化、0缺失。变化在MCP桥接端点、Harness任务运行端点及3份`cluster-task-messages`：旧键均属`consent-renew`，新键仅`consent-*`，公共条目0修改；不把临时同意续期轮换称业务聊天丢失。v1/v2/v3保护点及目标公开终态保留，私有正文与token未进报告。目标辅助功能`authorized=true`、主窗口可见/输入启用，没有重复系统授权。一次固定工作区零工具`cluster.model.verify`仅返回`request_started`且未重试，随后生产16:12Z心跳报`modelReady=true/modelStatus=ready/credentialStatus=valid`；这证明模型阶段实收，不等于所有工具和可见会话问答已验。

## QA房重申请与未完成门禁

QA房`5aaa0431b7666a8bb898c103bf226990`原成员`revoked/revision2`，后台有未过期且指纹匹配的pending邀请`177e89a6e621e74c71eedbf6999eca7b`；旧723对同邀请曾本地拒绝“已有申请或决策”。新799在原目标用同一邀请ID单次`cluster.apply`，生产只读读回邀请仍pending但已绑定新application`ffa3d827e638295ad265920ef053249e`、状态pending/revision3，成员仍revoked2，未自动审批或授予任何仿真/任务权限。下一步由获授权管理员在后台审原设备信息并批准，再实测房间委派连接、工具和降级/撤销拒绝，不能把`simulator.call`外层ok或pending申请算G08通过。

Intel目标的799仍暴露控制端预算缺口：`device.app_signature`目标真实执行13.556秒成功，控制端普通8秒RPC先报失败；一次`cluster.rooms`目标725毫秒成功但外层超时，身份/连接读回后仅对只读请求重试成功。该双侧证据要求下一候选对明确只读工具做有界时限/传输回归，不重放副作用工具。Safari15目录选择、真实当前会话UI点击/IME/粘贴、旧会话正文、严格长空闲与同签名移除重装仍未全验，G02本机全功能保持BLOCK。529/Windows/617及原Office任务、100台真实扩展也未因132这次覆盖自动通过。
