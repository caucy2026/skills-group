# PAD 原生构建来源与记录追溯

## 当前2657实际C6 b5与relay profile符号输入（2026-10-16）

本节覆盖下文旧“当前591”措辞。Main2657正式APK SHA3fc89666f54763e2ab132e5e75786941d94aad2c4c0545537a8e1a6c07dba4ab中的C6、source657 JNI与`RUN/c6-pad-audit-task-client650-native-build/librustdesk-pad-audit-task-client-stripped.so`完整一致：39604272B，SHAb5cb350cc12dfef246b11134160bde1ff4259e281fc1ddaf1ad5b1305295edad。原82652本地native build终态0，Root核1033冻结输入，本次又按POSTBUILD清单逐SHA全部匹配；精确源根为该目录`rust-source`，不是当前dirty client或仅某个Git HEAD。仅相对qualified649的hbbs_http.rs/http_client.rs/server/connection.rs三处delta，命令仍`bash flutter/ndk_arm64.sh`及原NDK28.2/locked release依赖合同。

raw `rust-target/aarch64-linux-android/release/liblibrustdesk.so`为39604288B/SHAd424ce367cae88dd50d9ea7ba4376bad937b799999eed0f877ecc43b7e49b055。实际raw与strip均无GNU Build ID、symtab或DWARF，只有Android工具链note；不要把raw名字当完整符号。两库及正式APK的.text/.rodata/eh_frame等内容与地址精确相同。当前APK C6为STORE，payload33308672；.text VA13218688/fileoff13202304/23475720B。relay trace map1 start_offset33308672、exact_offset46510080，与RX PT_LOAD页对齐及load_bias16384一致，raw rel_pc已是ELF虚址，不能再减APK或load_bias。证据`RUN/c6-b5-symbol-provenance657-readonly`。

以下保留物是当前必要符号/源码输入，不能按“旧650生成物”清理：同build `.a`408897748B/SHAe3012fb8856512068c296ddbb1217c2c82cc119efc23408fe7ca667e80428508、`.rlib`63777246B/SHA56069e896a147fb1d00e56af4338a7fb4adbe558f851e9f43507d2bda66ac42e、raw/strip库、1033源与Cargo.lock/构建回执。rlib有5698定义text符号，但对象相对PC不是ELF绝对地址，禁止直接rlib addr2line冒充热点函数。先actual mapping/PT_LOAD归属，再按实际函数范围、对象字节和重定位逐边绑定；ICF同体不能唯一指定crate。

Root98863原relay49Hz/30s/256pages trace14702B/SHAc9f8dcc3713206137888a7f5a793cb7fd574586127ae84084650e941786a56e9：35样本全PID17106/start31815892，unwind0，discard1，不能按样本比例算CPU。两个whole-byte fe25519_mul样本4/34的上游已逐6条实际CALL26绑定HBBS sync→post_request→post_request_via_tcp_proxy→tcp_proxy_request→secure_tcp_impl→create_symmetric_key_msg→box gen_keypair，证明这两样本实际raw TCP链，不区分builtin直接raw与HTTP失败fallback；巨async其余重定位未全证，不改密码学、nonce、身份或心跳。HBBS已有Android专属同key HTTP Client复用；direct raw future不await HTTP factory，不能再次猜“每tick必建Client”。精确小proof在`RUN/perfetto-relay657-b5-offline-parse/TWO_FE_SAMPLES_RAW_BRANCH_PROOF_PUBLIC.json`及`HBBS_FROZEN_SOURCE_CHAIN.md`。CPU657正式300秒仍5.572595% FAIL5，不因符号定位授发布PASS。

## 2026-10-15 PAD 自有 C6 适配授权与648候选

用户已明确允许“PAD 自有 C6 适配，官方 SDK、服务器和桌面不动”。本次仅在 Android VibeKits Harness 的 HBBS 专属 current-thread runtime 内复用一个 HTTP Client；TLS类型、证书校验模式和完整代理配置组成缓存键，配置变化替换，构造回退不缓存，退出作用域清空。心跳频率、请求及重试、身份和授权语义保持。该授权不扩大到其他核心或服务器修改。

