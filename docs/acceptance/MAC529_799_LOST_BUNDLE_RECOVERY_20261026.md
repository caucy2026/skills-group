# Mac529 丢失磁盘包后的799受控恢复（2026-10-26 本地时间）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 原现场与保护

原仿真ID`5298938227`、原SSH Ed25519指纹`SHA256:Ccvlq/fFq7TtnCOFhZpJ4UMwUqOJeupvuuGEVl600/c`、macOS26.5.1 ARM64。原792/build2792主PID68784（出生Sun Oct25 06:21:21）仍映射inode175198295，却指向已不存在的`/Users/kemi/Library/Caches/com.caucy.vibekits/Vibekits.app`；旧原生relay服务PID95745映射inode175232287，另一stdio PID68789同inode。hbbs原ID服务器答复在线，但原`simulator.connect`仍在SSH source authorization报HTTP500，hbbv两房心跳已停约12小时。磁盘只找到`/Applications/Vibekits.app`旧723，不能用它假称792。原用户私有备份22文件/1125724字节在本轮再次源与副本22/22逐SHA匹配，Keychain/TCC/原公钥单独保护；目标数据卷起始可用约84726496KiB。

用原已授权LAN地址`192.168.3.68`和固定Ccvl指纹BatchMode SSH直接接管，与VibeKits仿真故障通道独立；备用KEMI远程办公ID`415501605`服务器答复在线。用户最近输入空闲约17分钟。主线`predeploy`资格ELIGIBLE；没有改执行策略、用户数据、系统权限或其他服务。目标没有可证明与**运行中的已删除792 inode逐字节相同**的原包，这个回退限制不能省略。

## 双签名包预检与一次切换

799最终Developer ID公证ZIP：456875779字节/SHA `43749b74fdf57e360164491e3a73b36065d020186613fdc794003baa451e9759`。同签名792正式ZIP：456824503字节/SHA `881308734d4c723b25291d0ac819009e29552650e8085608fba15de91c02e3c1`，仅用作失败后的同身份同版本应急材料，**不是旧运行二进制的字节证明**。两包只传至目标用户权限700的独立暂存区、文件600，目标大小与SHA逐项读回；未停止旧进程时先各自解包，核唯一App、Bundle ID`com.caucy.vibekits`、build2799/2792、完整相同的指定签名要求、Team`26T5WV4GLP`、deep/strict/all-architectures与Gatekeeper。新799主程序SHA`28c7cda317b996467ad85552099c48ef7e4760c109d6ebe7caef7e100ec4f691`，helper SHA`a2373e92cf064eaaf815f020a84731fc15353f6e73fafedf95a68923597e0517`。792签名helper可从旧relay读回原ID、原生公钥SHA`a1131f9cfd10d8932b716a6f8aae80532fae9b0fc4c4ebb264df77d0d3bf5d4d`、callable=true，活动控制连接0。

本任务的目标特定一次性脚本以原PID/出生时间、旧主/relay映射inode、双签名包哈希、私有备份22/22和磁盘余量为硬门禁；`--inspect`只读输出计划SHA`9d7cf95b2c3594ba876834ae336e7fd6735ed163fa8d2da28186c14d448ebe7d`，三个隔离状态转换合同覆盖成功、候选启动失败回退与旧PID未退的阻断。正式`--apply`先重核同一计划，并由目标独立`nohup`进程写原事务状态；只对精确旧主PID及旧relay服务做限定停止，把已验的799 App原子移至原缺失路径，再以LaunchServices启动、核原ID/公钥/实际helper映射。候选失败时会将失败App留证并尝试同签名792应急包；未调用任何“重装清数据”路线。唯一runId对应的目标状态读回`COMMITTED/PASS/rollback=NOT_ATTEMPTED`，新主PID22974、relay PID23054、helper inode180725507；原任务未重放。预检和应用脚本SHA、私有计划/日志与目标终态保存在本任务私有目录，不上传token/用户数据至Git。

## 独立真机读回

严格指纹LAN SSH独立复核原路径App为799/build2799，主/relay SHA与上述正式包一致；真实relay PID23054的`lsof -a -d txt`映射inode180725507等于盘上新helper，deep/strict/allarch签名及Gatekeeper均通过。新helper本机原生status仍返回原仿真ID`5298938227`、原生公钥SHA`a113...`、`registered/callable=true`。随后原控制端`simulator.connect`从此前HTTP500恢复为`connected=true`，原Ccvl指纹、SSH/MCP ready；真实`system.info`命中新PID22974，`device.applications`读回同路径799/build2799，`cluster.rooms`返回原serverId`da3553a32048bfe691d99ad1a27a914b`、原安装key摘要`ce01c0e6f085830e8841609e22beb6712fafadd95f3e39c44109f0d9bfdf0d4f`、kemi业务房与newlink售后房均approved/live。生产只读采样中529心跳从约12小时滞后变为2.61秒，设备档案更新`1.9.0-dev.799`，原六台可联网设备的房间心跳均新鲜；617仍按用户确认关机/断网不连接。

对照升级前本地有效一致性数据库快照：529设备token摘要、owner摘要、安装指纹、两房`approved/revision1`完全相同；session epoch随原进程重连更新，这是新会话代次，不能称身份丢失。原通用Office任务`7ab36135ed5614d317f2987fe530ec0a`的529实例仍`accepted/revision27/fence1`、评分仍唯一`+1 accepted_result`，结果与审核正文哈希及有关的52条消息元数据/正文哈希逐项相同，未重做业务或补造ACK。原KEMI远程办公备用ID`415501605`升级后仍服务器可见在线。

私有保护副本22/22哈希不变，目标源19份仍逐字节相同、3份`cluster-task-messages`发生缩小、缺失0。逐JSON键比较，移除/新增仅`consent-renew`与`consent-*`临时键，公共消息条目0修改；没有`m-*`业务消息键被移除，且上述独立服务端Office审计完全不变。旧副本与同签名792应急材料仍留待完整验收，不把临时键轮换当用户聊天丢失。目标`ui_inspect`显示新PID22974的主窗口可见、AX授权与输入启用，无重复系统授权。一次显式固定工作区零工具`cluster.model.verify`仅返回`request_started`，随后生产心跳报16:53Z `modelReady=true/modelStatus=ready/credentialStatus=valid`，未重试模型请求；这不代替真实当前会话问答与工具全矩阵。

## 边界

受控脚本的终态及本轮仿真/房间/身份/审计证明529恢复了原ID与集群通道，但当前运行旧792 inode的原字节无法追回，792应急包只是同签名同版本回退；不能宣称精确字节回退保证。529完整GUI/IME、工作区文件读写、旧会话正文、手机同账号协同、严格长空闲及同签名移除重装仍待真机验收。其他两台Windows未覆盖最新合格签名包，617离线，原Office任务七台全闭环和G08撤销/百台真实扩展亦继续BLOCK。
