---
name: hbbv-server-build-deploy
description: 整理、测试、打包、备份和部署hbbv房间与能力管理服务器源码，保留服务器身份、设备授权和持久数据；不用于hbbc或RustDesk hbbs/hbbr发布。
---

# hbbv服务器源码交付

先读取目标项目AGENTS和本机环境规则，确认源码、部署目标与当前活动任务。源码包含server/、web/、contracts/、client/、quality/和docs/；运行入口、依赖及部署参数以当前源码为准。不要把网页更新可见当作Python模块已重载。

## 构建与验证

当前服务器是Python/SQLite源码运行项目，无需C/C++或Rust编译。使用Python3.10+专用虚拟环境；现场已验证Python3.12。在机器规定的构建目录创建环境，执行`python -m pip install -r server/requirements.txt`，保留锁定依赖，不顺便升级。当前锁定jsonschema4.26.0、cryptography50.0.1，以实际文件为准。

设置TMPDIR到项目专用可再生目录，`python -B -m unittest discover -s server -p 'test*.py' -v`。针对修改运行必要测试；真实HTTP测试需要允许本地监听。源码测试、合成100节点并发和真实设备验收分别记录，不能互相代替。当前新增发现/邀请相关27项通过，不等于完整长期稳定或生产部署通过。

## 启动

通用入口`server/app.py`，先执行`python -B server/app.py --help`核对参数。回环开发：

```sh
python -B server/app.py --data-dir /private/hbbv-data --password-file /private/admin-password.txt
```

远端HTTPS按实际目标替换参数：

```sh
python -B server/app.py --data-dir /private/hbbv-data --database-name integration.sqlite3 --host 0.0.0.0 --port 21122 --public-host cluster.example:21122 --tls-cert /private/tls-cert.pem --tls-key /private/tls-key.pem
```

上例是参数模板，不能直接启动或据此宣称目标已部署。新数据库默认hbbv.sqlite3；迁移现有验收数据库时显式选择integration.sqlite3，避免启动空库。密码文件只初始化新账号，不用于覆盖已有密码。现有服务身份、任务签名私钥、设备记录与授权须一起保护；不打印私密材料。

`server/run_local_https.py`是当前Mac双监听验收入口，具有ORICO挂载检查、既有数据目录、专用证书及TLS1.2现场兼容设置；不能原样搬到Linux或把本机限制变为通用要求。生产使用通用入口并按真实环境验证TLS与服务管理。task-execution-scope省略时不启用签名任务上下文；配置范围不等于每设备已获授权，不降低签名租约、本地grant和操作permit门禁。

## 备份、部署与回退

用户已要求只备份main时，沿用项目成熟独立索引备份脚本，普通推送并核验远端树，冲突按双方内容主动解决；不force、不reset、不覆盖共享未提交改动。此项目归档在私有仓库priv的hbbv/前缀。备份源码和说明，不备份数据库、密码、令牌、TLS私钥或设备私钥到Git。

部署前按kemi-server-ports查目标唯一台账，核验listener与已有预留；不得操作hbbc/hbbs/hbbr。冻结通过的源码哈希，私有备份现有SQLite及配置/身份，确认无活跃租约、外部操作或升级事务。沿既有supervisor一次正常部署，记录意图防止重复重载；观察超时不代表进程已停止。

部署后核验实际加载源码、HTTPS证书、原serverId、持久房间及成员、认证隔离、管理MCP目录和逐台客户端心跳/工具。先一台再批量切换；错误保留原配置和数据库回退点，不用新身份或空库掩盖失败。全局接入协作技能的完整真机场景仍待验，不把本技能当作已通过证明。

云端部署收尾必须执行`cloud-build-cleanup`：健康核验后，清理本任务已结束且无恢复依赖的临时编译、测试、解包与传输缓存，并回读精确目标不存在及保留项仍完整。hbbv是Python源码服务也不例外。保留当前服务/venv、源码、数据与身份材料、最新交付和必要回退；staging常混有源码、SQLite备份和正式证据，禁止整目录当缓存删除。报告实际删除字节、保留原因及服务PID/身份/健康前后状态；只做盘点不算完成清理。

从旧release准备候选时，根目录的`deployment-evidence`等历史数据库备份不得被整树复制进每个新版本。使用明确的源码集合或根级排除，保留原证据位置；不能递归按同名目录删除合法源码/fixture。复制后分别核对源码完整与备份未继承，已有`quality/test_release_copy_boundary.py`回归可复用。2026-10-21实测约61.92GB主要为SQLite历史副本，不能把它称为编译大小；备份保留与去重必须另按数据保护规则核验，禁止当缓存整删。

## 当前项目入口