精确候选入口 `RUN/c6-http-client-reuse648-candidate`；实际原生构建 `RUN/c6-http-client648-native-build`。原始591输入保留。新库 SHA256 `3059927e6e966c21c6cc13f1a63be847d56f5e7373dad843202ac71b841a3365`，39,597,680 B；38个JNI导出和14个FFI声明闭包、动态依赖及身份源码核验通过。不要继续把旧C6 SHA硬套新候选，也不能跳过新库资格检查。

构建脚本 `build.rs` 调用 `hbb_common::gen_version()` 会生成 `src/version.rs` 的 BUILD_DATE。本次原生编译退出0后，冻结检查因这一个日期字段变化而退出1；已独立核原生成器及仅日期差异，保留原失败回执，不重编或忽略其他源码变化。新构建应区分不可变输入和已证生成输出。

Main2648完整包已本地构建和签名核验：381,988,666 B，SHA256 `0134a23412bfb31e3a7cde99787c71cda31fc65dcbc6e6197b56d82fc9ce7171`。构建入口 `RUN/prepare648-c6-http-reuse`；对应64801读回探针已编译资格。此条只记录构建通过，覆盖安装、原Key与完整数据、CPU收益、全77项和商城仍需实机证据，不能沿用647通过项冒称648通过。

排查最终 APK 内原生库时，先从当前完整 SHA 反查本版 release_driver/签名闭包与改动记录，再沿记录引用的 native manifest、source-provenance、build-command 和真实输出定位；不能只查通用 CARGO_TARGET_DIR 或当前 dirty RustDesk/client，不能因 GitHub 没有 Android Actions 就断言没有对应构建。

## 已确认的当前 C6：本地 legacy-registration591

以下 RUN 为环境索引中的 resources-dev523-20261005，不是所有同事的固定磁盘路径。

- 首次完整 Main 引入为 dev591；`prepare591/main-changes.json`、`prepare591/final-native-components.json` 链接 `legacy-registration591/manifest.json`。dev647 的 source JNI 和最终 APK member 均沿用同一库，不是 dev647 重编 native。
- 原始库：`legacy-registration591/rust-target/aarch64-linux-android/release/liblibrustdesk.so`，39,592,880 B，SHA256 `19828a76f1507c1da19a6c0e7cc275ef05c789b1d861fc2e9e14d53839e52c20`。
- 包内库：`legacy-registration591/librustdesk-legacy-compatible-stripped.so`，39,592,864 B，SHA256 `c6f6d5383bf110efc0fbb2ec9177687487df45e7c0014e8914663cee1a8dfcf8`。
- 精确源码：`legacy-registration591/rust-source`。`source-provenance.json` 记录源自 `stable-registration-uuid589/rust-source`，1032 个记录路径；2026-10-15 Root 逐文件重核缺失0、SHA差异0。它是冻结源码加补丁，不可用当前工作树 HEAD 冒充精确历史源码。
- 此层唯一修改 `src/pad_registration_uuid.rs`，结果 SHA `aebb3c5db33187033c8bf6085f5e6bb467edecf280ba8a25293a2d482459c2ae`；补丁 `qualified588-native-legacy-unchanged-pk-only.patch` SHA `9a2b7c73141a2d6464e67a0c4bd208f7f26ce20b4661d8edf9d5d4070cb29097`。
- 用途是既有有效身份的兼容：受保护旧记录公钥与当前公钥完全相同时保留原 UUID 结果；换 Key、错误 scope、畸形或链接记录继续拒绝。不能把它描述为无条件重置身份，不能据此断言它是 CPU 根因。

## 原命令与依赖

复用 target 到新隔离目录时，不假设所有 C/C++ 增量输出可重定位。649实测保留两类失败：host libsodium 的 autotools 状态仍认为已被清理的 `libaesni.a` 存在；libsamplerate 的 CMakeCache记录旧648绝对路径。先读实际失败日志和已终态事务，只将对应crate的生成out重命名保留，再由原build-script生成；不盲改缓存路径、不全量cargo clean、不清原target/源码/工具链。失败的Cargo build-script fingerprint未完成时可正常重跑，不能仅凭目录复制成功声称增量可用。两次恢复均使用新事务和日志，原失败不覆盖。后续清理生成archive时须同步考虑autotools自身状态，不能只说Cargo会自动识别所有嵌套缺失。

