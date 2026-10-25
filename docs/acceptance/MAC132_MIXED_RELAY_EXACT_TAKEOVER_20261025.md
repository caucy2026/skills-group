# Mac132 混合原生中继精确接管验收（2026-10-25）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

## 原状态与边界

原仿真ID`1321656264`、macOS12.6.4 Intel、原SSH指纹`SHA256:G73XaZfXCAJjGB793rJdNXr+eHvfl7xbnXGAYZvf5ak`。签名798在该机原30秒gate失败并回滚到723/build2723后，旧主PID54977仍运行；独立relay PID54678（出生`Sun Oct 25 00:48:38 2026`）的实际`lsof txt`映射inode`12906188249`属于失败798隐藏bundle，而磁盘旧723 helper inode为`12903573822`。因此此前不能称完整回滚。原私有90文件保护副本和失败798 bundle保留。本次**未重放798的update_apply**、未清身份/配置、未触碰617。

通过原仿真只读接口先核原主程序SHA`16881754b3b9336549d8eed849eccbaa1c29cb9bfeb9b0133e93c6b0e3306053`、磁盘旧helper SHA`59f2e2d3f2050d756d79d1d13bd2754d0b71b07f0b91a6af798210e3a83f80dc`、失败798 helper SHA`960816de38bbc6f443e27af44b9665a59fb0b91a55dbe9ce12bfe09558f9558f`、原native公钥SHA`7656c766e0c1f0749bd2da9e4426e7193821fb5948e78510342e44a4e30a05c8`。目标房间任务会话0、claims0，唯一观察到的活动控制连接来自本机155；目标卷仍有约7GiB可用。既有`Mac132ColdGuard712-v3.js`只重开旧主程序，不能用于relay接管。

## 独立守护与安全分支

本机私有证据目录`g02-mac132-798-stage-20261025-v1/relay-guard-20261025-v1/`保存精确计划、脚本SHA和模拟合同。守护绑定原主PID/出生时间/主程序SHA、原relay PID/出生时间/失败映射inode、旧正式helper inode/SHA、原仿真ID与公钥。执行必须由单次runId的`go.txt`触发；触发后重新核身份、签名字节与当前连接，拒绝额外控制者。先用当前签名helper的专用`--vibekits-harness-stop`停止**原PID**，只在仍属同一PID/出生时间的延迟退出时才发TERM；不按进程名批量杀。启动旧723正式helper，真实查询原ID/公钥/callable及映射inode；旧helper若失败，最多一次停止并恢复先前同SHA的798失败helper作救援，不继续循环。状态每步原子写入目标私有文件，不在Git保存runId或凭据。

离线合同覆盖：旧helper一次恢复、旧helper失败后798兜底、额外连接与映射变化拒绝、错误触发文件不执行、原生stop拒绝保持旧进程；均通过。目标端`--check`、解析器自检、只读`--inspect`也通过。前三次守护在真正stop前安全中止：第一次短时额外连接；后两次因把“后台空闲0连接”误当作异常。独立诊断证明前台SSH本身会临时产生一条155连接，而后台无调用时为0；最终守护只接受稳定的0连接或唯一已核155连接，其他/多连接持续存在仍拒绝。**三次安全中止没有停止旧relay或改变主程序**；保留原失败状态和诊断，不把它们算成功。

## 本轮真实结果

最终v7守护PID11945已独立arm，目标再次只读`safeToArm=true`；`go.txt`触发后目标私有状态于`2026-10-25T10:05:03.853Z`记录`restored-old-helper`，新relay PID12197、映射inode`12903573822`、state`registered`。独立回读：旧混合PID54678不存在；主程序仍为原PID54977，旧主/旧helper SHA与上述保护基线一致，整包`codesign --verify --deep --strict`退出0。旧723 helper的原生status返回原ID、`callable=true`和同一native公钥SHA。

控制端随后显式断开，再按**原仿真ID**重新连接，连接时间`2026-10-25T10:06:53.146860Z`、原G73指纹不变、SSH/MCP ready；真实`vibekits.system.info`命中原主PID54977。`vibekits.cluster.rooms`返回connected/roomsAreLive=true，kemi测试房`c0985cc4dfeedaf71515ae029fc4cc4f`与newlink服务房`f450c684b868292f67c534b793e26314`均approved；服务器独立`peer_presence`于`10:07:26Z`回原ID online且答复已验证。在线人数是瞬时值，不构成长期稳定证明。

**结论**：Mac132的“旧723主程序 + 失败798中继”混合代次已按原签名身份恢复为同代723进程族，原ID、原公钥、原授权连接和两房间可用性复验通过。G02的统一**新版本**覆盖仍BLOCK：本轮没有新签名公证候选、没有798成功安装，也未完成Safari15/模型/工作区等全功能真机矩阵。下一候选须含主线注册等待single-flight修复和更新器helper实际映射inode门禁，并在132原30秒健康检查及失败回退上重新真实验收。
