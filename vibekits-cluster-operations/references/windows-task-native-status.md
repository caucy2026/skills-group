# Windows计划任务：原生权限、未知结果与守护边界

复用同设备已验证的独立升级入口；任务身份使用原登录用户、InteractiveToken、LeastPrivilege、无触发器及单实例，不通过提升权限、改策略或换账户修复观察错误。

TaskScheduler导出的XML会省略默认RunLevel。缺字段不能推出权限异常或最高权限，也不能直接按期望补值当作实际证据。通过原已授权用户的Schedule.Service COM读取Principal：InteractiveToken=3、LeastPrivilege=0；同时核UserId（支持原SID与账号别名）、action精确路径/参数、Triggers=0、MultipleInstances=2（IgnoreNew）及执行期限。显式高权限、其他LogonType或action变化仍须拒绝，不修改任务来迎合解析器。

注册成功不代表执行。先核原任务、控制源码/可执行SHA、初次/历史运行态和唯一事务回执，再启动同一个合格任务。超时先对账，不重新创建或覆盖。只读探针可验证任务通道与父启动器退出后的结果，不能替代真实App退出、全SDK空闲、安装器存活、升级健康确认和原ID/授权验收；普通app_control子进程仍不能承担自覆盖守护。

清理时按原生HResult识别缺失：80070002可能被.NET转换为FileNotFoundException，不只限COMException。删除返回或异常不能单独证明任务仍在/已删；独立复查精确任务，确认消失。不因观察误分类重复删除，不触碰其他任务。

原SDK全会话API如返回401，应经现有获授权认证入口核验；不跳过鉴权，不从UI当前会话、缓存目录或低CPU推断全机空闲。只导出脱敏状态，不输出会话正文或令牌。

收尾只清本次已终态且无恢复依赖的生成EXE：保留源码/编译输入/证据，逐个核SHA和占用，并回读不存在；不删除节点运行库、正式包、用户配置和必要回退。区分逻辑字节与磁盘可用空间变化。

实证：[Windows58独立守护通道](https://github.com/caucy2026/vibekits/blob/main/docs/acceptance/WINDOWS58_INDEPENDENT_GUARDIAN_ROUTE_20261021.md)。该实证未做真实App退出或覆盖安装，不引用为整机群通过。
