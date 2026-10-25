# Mac 更新器原生 helper 映射 inode 门禁（源码阶段）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 缺陷与范围

原 Mac132 的798更新失败后，更新器将主程序恢复到723并记录`ROLLBACK/RESTORED`，但运行中的原生服务 PID54678 仍映射失败798 helper 的 inode `12906188249`；当前旧723磁盘helper inode为`12903573822`。既有更新器检查只比对`ps comm`和`lsof -Fn`的路径。目录移动或路径投影变化时，路径可等于当前 App，实际 Mach-O 映射仍属于被拒候选，因此只比路径不足以证明进程族同代。

本次沿现有`verifyHelperMappings`加一条实际字节身份断言：读取当前包内helper的`stat` inode，读取每个匹配helper进程的`lsof -Fni`实际`txt`映射，要求同一记录的**路径与inode同时匹配**。无helper保留`helper_mapping_unavailable`；有路径但inode不同或混合多个helper保留`helper_mapping_changed`。检查仍在仿真gate和只读MCP通过后、写`HEALTH_PASS`之前，候选及回滚两种模式均使用同一门禁；失败不删除包、不清身份、不改授权。

## 负控与验证

在独立源码目录，`test/helper_mapping_contract.mjs`直接提取更新器实际Node函数并用`vm`注入有限的`ps/lsof/stat`回执。旧源码面对“当前路径 + 失败798 inode”时未抛异常，负控按预期失败；新源码对此、失败包路径、无当前helper、一好一坏两个helper均拒绝，当前路径与inode完全一致的正控通过。最终函数三轮各五组夹具通过。

同一隔离工程`test/simulator_update_service_test.dart`整份21项通过，覆盖已有授权复核、失败关闭和暂存合同。定向`dart analyze`退出0，仅有原文件三条info级提示。隔离测试环境初次缺失`third_party`与主线已有的`native_filesystem_spelling.dart`，补齐只读原始输入后同一测试真实通过；该环境错误不是产品缺陷。

**发布限制**：本次未构建、签名、公证或安装新包；没有证明新门禁能恢复Mac132的混合进程，也不改变PID54678。最终候选仍须在构建Mac、445和原132检查唯一主程序/helper映射、旧授权/ID、公证和原30秒仿真gate；若132回滚再次留下混合relay，更新器必须诚实报回滚未完全恢复，不可把主进程可用冒称整族通过。
