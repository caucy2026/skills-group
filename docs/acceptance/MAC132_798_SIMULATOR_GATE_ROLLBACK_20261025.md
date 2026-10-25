# Intel Mac132 使用最终798包覆盖时仿真门禁失败并自动回滚（2026-10-25）

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

**当前结论：132没有升级到798，G02仍BLOCK。** 原设备1321656264/macOS12.6.4/x86_64保持原仿真ID、公钥、授权与业务房；运行中的正式App已由更新器自动恢复为723/build2723。不能因798包在本机和445通过、目标磁盘曾短暂显示798或控制端apply调用已发出，就把132计为升级成功。

## 冻结输入与一次原事务

使用个人账号会话已签名公证的**同一最终ZIP**，456830108字节/SHA256`815c1e3d484cca0fe87c1c8ec01d36b362daa61aa98bf2487fc8048c92a10579`。本机独立验证Universal x86_64+arm64、最低macOS12.0、Bundle ID`com.caucy.vibekits`、Team`26T5WV4GLP`、指定签名要求、deep/strict/allarch、Gatekeeper、stapler全部通过；候选主程序SHA`8f762c1c270eb67589ef8b4a8b959ab6c90fdf57fa6e3fea9e95ed35ec357d09`。主线自该包冻结后仅追加文档与Windows专用集成文件，未用旧包冒充新源码。原132运行路径`/Users/mac/Library/Caches/Vibekits 2.app`、build2723、旧主程序SHA`16881754b3b9336549d8eed849eccbaa1c29cb9bfeb9b0133e93c6b0e3306053`；原G73 SSH指纹、bundle/Team/指定要求与候选逐项核对。原后台两个房间approved、心跳新鲜、taskSessions0、Harness busy0/waitingApproval0、磁盘空间满足6GiB门槛。

ZIP按唯一命名14块传入，目标每块独立SHA、整包再次SHA均一致。14块和本任务上传的备份脚本已精确清理，完整正式ZIP保留。覆盖前在目标用户私有Application Support另建独立数据快照，90个规则内文件/514884字节复制并逐件复算哈希；没有导出聊天、Key或凭据。原设备身份、运行PID25907与旧包字节在提交前再次核验。`update_stage`一次返回staged=true、hash/字节与本候选一致，无原在途更新。仅调用一次`update_apply`；控制端等待35秒超时后**没有重交令牌、没有新建更新器、没有通过SSH运行脚本或关闭安全闸门**。

## 原更新器的终态与恢复

同一原更新器PID53678的公开事务记录于2026-10-25T07:48:53Z为`phase=ROLLBACK`、`code=FAILED`、`rollback=RESTORED`。候选798进程PID53983已于07:48:17Z真实启动，但原30秒健康检查在07:48:47Z为`HEALTH_FAILED / simulator_gate_not_ready`；旧723回滚在07:48:53Z为`HEALTH_PASS`。这是明确的候选仿真门禁失败，不是单纯控制端超时。更新状态最终receiving=false/applying=false、无staged，目标磁盘和实际运行均回到723；新旧候选没有混合运行。

独立回读旧723主程序原SHA、deep/strict/allarch签名、原仿真ID及nativePublicKeySha256`7656c766e0c1f0749bd2da9e4426e7193821fb5948e78510342e44a4e30a05c8`、当前relay callable=true；目标`vibekits.system.info`实际命中新PID54977、`cluster.rooms`仍connected/roomsAreLive=true，服务器房间与心跳继续新鲜。90个保护文件没有缺失；85个逐字节不变，2个仅MCP/任务运行时endpoint、PID、临时token随正常进程重建变化，3个`cluster-task-messages`仅短期consent-renew条目轮换，JSON其他路径均相同。原始与当前内容均保留，不以回写旧数据掩盖差异；**不能称90个全部字节相同**。用户聊天和其他受保护正文未被本报告读取或上传。

已签798失败候选bundle留在目标隐藏`-failed.app`供诊断，目标读回主程序与helper分别和本机最终候选SHA一致、深签有效；该失败bundle的只读helper status在回滚后看到原设备ID/公钥，不能反推候选运行时曾注册成功。目标旧723当前helper仍是旧正式SHA，不存在未验证的新版helper占据中继。

## 已定位与未证明的原因

候选PID53983的DSH/Web诊断多次ready，启动阶段总耗时约3.5秒；失败点集中于仿真原生中继。旧relay在07:48:20Z收到close；新relay开始IPC后，07:48:22/23/25Z向多节点登记均返回`Cluster registration refused: SERVER_ERROR`，约07:48:30及07:48:43Z另有relay启动尝试报`Address already in use`。这与健康检查一直看不到原仿真gate ready一致，**但尚不能判定SERVER_ERROR的服务器内部根因，亦不能把第二个IPC竞争当唯一首因**。生产hbbs当前主机的窄时间日志未提供匹配条目；目标时间戳按UTC换算无明显时钟漂移。不得简单延长健康窗口、跳过原生来源校验、使用旧helper混装或靠重启/重复apply凑PASS。

备用远程办公ID372799163在界面可见在线，电脑操作接口本轮返回`noWindowsAvailable`未取得可用画面；按原G73指纹验证的LAN SSH公开密钥认证被拒绝，未绕过。故本轮在原仿真恢复后用原MCP/SSH只读回执和服务器权威心跳完成对账，不能宣称备用桌面UI已验收。

## 下一步门禁

Mac原生负责会话需在隔离环境定位798对旧macOS12的注册`SERVER_ERROR`与relay单实例/IPC竞争，保留本首败，做负控和真实旧723→修复候选同身份覆盖。修复后重新构建、Developer ID签名、公证同一Universal包，先本机及445完成受影响回归，再在132复测30秒原门禁、Safari15兼容工作区/目录选择/模型与会话、原授权/Key、原ID反向只读MCP、房间心跳与空闲资源。该修复未有结果前，798不能计入132合格版本，也不扩散到529或商城。617仍遵照用户确认的关机/断网保护。

私有原始回执与目标数据备份索引位于`/Volumes/ORICO/kemi-build-cache/app-release-gate/hbbv/hbbv-main-deploy-20261024-v1/g02-mac132-798-stage-20261025-v1/`。本报告不含一次性更新令牌；控制端原等待超时的调试异常曾把该令牌写入本聊天私有工具轨迹，后续同类调用必须捕获`TimeoutExpired`并只记录错误类型，不打印命令参数。该令牌对应事务已终态且目标无staged，不用于重放。
