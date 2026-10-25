# Harness 调试会话清理

用户要求清理调试环境时，先复用当前项目维护记录和精确来源清单。自动描述员为零、ownedDebugOnly 空列表，都不能证明旧版或普通会话已清干净。

枚举新旧 Harness profile 的 canonical、普通 session、分析员、workspace/pin/archive 和投影。按实际输入、工具事件及任务台账确认调试 ID；正常业务、未知归属和在途队列保留。使用产品 SessionStore 永久删除，不用归档遮住记录。

先整批预校验允许集合，避免前几条已删除才遇到未授权 ID。独立守护绑定原 PID、出生时间、应用哈希及实际空闲状态，等待 owner 落盘退出。关闭 owner 可能改写日志元数据：先比较完整用户、助手、工具事件摘要确认对话未变化，再冻结停止后的全部文件 SHA；不能忽略真正内容变化。

重启原路径后回读永久删除账本、canonical、投影、工作区及归档索引，并核实际 UI 选择、原 ID 工具调用和房间心跳。正常业务和空白默认会话仍存在不代表失败。离线设备不能计入完成；同事自行清理不计为本任务成果。

2026-10-16 实证：六台在线设备本轮24条，617离线未清；源码及首败恢复见项目 tool/maintenance/cluster-debug-reset-20261016 和 docs/acceptance/HARNESS_DEBUG_RESET_20261016.md。固定 PID、事务名、路径与摘要不可直接重放。

## 整机历史聊天重置的补充（2026-10-17）

明确授权清理全部 Harness 聊天时，精确列出新旧 profile 的普通、cluster、分析员、归档和投影；空白默认会话及重启后新生成的系统会话与旧聊天分别核验。停止 owner 后仍通过产品 SessionStore 永久删除和 continuation 清理，匹配会话的旧 draft/queued 项一并清除，其他队列不动。对话在预检后变化时先无删除恢复应用，重新核对空闲状态与新内容，不重放旧清单。

大压缩日志超过盘点预算不能当作零事件或空会话；按实际文件大小调整有界读取，并冻结停 owner 后的完整文件 SHA，删除器用流式摘要逐项核验。Windows 原生进程查询与实际 WMI 结果不一致时，对账同一 PID、出生时间、路径和签名，沿普通退出流程处理，不强杀或重启未知事务。

Linux 用真实 XDG 数据目录与 /proc/{pid}/exe、进程出生 tick 核 owner；ps comm 通常是短名称，不能沿用 macOS 完整路径比较后误判“无人占用”。复用原图形会话环境恢复原路径，不输出环境中的凭据。备用远程办公 ID 若仅为设备自报，先核同机身份，不据此要求用户输入密码。

## 六机仅元数据盘点与维护窗口（2026-10-26）

先用原ID/登记主机指纹确认目标，**只计数**新旧Harness profile的canonical目录、普通/cluster命名空间、workspace与归档索引；不输出会话ID、标题或正文，不解压/读取JSONL。Mac可用现有Python或系统Ruby，Windows用已准许的只读PowerShell，不为盘点安装开发工具或改执行策略。Mac445的系统`python3`只是xcode-select开发工具安装入口，改用已存在的Ruby；其可见安装工具进程在本轮前已运行约14小时，不擅自关闭。六台在线设备真实计数见[私有只读范围回执](https://github.com/caucy2026/priv/blob/main/hbbv/docs/acceptance/HARNESS_DEBUG_SCOPE_READONLY_20261026.md)：现用profile canonical目录依155/445/529/132/424/619分别为50/8/5/7/9/6，旧profile目录均0。`ownedDebugOnly=0`不等于这些普通/旧会话已清，也不能因目录存在就认定它们全是待删聊天。

本机155仍有共享App和个人账号/签名在途时只读、零删除；其他设备同理先核owner空闲及原事务。到窗口后再按本技能上文用产品SessionStore、完整事件摘要、整批预校验、正常退出和永久删除，复验canonical/工作区/归档/删除账本及原ID房间心跳。617离线不计入六机成果。
