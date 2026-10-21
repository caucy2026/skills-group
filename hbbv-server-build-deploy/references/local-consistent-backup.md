# 只落本地的一致性数据库备份

仅用于已获服务器读取权限、已有可信保存SSH档案的hbbv运维。源代码入口是项目`tool/local_database_snapshot.py`、`tool/local_database_snapshot_worker.py`；现有数据库含配置、账号、令牌等私密数据，备份及中间流不入Git。服务器任务签名/TLS材料继续原位保护，数据库快照不代替它们的独立身份保护。

## 经验证的方法

通过VibeKits现有`remote.ssh_exec`和`sftp_upload/download`，保留原主机指纹校验。发送端只打开`mode=ro`、query_only的SQLite连接，在WAL下BEGIN后首次SELECT固定快照；不暂停写入、不调用BEGIN IMMEDIATE、不生成云端SQLite副本、dump或压缩包。只有一个临时0700运行目录和0600 Unix socket，无新增公网端口。

发送端按原schema/类型流式读取普通表；保留TEXT中的NUL、Unicode、BLOB、64位整数、浮点、普通表ROWID、WITHOUT ROWID主键顺序和sqlite_sequence值。当前项目不支持的虚表、生成列和额外内部统计表会拒绝，不能静默遗漏。直接SQL iterdump在本次NUL夹具中丢数据，因此不将其当完整替代。

接收进程先在本地产生X25519临时密钥，仅把公钥送给发送端；私钥只在该接收进程内存中保留。HKDF/AES-GCM把job、原serverId、序号和包类型绑定。工具stdout中只有密文，避免SSH工具调试记录落下数据库字段；不是通过编码绕过工具拒绝。每个512KiB密文分块的控制帧小于900000字节，原SSH单次1MiB输出上限保持。

当前预算：单记录16MiB、明文流8GiB、压缩接收1GiB、发送端虚拟内存256MiB/CPU120秒、低优先级及约35%单核平均CPU预算（计自然传输等待，短时信用最多1秒）。网络分块有ACK；发送端仅缓存一个未确认密文块，原请求丢回包时先核对原PID/创建时间/job，再重读同ACK，不建第二个未知快照。断开、空闲60秒、总期限900秒或WAL增长128MiB保护会释放读取事务。

开工前实测项目分配占用；加128MiB WAL余量和32MiB保守余量后必须仍低于3,000,000,000字节。必要数据已不够时报告缺口，不删正式DB/WAL、不放宽预算。CLI示例的连接/内存等参数按原部署核对，不能拿历史快照当当前值。

## 执行及验收

1. 核对保存档案、HTTPS原serverId、实际服务PID及其数据库FD、WAL模式、schema支持情况、当前是否有同一备份在途。源端只上传两份有SHA清单的程序；禁用.pyc写入。运行目录短于Unix socket路径上限，状态只记公共计数/固定错误码。
2. 本地备份目录700、文件600，私有retention-index.json与目录实际保留集合一致。先保留全部有效旧备份；读取锁防止同一目录并行修改。空间至少覆盖数据库重建及排序临时量，另留当前任务/机器规则要求的余量。
3. 同一接收进程持有临时私钥，调用SnapshotRecipient.collect；每个已落盘分块才推进ACK。完整密文manifest校验压缩字节及SHA，随后finish原job。实际PID结束、读取事务释放分别核验，不能只看COMPLETE文件。
4. restore_verified在本地新建、绝不覆盖旧备份。检查解压完整性、全记录SHA、每表计数、schema、原serverId、quick_check，并逐行重读普通表计算逻辑摘要。额外核对pragma和序列值。它是逻辑一致性快照，文件布局/SHA不要求等于在线主文件。
5. 新文件验证后才能正式归档，再按源快照日期淘汰旧备份，只留最近最多3份已验证备份；不按今天复制时间排序、不制造重复备份凑3份。删除旧文件前核精确路径/Hash/占用，未知或在用则保留并报告。临时压缩流和失败片段不登记为有效备份。
6. 确认原job终止后，保留脱敏回执和已知首败，清理本次匹配SHA的云端程序复制件/状态/socket/空日志及本地无用中间流。读取DB、WAL、原服务UUID和HTTPS仍正常；不整删staging或动其他任务。仍执行cloud-build-cleanup。

外部Mac缺少注册工具时，项目`tool/examples/backup_external_controller_example.py`与`finalize_external_snapshot_example.py`是成功路线的环境变量模板，不是自动发现或新环境的一键安装器。必须先准备当前只读preflight和明确的既有三份保留索引，逐项设置HBBV_*环境；具体远端布局、Python路径须匹配本团队部署。模板不内嵌账号、凭据或本机路径；其他控制环境按其已授权MCP接口映射相同协议。

当前实证与完整回执索引：项目`docs/acceptance/LOCAL_CONSISTENT_DATABASE_BACKUP_20261021.md`。首轮WAL保护失败未改旧备份；第二轮成功后本地正式保留三份、云端仅余原服务/DB/WAL及依赖，不把“片段已收到”算完成。