原 `native-build-command.json`：cwd 为上述冻结 rust-source，运行 `bash flutter/ndk_arm64.sh`。该冻结脚本实际执行：

```sh
cargo ndk --platform 21 --target aarch64-linux-android build --lib --locked --release --features flutter,hwcodec,mediacodec
```

NDK `28.2.13676358`；CARGO_BUILD_JOBS=4；CARGO_TARGET_DIR=`legacy-registration591/rust-target`，TMPDIR=`legacy-registration591/tmp`；VCPKG_ROOT/VCPKG_INSTALLED_ROOT 用原记录中的现机依赖路径，复用前核当前存在及依赖身份。脚本使用 NDK llvm-ar/ranlib，并对 sodium/FFmpeg 动态未解析导入做失败门禁。历史日志 `native-build-first.log` 与 manifest.actualNativeBuildExit=0 是本地执行证据；不得称为 GitHub CI 产物。

## 每次查验与后续编译

1. 同时读 GitHub workflow/run/artifact/release 的实际分页记录，以及对应 main 中构建/事故文档。区分本地构建、云端构建、源码备份、产物上传；当前 artifact 列表为空不能证明历史未构建。
2. 核原始库、处理后库、冻结 JNI 和最终 APK member 的完整 bytes/SHA。改源后原 SHA 不再适用；不能以新编库覆盖旧来源记录。
3. 核源码清单、Cargo.lock、NDK/ABI/features/命令和实际终态。保留原 patch、失败日志、签名材料与正式库。确需重编才沿原隔离路线；不要为了证明找到来源盲目触发云端或本地大编译。
4. 原始库与符号库分开判断：文件名 raw/unstripped 不保证保留 `.symtab`/DWARF/Build ID。先读 ELF sections/symbols；没有可用符号仍可定位精确源码，不可因此声称已有函数级 CPU 证据。
5. 本次 Root 复核入口：`RUN/c6-provenance647-root-review/ROOT_EXACT_BYTES_PUBLIC.json` 与 `ROOT_FROZEN_SOURCE_REVIEW.json`。GitHub 全分页审计入口 `RUN/c6-github-build-records647-readonly`；后续结论以该目录终态报告为准。

找到来源不等于性能修复、重新构建可逐字节复现或发布验收通过。仍按原历史77项和安装稳定后发布要求执行。

## GitHub 已核实的备份入口（2026-10-15）

VibeKits 提交 `de98fe1a348c540fc94b13e17470e2b6a444744b` 的 [native/harness/pad-source/manifest.json](https://github.com/caucy2026/vibekits/blob/de98fe1a348c540fc94b13e17470e2b6a444744b/native/harness/pad-source/manifest.json) 已保存 C6/raw SHA、构建命令、来源说明与三份最终 Rust 源码。README、manifest、累计补丁和3源码均已回读；三份源码与本地591对应文件逐SHA一致。累计补丁 SHA `b44c5bde52064eb7611260e4cd1e3198cdfca7fe6f44ba0cfbba30086eb5e55f`。

来源仓库 `caucy2026/rust-desk` 的 developmentCheckoutHead 为 `2db647ec268f3f3f18b7f40f2adb05bf0935da64`，只是来源标记；精确输入须 qualified 冻结基线加已记录变更，不可仅检出该 HEAD 即宣称同源。云端只保存这3源与累计patch，不等于全部1032文件与依赖闭包已独立可获取。

本次 GitHub API 实际分页核查 VibeKits 当前可见3 workflows、438 runs（5页；macOS246、Windows185、Harness evolution7）、当前0 artifacts、1个仅桌面包 release；native路径历史5提交。源仓库上述准确 HEAD 的 Actions runs 当前0。以上是可见历史核查结果，不是“从未有Android构建”的证明。C6的正向来源证据是本地591编译与随后GitHub源码/二进制归档。

Raw库也仅有dynsym，没有已证明的symtab/DWARF/Build ID；不要将找回raw库说成已找到完整调试符号。继续CPU定位应使用已绑定的591源码，不再用后来dirty client猜测，但不因此绕过设备采样拒绝或改官方核心。
