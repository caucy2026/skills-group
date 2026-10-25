# Mac529 下一签名包前的数据保护基线（2026-10-25）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

原仿真ID`5298938227`对应目标`kemideMac-mini.local`，沿登记LAN地址及独立Ed25519指纹`SHA256:Ccvlq/fFq7TtnCOFhZpJ4UMwUqOJeupvuuGEVl600/c`只读连接。原主进程PID68784仍运行，出生`Sun Oct 25 06:21:21 2026`、命令路径指向792缓存App，但该`.app`当前磁盘不存在；正式`/Applications/Vibekits.app`为旧723，不得据此覆盖/降级。生产hbbv的529业务房/售后房历史成员均approved，但心跳已停约6小时；hbbs仿真在线与真实集群在线分开记录。

先复用项目既有四个VibeKits用户数据根和限定文件类型，对工作区设置、会话、continuations及任务消息做**只读盘点**：22个文件共1,125,724字节，单文件/总量均在旧保护脚本的32MiB/256MiB界限内。目标卷约32.9GiB可用。随后只在目标用户`Application Support/.vibekits-cluster-backups/preupgrade529-20261025-v1`创建一次不覆盖的私有副本；原文件逐项冻结设备号/inode/大小/mtime，复制后源与副本重新计算SHA-256并复核源元数据未变化。私有manifest SHA256为`5d606abb4ba64aa630484f22d94ad14d51ff60346e86aa707017ffc7bd815dd1`，记录22份、1,125,724字节、allCopiedAndRehashed=true。独立第二次读回22个副本全部与manifest大小/hash一致，备份目录700、文件与manifest600。**用户聊天和文件正文未进入工具输出、Git或报告。**

备份后另用macOS真实`ps -p 68784`确认原进程出生时间与路径未变。此前一段诊断草稿用`/proc`是否存在表示“进程仍活着”，该字段在macOS没有证明力，已丢弃，未作为本报告或升级门禁依据。Keychain、系统授权和原安装身份不能由上述22个文件副本代替，覆盖前仍须独立核原公钥、签名/Bundle身份、权限及运行中的进程；若备份后用户数据继续变化，安装前须按相同限定范围刷新保护点并核旧副本保留价值。

本轮**没有安装、停止或重启529**，没有恢复缺失的缓存App，也未把792运行路径缺失等同整机离线。下一步等包含当前集群/账号修复的同一合格Mac签名公证包，沿已授权LAN SSH/原仿真恢复流程做同身份覆盖与原ID/MCP/房间/数据连续性验收；不能拿已装旧723伪造修复或把只有版本号相同的本地792候选当作原进程逐字节证明。
