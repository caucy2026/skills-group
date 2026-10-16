# PAD CPU 定位：已验证路线

先保存无干扰 300 秒基线，绑定最终 APK SHA、UID、PID/startticks 和控制端生命周期。采样期间不调用 MCP、不操作 UI、不重启进程；短时栈采样不是空闲基线。

## 标准系统 Perfetto

63 的普通 shell/simpleperf 和 debuggerd 曾被拒绝，不能提权或修改 SELinux。后续已验证另一条标准系统路线：实际 userdebug 系统的 `linux.perf` producer，由已有 traced_perf 权限采集授权目标。不能据此推定普通 user 系统、其他设备或应用自身也有权限。

每台先只读核系统类型、producer 注册和实际版本；不运行会改全局属性的 prepare。实际 63 为 userdebug、Perfetto v15，未修改属性、应用 profileable/debuggable 或权限。

沿 RUN/perfetto-cpu647-offline-plan 的原执行器：精确正整数 target_pid、fresh quiet、包/UID/PID/starttick 核验、唯一事务与输出路径；仅 linux.perf，kernel_frames=false，短时、文件大小有界。不得加入 ftrace、GPU、heap、全机 bugreport 或其他应用采集。未知录制先对账，不重放。

实际教训：

- 首轮 19Hz/10秒取得4个目标样本，DISCARD 与写文件模式产生配置警告，保留原 trace。
- 改用 RING_BUFFER、flush_period_ms=5000 后配置警告消失；99Hz/30秒、32页 ring 仍有1689条 kernel overrun 记录，因此不能用样本比例推算 CPU 占比。
- Main 的49Hz/30秒、256页 ring 取得56个精确目标样本，未见 perf_lost 计数，但9个 unwind_error 仍须保留。
- kernel_frames=false 只抑制内核调用链，不等于 cpu-clock:u。
- 不因 v15 标签就认定新字段失效：实际解析与目标样本才是证据。

## 解析与符号

优先复用现有 trace_processor；缺失时使用官方独立工具并核官方哈希，放任务自有 ORICO tools，TMPDIR 同样在外盘，不覆盖其他工具。本次已验证 Mac arm64 v58.2，SHA256 `d29864d1ba3b36855527bb1b0ca3aa7f703cdce338b9680bb922c5c151b358fa`。

先查 perf_sample 的目标 PID、TID、unwind_error 和 stats。公共报告只保模块 basename、相对 PC、数量与错误，原 trace 保持私有。stack_profile_callsite 的 depth0是线程根，叶节点为 sample.callsite_id，不能把 __start_thread 误报成热点。

base.apk 中的帧须结合 APK成员 payload offset、mapping offset/load_bias 和 ELF可执行段页对齐，frame.rel_pc 可能已是 ELF虚址，不重复减 APK偏移。C6来源见 native-build-provenance.md。

同构建 .a/.rlib 的局部字节匹配只是候选；必须核符号范围、真实重定位字段和直接 BL目标，不能把 object偏移或最近导出符号当最终地址。此法已将647的热线程入口绑定到 hbbs_http::sync::start_hbbs_sync；不代表全部CPU根因或发布通过。

官方依据：[Perfetto CPU profiling](https://perfetto.dev/docs/getting-started/cpu-profiling)，以及 AOSP android-12.0.0_r34 的 producer_support.cc、traced_perf.te 和 perf_event_config.proto。所有旧拒绝、首轮配置问题和损失统计保留。


## 已安装Dart AOT的离线符号恢复（2653实证）

已有最终包缺Dart符号时，先找对应冻结源码 `.dart_tool/flutter_build/<本次ID>/app.dill`、原arm64-v8a/app.so、该次Flutter SDK的gen_snapshot及其实际默认参数。2653使用原kernel/原compiler、原`--deterministic --snapshot_kind=app-aot-elf --strip`，只增加`--save-debugging-info=<独立输出/app.symbols>`并把elf输出指向自有ORICO目录；原事务50523终态0，生成app.so与原编译输出整体字节一致。不得擅加`--dwarf-stack-traces`、重编内核或拿其他版本符号套当前栈。必须核输入与工具SHA、输出原事务；正式APK可能经AGP改变ELF元数据，所以另核最终APK中.text/.rodata的地址与全部字节及GNU build ID一致。未通过精确绑定不得用addr2line结果认定故障方法；这不是新APK验收，也不修改已安装程序。

APK内库映射需逐mapping判定容器原点。2653实际libapp ZIP payload557056、RX文件偏移/虚址6356992、映射exact_offset6914048；同VA/buildID有start_offset557056的内库映射及start_offset0的APK容器映射。只有后者须减去557056；前者原PC已是ELF地址。用ZIP实际本地header长度、ELF PT_LOAD、trace mapping字段联合推导，不能只按哪个函数看起来合理选偏移。未经校正时把MCP递归验证误读为NaCl或布局，2653已保留候选与纠正记录。官方字段定义：[AOSP Mapping proto](https://android.googlesource.com/platform/external/perfetto/+/8d9b0dfd620b6c555ff67d998f3500013a01a561/protos/perfetto/trace/profiling/profile_common.proto)。

本次74个精确宿主样本、Main50且25有unwind error；currentJson仅6个真实叶/7个inclusive，不按帧重复数冒充独立样本或CPU占比。校正是强定位线索，不单独证明唯一原因或新实现通过。实际低开销改善仍须同签完整包的有效300秒原性能门槛与相关历史回归。
