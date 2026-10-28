# Windows计划任务：原生权限、未知结果与守护边界

复用同设备已验证的独立升级入口；任务身份使用原登录用户、InteractiveToken、LeastPrivilege、无触发器及单实例，不通过提升权限、改策略或换账户修复观察错误。

TaskScheduler导出的XML会省略默认RunLevel。缺字段不能推出权限异常或最高权限，也不能直接按期望补值当作实际证据。通过原已授权用户的Schedule.Service COM读取Principal：InteractiveToken=3、LeastPrivilege=0；同时核UserId（支持原SID与账号别名）、action精确路径/参数、Triggers=0、MultipleInstances=2（IgnoreNew）及执行期限。显式高权限、其他LogonType或action变化仍须拒绝，不修改任务来迎合解析器。

注册成功不代表执行。先核原任务、控制源码/可执行SHA、初次/历史运行态和唯一事务回执，再启动同一个合格任务。超时先对账，不重新创建或覆盖。只读探针可验证任务通道与父启动器退出后的结果，不能替代真实App退出、全SDK空闲、安装器存活、升级健康确认和原ID/授权验收；普通app_control子进程仍不能承担自覆盖守护。

清理时按原生HResult识别缺失：80070002可能被.NET转换为FileNotFoundException，不只限COMException。删除返回或异常不能单独证明任务仍在/已删；独立复查精确任务，确认消失。不因观察误分类重复删除，不触碰其他任务。

原SDK全会话API如返回401，应经现有获授权认证入口核验；不跳过鉴权，不从UI当前会话、缓存目录或低CPU推断全机空闲。只导出脱敏状态，不输出会话正文或令牌。

收尾只清本次已终态且无恢复依赖的生成EXE：保留源码/编译输入/证据，逐个核SHA和占用，并回读不存在；不删除节点运行库、正式包、用户配置和必要回退。区分逻辑字节与磁盘可用空间变化。

实证：[Windows58独立守护通道](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/WINDOWS58_INDEPENDENT_GUARDIAN_ROUTE_20261021.md)。该实证未做真实App退出或覆盖安装，不引用为整机群通过。


## 已验证的自覆盖闭环与控制端重启恢复

[原619的717→签名732实际覆盖](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/WINDOWS732_ORIGINAL619_OVERLAY_20261021.md)证明的是该设备、该包及列明的核心功能，不是七台/全平台或严格空闲通过。脚本中的PID、路径、哈希、任务名属于一次事务，接手者不能重放。

当已有完整合格回退副本时，可复用其安装目录外的Node及已封存本机依赖；逐项核原清单SHA并做有界原生调用，再决定能否承担守护。递归目录工具超时后优先有界读取已有清单，不盲扫或重新装SDK。工作盘沿用该设备已登记约定，无D设备的原路径例外不推广为通用C盘构建许可。

遇command_requires_uploaded_script等长度保护，按接口要求上传固定脚本后用已有合格执行器运行；不切分、换编码或改策略绕过被拒脚本。注册后核实际任务上下文，再用目标端PID/birth和终态核执行，不能把Run请求成功当安装完成。

Windows58的D盘专用清理曾遇到此门禁：短内联只读/精确单件操作通过，较长的17件批处理被拒为`ssh_command_requires_uploaded_script`。当时`simulator.upload_file`只收`localPath`，默认落用户目录，不满足该机D盘专用约束；原指纹绑定的直接SFTP返回`Connection closed`，旧SCP返回`lost connection`，远端脚本与候选文件回读均无部分写入/删除。此时保留冻结清单、解除自建空暂存，停止该批；不能缩短内联命令、转C盘暂存或把已准备脚本记作已执行。若后来取得合规D盘上传能力，先核同一原ID/指纹、脚本SHA、执行策略和目标身份，再启动新事务。这个案例不意味着所有Windows设备的SFTP均不可用。[原回执与保留范围](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G10_WINDOWS58_OLD_PDB_COPY_CLEANUP_20261028.md)。

后续按用户指明的仿真接口发现更准确的传输能力：目标工具`vibekits.network.download`有`outputDirectory`，在受限同LAN短时HTTP源、固定目标IP和D盘绝对目录下，94B探针及固定`.ps1`均直接下载到D，目标独立SHA匹配；此前“没有D盘上传入口”仅是阶段判断，不能沿用。**上传成功不等于执行许可**：Windows58随后的`powershell -File`仍被本机ExecutionPolicy以`UnauthorizedAccess`拒绝，五份候选回读未删，临时服务/文件/目录已清。遇此策略拒绝就停止该脚本事务，不改策略、不改为内联或其他执行器绕过；保留原文件和回执，按设备管理员已批准的脚本策略/正式入口处理。此路线依赖目标真实catalog、D盘约束与网络可达，不推广成所有设备都有该工具或LAN。[最新同一回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/G10_WINDOWS58_OLD_PDB_COPY_CLEANUP_20261028.md)。

退出App前封存新鲜、私有DACL的数据见证，两轮核集合及SHA；受管依赖链接记录目标而不跟随。独立观察器同时绑定PID/birth和日志更新时间，未知/部分写入的安装终态不能让监控提前结束；未知活跃安装器也不能被重复安装或覆盖回退。成功安装后须清除等待计时器；旧包仍在且只剩辅助进程时，按GUI实际存在性恢复界面，不能按“进程族非空”误判GUI正常。

健康提交以前，从原ID重连，核主机指纹、实际新PID/版本/路径/签名、真实MCP和受保护命令、双向文件SHA、房间实时身份及实际界面。控制端自身重启导致not_connected时，先对账控制端进程/桥，再按原ID重连核同一目标事务，不把目标重新安装一遍。

结束后只清已终态的自有任务登记、生成EXE、夹具和正常原始日志，保留源码、合格包、必要回退及脱敏汇总/证据SHA。升级期资源轨迹与严格空闲分开。ownedDebugOnly空清单不证明普通会话已清；普通QA先凭原始请求回执、真实UI选择ID和完成状态确认归属，再走已授权的产品归档流程。归档不等于永久删除；最终可见回答/模型来源可保留，系统提示及整段历史不入Git。权限拒绝后不得换通道执行同一被拒动作。

本例桌面源1/传统点击菜单失效、源2/1:1可操作，仅是已验恢复路线；切换输入源前后读回并恢复原设置，不推广成IME/粘贴/所有平台输入已通过。
