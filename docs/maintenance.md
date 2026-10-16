# 监控、调试记录与磁盘清理

## 三层监控

分开记录房间心跳/角色、原ID真实工具可达、系统与App/helper资源。心跳新鲜不证明模型或工具正常，短时正常不等于24/72小时稳定。断线用有界单飞、退避与原事务恢复；不持续截图录像、忙等或创建无意义模型任务。

严格空闲CPU/RSS测量先核真实业务场景和当前工作，不能停别人任务。区分单核等效与按核数归一，沿项目原门槛，不用低数值替换失败。未知指标标未知，不填0。

## 清理调试会话

仅清已登记自有调试ID，覆盖当前与旧profile、普通调试与自动描述会话；不能凭标题/年龄判断归属。先用真实SDK元数据核owner、状态和持久队列，忙碌拒绝。默认保留业务会话与历史，不用清空整个Harness目录当恢复。

metadata_list若scope=ownedDebugOnly或legacyInventoryComplete=false，只能证明对应调试集合，不能证明全部用户会话空闲。需检查真实当前SDK/UI/任务状态后再安排升级或资源验收。

## 日志规则

普通原始日志/临时采样最多24小时；错误、警告和崩溃最多7天，按级别限量轮转，启动清过期记录。保留脱敏正式报告与证据索引；不留Key、PIN、token、私钥、聊天/剪贴板或文件正文。旧格式先核归属并提取有效期关键证据；未知文件和活跃writer不强删。

## 磁盘与构建缓存

盘点本任务索引、保留集合、当前进程/占用和可再生性，核精确目标后清旧生成物。目录名或年龄不单独证明能删。保留源码、未提交改动、Git、配置、签名材料、当前正式包和必要回滚。不停止活跃构建/签名/发布换空间。

按本机LOCAL-ENVIRONMENT-RULES选择构建盘；同事没有外盘不照搬别人的ORICO路径。Windows设备按已登记盘约束，不能自行改成C盘编译。

清理后读回目录和实测可用字节，验证App、原ID工具和房间心跳仍正常。不把删除命令返回0当环境干净，也不重复清理已完成范围而误伤新业务。

## 完整技能与深入阅读

- [资源与恢复经验](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-work/references/resource-recovery.md)
- [调试清理](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-cluster-work/references/harness-debug-reset.md)
- [磁盘清理](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-storage-cleanup/GUIDE.md)
