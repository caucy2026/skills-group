# G09 一万成员离线合同复验（2026-10-25）

Session-Name: vibekits 集群开发  
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2

从当前hbbv源码在本机运行两项现有合同：`test_room_device_summary.RoomDeviceSummaryTests.test_ten_thousand_synthetic_members_have_bounded_summary_pages`和`test_service_auto_assignment.ServiceAutoAssignmentTests.test_actual_ten_thousand_offline_members_send_next_device_to_slot_two`。首次使用工作区自带Python缺`jsonschema`，测试尚未执行；随后仅在ORICO本任务临时目录建立Python3.12隔离虚拟环境，按项目`server/requirements.txt`安装`jsonschema==4.26.0`、`cryptography==50.0.1`及依赖，未改源码/生产服务。

正式重跑两项均PASS，`Ran 2 tests in 3.969s / OK`。合成1万成员房间的管理摘要第一页恰100台、约114357字节，局部查询耗时约0.0086秒；满1万离线成员后的下一台自动分到服务房2。数值只反映本机合成夹具和该次查询，不表示生产1万人同时在线或长期重连通过。生产实际登记/新鲜设备仍由独立只读采样确认；100台以上真实扩展、24/72小时稳定与持续资源曲线继续BLOCK。

测试临时venv和uv缓存均为本会话创建的可再生依赖输出，测试进程已退出。删除前两者分配占用分别`15920 KiB`与`19644 KiB`；按精确路径确认无打开句柄后顺序删除并读回均不存在。ORICO实际可用字节分别增加`151552`与`20492288`，合计`20643840`字节；venv的大部分内容由APFS共享/克隆，不能把逻辑占用直接算作物理释放。正式证据文档保留，未删除源码、数据库、工具链、正式包或别人的生成物。不把本地依赖安装计作云端构建或正式包交付。