本机源码/README与远端准备记录位于项目hbbv；具体本机路径和端口通过kemi-server-ports本地索引获取。生产21122/TCP HTTPS/SSE已部署，当前状态须实时核验，不沿用早期设计预留或旧PID。2026-10-22缓存治理生产实证、旧端兼容及测试资源预算见[缓存治理部署](references/cache-retention.md)。早期接入设计仍见项目docs/REMOTE_DEPLOYMENT_READINESS_2026-10-06.md与86_SERVER_INITIATED_ROOM_INVITATIONS_2026-10-05.md，不把历史状态当当前事实。


## 已验证部署路线（2026-10-06）

以VibeKits工具为主：remote.list_profiles确认已保存host/port/user及主机指纹；remote.ssh_exec执行有界命令，remote.sftp_upload上传精确文件且overwrite=false。open_interactive返回导航器未连接时，先在VibeKits开发工具打开SSH/SFTP工作台，不换成外部SSH、不绕过主机指纹。保存凭据成功不代表密码认证成功；认证失败优先读取服务器限定长度auth.log，区分Failed password与Accepted password，不输出秘密。

本次实际目标：/opt/vibekits-group，域名kemi-chat.newlinksz.com来自RustDesk部署源码并与服务器hbbc public_base_url及证书SAN一致；21122/TCP由统一台账预留，已检查ss、全部socket与Docker映射无冲突。其他环境从各自台账发现，不照搬此地址。

冻结源码server/web/contracts及逐文件SHA清单；SQLite在线backup生成一致性迁移副本，上传后核对SHA和quick_check。原task-signing-key.pem是服务私钥，迁移前必须满足工具审批对材料与目的地的具体授权；拒绝后不得改名、打包或改工具绕过。授权后限制600，只供原服务身份使用。设备私钥、密码与令牌不打印、不写Git。保存原服务UUID、原成员审批和同一签名公钥；不能让启动入口在缺原私钥时生成新身份冒充迁移。

专用venv使用锁定requirements；长安装用后台原PID及限定日志观察，不重复安装。远端27项邀请/管理MCP测试已通过。独立vibekits-cluster.service以通用app.py启动，显式database-name=integration.sqlite3、原数据目录、可信HTTPS域名及原执行范围；使用Umask0077、NoNewPrivileges、PrivateTmp和只读系统保护，仅数据目录允许写。systemctl daemon-reload只登记单元；启动前核对端口，启动后确认原hbbs/hbbr/hbbc的PID及active状态保持。

设备迁移使用cluster.status保存安全摘要，然后cluster.configure(serverOrigin、trustedHosts、trustedCertificatePem、serverSimulationId)。公网受信证书不带旧自签CA。地址改变后首次rooms可能只返回“发现中”，等待原异步同步再读取；不要因瞬时空房间重复申请。155真实迁移已保持原UUID、安装身份、批准成员并恢复实时入房；其他设备与云端心跳须分别核验，不能凭数据库历史批准称全部在线。仿真连接与房间心跳分别验证，离线桌面不得恢复。

公网管理台使用原管理账号及浏览器正常认证，不将令牌放URL。展示给用户前核验真实页面；公网部署、基础入房和27项隔离测试都不等于完整任务执行、评分或100台长期协作通过。

## SSE / SQLite 关闭竞争（2026-10-11）

客户后台Linux测试曾在27个通过点后以-11退出：ThreadingHTTPServer的daemon SSE线程仍可能读取共享SQLite，不能无锁close。沿现有Store.lock关闭并幂等标记_closed，events及REST/MCP入口在锁内拒绝已关闭访问；不要把线程异常当网络离线。复用test_store_close_lifecycle及真实SSE回归，冻结后Mac/Linux各297项和5轮SSE通过才切换。保留原失败日志，生产原身份/成员/客户、其他服务PID及实际HTTPS资源哈希分别读回。真浏览器工具被拒绝时标明未验，不以资源200代替UI，不换自动化绕过拒绝。实际部署证据在项目docs/acceptance/CUSTOMER_DIALOG_CLOSE_RECOVERY_PRODUCTION_20261011.json；数字仅是本次记录，不是后续固定测试数量。

## VibeKits/hbbv 云端容量与本地备份规则（2026-10-21）

生产数据库备份或部署前保护，先读[已验证的只落本地一致性备份](references/local-consistent-backup.md)。2026-10-21已完成真实生产快照和三份本地保留；旧历史“先云端backup再下载”路线不再适用。

