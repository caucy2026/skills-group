# 房间时间与等级恢复

## 时间未来拒绝：先校准现场，不改安全阈值

`ROOM_SIMULATION_INTROSPECTION_TIME_FUTURE`说明时间证据未通过，不能单凭它判设备离线或权限撤销。分别记录控制端、目标、服务端的UTC毫秒时间与读取起止范围；网络耗时和HTTP Date秒精度不能被当作精确偏移。不要延长票据TTL、放宽未来时间阈值、改白名单或伪造时间字段。

Windows已验证的一种现场是W32Time停用。沿原ID和固定指纹的既有授权连接，先只读核实际主机、服务状态/启动方式、当前操作者权限及在途签名任务，再决定同范围维护：

```powershell
Get-Service W32Time
Get-CimInstance Win32_Service -Filter "Name='W32Time'" | Select-Object State,StartMode
w32tm /query /status /verbose
w32tm /query /peers
```

原服务确实停止且具备正常管理员权限时，使用`Start-Service W32Time`，随后`w32tm /resync /rediscover`复用其已配置时间源。不要默认更换组织NTP源、改域策略、强设本机时间或索取凭据。权限明确拒绝时按既有正常认证入口处理，不能换身份绕过。

**命令exit0不等于同步成功。** 实测首轮exit0但正文“无可用时间数据”、Leap3，不能报通过。用原时间源的有界`w32tm /stripchart /computer:<原已配置主机> /dataonly /samples:3 /period:1`确认可达与偏移，保留超时样本；有了新的可达证据后可再做正常`w32tm /resync`。最终同时核成功正文、Leap0、有效stratum/source/最近同步时间及实际偏移。无需把同一个失败命令无界重试。

确有重启后服务停用问题且在已授权维护范围时，可将该服务改为自动启动并回读原/新启动方式；不要把这次现场修复升级为所有设备统一改系统配置的规则。未真实重启不能宣称开机同步验收通过。

恢复后只对已知未执行的只读检查申请新requestId，立即消费单工具票据并核claimed/completed。未知业务结果仍先对账原事务，不借校时重新执行安装或签名。保留首次拒绝和修复回执；一次恢复不等于长期时钟稳定。

## 等级边界与双向互访

普通业务房同级普通成员互访，与普通成员访问更高等级管理员，是两个用例。`ROOM_SIMULATION_HIGHER_LEVEL_APPROVAL_REQUIRED`是权限边界，不能靠提级、临时名单或改房间模式凑双向PASS。分别读取实际房间类型、成员修订、当前设备等级及有效管理员来源；旧device_levels=0不排除账号继承的房间管理员权限，网页显示等级也不能代替当前签名授权。

选择两台已批准的同级普通成员，按真实catalog通过已有授权编排连接在对端发起`room_connect→room_call→room_disconnect`；被测段仍必须为对端原身份签出的房间票据。分别验证两方向system.info与至少一项所需低副作用真实工具，如对已登记应用文件做file_hash。不读取无关客户文件。编排连接不是房间授权证明，文件哈希不是最新版本或覆盖升级证明。

独立服务端审计关联同一delegationId/controller/target/room/requestId，并核`created≤claimed≤completed≤expires`。仅看目录、准备成功或connected=false不算执行；后者在room_connect准备阶段可以正常。成功后关闭自建房间通道与原本未连接的自建编排连接，保留他人原连接。

## 撤销证据不可替代

已left/revoked的测试房建链前拒绝，仅证明当前不具资格；本地关闭后的not_connected仅证明连接关闭。两者都不能替代“有效且未过期票据签出→成员/授权撤销→旧票调用拒绝”。重授后旧票仍应拒绝，新票才可重新按现权限验证。

撤销实测使用已有专用测试房；先保全原状态、可恢复的管理入口和原事务，不撤销共享业务房正在使用的设备来替代。管理MCP只允许特定房间、没有审批工具时，保留限制；不能扩allowlist、从私有中继提取凭据或直接SQL恢复成员。按平台要求完成确需的当次权限确认；浏览器控制超时与认证/授权拒绝分开记录，局部等待继续独立验收。

## 实证范围

2026-10-23实机：Windows既定时间源重同步后Leap0、偏移约−1.8毫秒；随后房间系统信息和应用清单调用及审计通过。Mac/Windows普通成员双向system.info/file_hash四次与审计通过；普通成员访问管理员被拒绝。见项目`KEMI_ROOM_WINDOWS_CLOCK_RECOVERY_20261023.md`和`G08_KEMI_ORDINARY_PEERS_20261023.md`。这些不是全设备统一包、在途撤销或长期稳定通过。
