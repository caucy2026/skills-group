# 快照文件计数与覆盖前保护（2026-10-15）

适用于 snapshot incomplete / scope_incomplete / host/byte_or_count_budget，以及旧包完整快照已不能覆盖当前新数据的升级。保持G1–G5、PAD-D01–D19和固定77项；不得用本页缩减发布目标。

## 先区分预算条件

650的Dart scanner以同一原因合并文件数、单文件、总wire字节和spill资格失败。读取真实元数据及生产谓词，分别检查；只统计目录文件总数不能当成实际catalog认证后的eligible数量。650设备观察集合272文件约5.67MB、最大1.35MB；保守spill计数上界58，排除其他预算条件后定位256计数上限。元数据观察不是原snapshot cut的原子证明，不能称所有272文件均eligible。

修复计数必须同时覆盖Dart wire/scanner/restore、Main Binder/publication/独立native读回、helper protocol/transfer/export/retention；只改生产者常量不兼容。保留原总字节、单文件、spill、扫描和内存上限；增加记录后精确计算编码开销，不能继续假设固定64KiB预留足够。跨语言测试须覆盖实际UTF编码、边界与超界拒绝。旧读者拒绝超过旧上限的快照属于真实回退限制，应明确记录，不能声称向旧Main直接回退可用。

helper最低资格沿实际installed()内max(minimumVersion,requiredVersion)核验；全局required已提高时，不必无依据修改独立凭据最低版本。较新版本不降级。

## 不删除新数据来让旧快照通过

旧generation通过不代表后续新文件被保护。当前快照不完整时，覆盖前保护必须覆盖新数据和旧spill并独立核字节；不清聊天、工作区或生成APK来迎合计数上限。未知事务先对账。受控诊断应先用非敏感fixture验证，再进入经审查的真实数据保护；fixture通过不能当真实备份或恢复通过。

## 真实运行库证明后再确定保护范围

65020在63的Main2650/helper37实测两轮新鲜签名H5证明：55,074个运行库文件、971,087,382字节；剩余CE/DE投影273文件、5,672,184字节、506访问条目、98,724元数据字节、最大文件1,354,831字节，前后完整元数据CAS一致。此时实际合格根只有1个、原始标记保留1个；不得照搬旧方案的2根/4原始文件假设。只排除当前签名APK资产逐字节证明的精确运行库根，未知兄弟目录及code_cache仍保留。该结果证明范围和预算，不证明加密副本、恢复或可立即覆盖。

65017/65018在独立测试包内实际各13项控制通过；负例必须匹配确切Fault代码或AEAD认证异常，任意IO/Keystore异常不能算拒绝成功。65020最终APK独立DEX复核1173类、自有类型无缺失；目录中的旧check_dex模板未执行，不能作为当前门禁，使用实际生成器和最终APK直接解析证据。

host-target只读检查也会停止宿主，须先核当前任务/SDK owner/persistence/worker静默，通过独立LAN观察本UID的PID与启动时间；检查后正常启动一次，再用原仿真ID、真实MCP及仿真隧道ADB核恢复。65020首次启动后重连返回offline，但独立ADB确认Main和relay已启动；随后只读重连及真实工具/ADB成功。保留首次失败，不重复启动或重放检查。准备真实pre-cover保护时，不得照搬“每阶段自动启动Main”的诊断收尾：旧cut比较前重新启动可能产生新数据，须先明确保护、独立校验、覆盖及失败恢复的顺序。

证据：RUN/runtime65020-signed-basis-readonly/root-actual/ROOT_INDEPENDENT_RUNTIME_AND_RECOVERY_REVIEW.json、ROOT_ACTUAL_SIMULATION_ADB_RESTORED.json；RUN/root-fixture65017-65018-actual/ROOT_INDEPENDENT_REVIEW.json。真实capture/restore尚未启用，禁止把本段计入完整备份或发布PASS。

## Android空间查询的实测差异

65006 fixture误从文件系统根目录建立SDS锚点而AccessDenied；改用Context提供的应用专属目录并保UID/NOFOLLOW/FD身份CAS。65007仍SecurityException时旧operation是残留值，不足以推断抛错API。65008在每个外部调用前加不含路径/消息的定位码，实际定位sun.nio.fs.UnixFileSystemProvider.getFileStore。Android12 AOSP实现明确固定抛SecurityException；Mac离线通过不能证明Android支持。不要提权、放宽SDS或重建真实密钥。

65009改用公开StatFs查询同一已验证输出父目录，查询前后核目录身份，保available >= 2*plaintextBytes+64MiB。查询错误/零空间不得兜底成功。实际63非敏感2文件70021B加密写入、独立解密对比通过；65010另一次独立调用复用原alias和ciphertext解密通过，未生成新Key/fixture、未写数据。此时真实私有捕获、显式恢复、Main覆盖后存活仍未完成，不是pre-cover或发布PASS。

## 证据入口

本机RUN以environment-evidence.md为准。对应native-readback65006至65010目录保原失败、ROOT_ONCE_TRANSACTION、实际结果和Main恢复回执。65009原安装后只读context超时，续作先验已装SHA，只执行尚未发出的fixture，没有重装。65010的ROOT_INDEPENDENT_EXISTING_FIXTURE_REVIEW区分真实读回与尚未证明的覆盖持久性；不得输出私有fixture引用或Key。

公开上游参考：https://android.googlesource.com/platform/libcore/+/refs/tags/android-12.0.0_r1/ojluni/src/main/java/sun/nio/fs/UnixFileSystemProvider.java （上游参考不是vendor二进制同源证明）。