本项目用户明确禁止后续在云端创建或保留数据库备份：数据库一致性备份只存本地受控磁盘，权限600、目录700，不入Git。不得先在云端生成完整备份再下载；使用已验证的在线一致性导出至本地方案，或经协调的静止数据库读取方案，不能直接复制正在变化的SQLite主文件冒充一致备份。若本地备份链路尚未具备，先实现并验证，不执行需要备份保障的生产迁移。旧准备脚本含云端backup/数据库复制时不可直接重跑，须先按本规则调整。正式运行数据库、WAL及身份配置不是备份，禁止删除来满足容量指标。

Rust Linux服务优先按`rust-linux-cross-build`在本地冻结源码、测试、交叉编译并核验ELF/GLIBC/哈希，再上传最小交付；hbbv是Python服务，在本地测试后上传必要源码和锁定依赖，无需Rust编译。不在生产云端建立长期编译缓存。用户提出1GB目标时区分临时构建空间与包含正式数据库的服务总空间；现有正式库已超过1GB，不虚报总空间达标，不为目标擅自删业务数据。

用户2026-10-21最终容量约束：hbbv云端项目总磁盘占用目标为3,000,000,000字节，禁止云端数据库备份。数据库备份只在本地保留最近3份已验证的一致性备份；每次新备份完整性/哈希核验成功后才淘汰更旧备份，失败或不完整文件不占保留名额。不得为了凑满3份制造重复备份。清理后以实测分配空间验收；正式库、WAL、签名身份、运行依赖不当作缓存删除。超过限额时查明增量并报告，不静默删除业务数据或擅自扩大付费预算。


## 外部分发门户的目录归属

部署包含 `web/vibekits` 的后台新版本前，核对当前实际入口及 source-main-manifest 的 externalDirectories。已由 vibekits-distribution 管理的门户必须保持指向 `/opt/vibekits-distribution/current` 的符号链接，不得复制或解引用成随后台冻结的旧静态目录；本机路径按现场映射。部署后核验链接实际目标、正式门户资源哈希与动态下载目录。外部可变目录不冒充后台 core 文件哈希，分别记录后台源码 SHA 与门户来源 SHA。2026-10-22 实测发现后台复制目录导致 current 更新不生效，恢复链接后无须重启服务；清理旧副本前须逐文件证明与保留回退源一致。

## 账号协作发布的健康端点

服务身份读取`GET /api/v1/service-info`的`serverId`；账号协作开关读取`GET /api/v2/account/capabilities`的`apiVersion=2`及严格布尔`enabled`。service-info没有`accountCollaborationEnabled`，不能据此误判关闭或触发回退。与授权计划中的serverId和开关值逐项比对，缺字段、类型错误、错误身份均拒绝；旧版不支持能力端点时明确记为旧版/不支持，不能伪造false或冒充支持v2的新候选。

可复用当前hbbv main的`tool/runtime_release_health.py`；它固定两端点、保持TLS验证、拒绝重定向并限制响应大小。`enabled=true`不等于SDK/Phone全链路就绪，`fullHarnessCollaborationReady=false`也不是服务宕机。2026-10-24已有Mac/Linux各6项检查器回归和8项真实TLS启动合同；这些合同是非交付证据；之后生产已按账号协作关闭配置部署，并补验真实房间文件工具。仍不能将其当作Phone/SDK全链路、统一舰队或完整功能通过。部署编排的原事务、资格及最终功能门禁仍需现场核验。

warning过滤的systemd命名空间须同时核验实际流等级：警告文本不会自动决定journald优先级。hbbv已验证配置为stdout=null、stderr=journal、SyslogLevel=warning，并用真实Python诊断发射器的一次明确标识故障注入确认Priority4落盘，不请求生产业务或新增周期采样。更新日志设置后只对账原重启的PID、目录和健康，不因瞬时观察缺失重复重启。


## systemd进程就绪与原事务对账

`Type=simple`的restart返回与MainPID变化不是应用就绪证明。复用项目main的`tool/runtime_service_readiness.py`，固定模块SHA：核systemd配置目录、真实/proc/cwd和exe、PID及startTicks连续两次一致，再进入HTTPS身份和版本化能力检查。错误配置/failed必须拒绝；过渡目录、0PID或消失进程有界等待。超时保留原事务及输入，先查Job和实际进程，不用第二次restart掩盖未知结果。回退同样等待真正旧进程就绪，不能将早期/目录快照写成恢复完成。

旧`tool/maintenance/account-backend-20261024/deploy.py`入口已退役；新账号启用入口在`tool/maintenance/account-enabled-sdk-20261024/`，先读其README与当前资格。2026-10-24修复经过Mac/Linux各8项合同及真实旧实例只读复验；新候选正向启用仍未通过，不能将这些证据写成已上线，也不能自行恢复事故执行者资格。
