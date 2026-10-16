# 完整构建、验收、云端和商城

## 冻结与构建

优先复用最近成功的隔离源码和完整release_driver；源码修改在最新源上形成最小patch，不对设备散发补丁、不覆盖共享dirty全文件。不重新发明签名/工具链。核源码digest、版本pubspec/Dart/generated、完整组件和assets清单后构建；未知构建先查原session/log/artifact。

当前625入口：`RUN/prepare625/release_driver.py`，source625冻结digest见current-handoff；623入口仅作历史。只有复用该精确输入时可用原approved digest；改源码须重新freeze和必要回归。签名凭据通过既有安全入口临时env读取，不打印或提交。最终产物身份为绝对路径+精确bytes+SHA256，验证内/外APK包名、certificate、最低helper/H5版本和实际运行要求。

执行`python3 tool/check_pad_embedded_helper.py <final-apk> --source <frozen-source>`及既有driver完整闭包。主程序必须默认带齐可运行所需关键文件；38 Flutter assets和按证据排除的可选桌面模型不能混为漏包。全新安装不能依赖开发机缓存/独立补丁/提前升级helper。

安装顺序固定：push到已核精确临时路径→远端sha256与本地一致→`pm install -r <path>`→PM包版本/hash/签名/UID→真正新Main进程/工具/模型调用。禁止adb install增量、-d降级、把PM成功当功能PASS。

## 发布门禁

先完整读vibekits-release-error-preflight及其本阶段引用、项目需求文档、当前固定矩阵。当前77项，不删case、不把未验挪可选、不伪造PASS。网络/生命周期/并发至少3次，原故障/负控保留；更换最终APK后受影响实机证据重取。

- R11：新系统从正式商城下载安装，真实注册、首次白名单、工具和ADB；保helper的联合卸载不能替代。
- R12：已授权旧版同签覆盖，原ID/身份/Key/名单/会话/工作区/输出连续，真实调用、冷启动重连。
- R13：ID/算法变化一次持久迁移，清旧绑定、新身份真实注册、必要授权、仿真/ADB；fixture不等于实际ID迁移。
- SIM01–05：无密码开启，pending/deny拒绝、allow允许、revoke失效、未信pubkey真实到授权门。
- 性能/上下文/存储、通用硬件、双屏、组件/Builder、UI及当前历史矩阵其余项保留；只测readonlytriplets不等于100次业务/长期模型任务。

运行项目`tool/check_release_error_preflight.py <receipt.json>` phase=prepublish绑定完整最终artifact和矩阵SHA/各内容SHA；缺项BLOCK。该程序只检完整性不代替行为。delivery阶段在真实发布后再补交付清理，不先伪造。

## 云端源码备份与合并

既有私有repo caucy2026/vibekits；使用既有GitHub安全认证和正常FF，选定owned文件秘密筛查、精确清单，create-only docs归档逐blob读回。选定源码备份不是整个构建闭包，也不是运行main merge。保护peer变更，禁止全量add/reset/stash/forcepush。提交文档不冒称线上代码已修。

运行main merge必须取最新preimage，只应用own最小hunks，复核共用平台接口/桌面行为，再build与适用真机兼容；旧preview或selected归档不能替代当前main验证。说明到底备份还是merge。

## 商城与清理

读kemi-market-publish、release-contract、signing-certification-closure及实时官方ai-publish/app-upload/store-api/Android self-update文档。用户已有发布授权可沿用，但门禁不豁免。按(package,android)更新现有记录；package-token/CDN/complete后精确bytes/SHA一致。file_size是十进制byte字符串，file_size_bytes同一整数。

回读开发者记录、公网详情和不带category平台列表；下载同一CDN完整APK核hash/size；old positive/current negative更新检查和真实客户端安装；保存无秘密报告。只上传成功不算发布。

上传后关闭本轮完成的选择器/临时页、释放自动化；不关用户和同事窗口。核现场；只删确知本任务可再生临时缓存/重复旧包，保最新签名正式包、必要回滚、源码/签名/证据。云端编译才触发cloud-build-cleanup，源码备份不冒称执行了云端编译。


## Reusable complete restoration regression runner

Current project includes `tool/pad_workspace_restore_closure_test/run.py`. Before an affected release, run this group with `--source` pointing to the exact current/frozen source, `--out` a fresh owned directory, and explicit `--jdk`, `--flutter`, `--kotlin-lib`, `--json-jar` from that machine. Read its README for the complete command. It uses current configured package roots without pub-get, compiles actual NativeVerifier, and sets the environment required by ten alias/mixed-workspace/build/spill tests. Do not copy these environment-dependent fixtures into default test discovery or replace native readback with a mock. `execution.json` binds production hashes, overlays, arguments and terminal result. The current shared-source run passed ten cases; this is not final Android installation or factory-device acceptance.


## Builder11 corresponding-source delivery checkpoint

Final component remains473a48315c38a76ab70f701fc3e5fb201cdb2226cfae75f9096325580a8ab505/version11. Source-only publication is verified at https://kemi-chat.newlinksz.com/vibekits-sources/builder11-473a48315c38a76a/source-index.json (10477B,6f4ff7de316649313b3011c89b56d260bfdd14375b0076a4be191346e72edd2f). It links the original124405760B OpenJDK source archive/c6efd7743b30c538e80c93e3be9d04cfee2d42b0404ce73ca7de7bb9d13776b8 and333291520B API interface source archive/aced8785274d8ddc18efb950cef2e7c9cb7108b11a6416528375434fabebf9b2. Independent remote hashes and full anonymous HTTPS downloads passed; source-only upload stages removed, no server config/service change. Evidence RUN/builder11-source-public-delivery/DELIVERY_RECEIPT.json plus ROOT_PUBLIC_INDEX_READBACK.json. This proves accessible matching-source supply, not original CI attestation, bit-rebuild reproducibility or complete component-release acceptance.

Before a future app79 publication, link this actual verified source index in truthful description/release notes; don't rebuild merely to append a URL. Public storefront stillversion8 and Main2607 as read2026-10-12. Main2607's contract metadata marks only7/8 source_verified;11 unknown, although its build path checks native buildReady. Don't infer full legacy-host compatibility from either the unknown label or successful625 task. Preserve actual old-host compatibility and market-install gates; no formal record mutation is recorded by source delivery.


## Stable application identity across every build and cover

Reuse the established application and helper package IDs, complete signing identity, permission declarations and credential identifiers for all versions/build directories; never mint another ID or signer for a diagnostic build. Main remains com.vibekits.vibekits with the established C8 certificate. Independent test packages retain their own established IDs/certificates and never borrow another application's grants. Before cover compare installed and final package/certificate/permissions/helper identities; afterwards verify installed base SHA, actual process and real permission/credential use. An unchanged name or enabled permission switch is insufficient. Preserve original authorization, login/license, trust, Key and workspace state. Identity mismatch must be fixed in packaging/migration, not concealed by repeated authorization or credential clearing. Device63 UID10129 is current evidence, not a universal UID assumption for colleagues.


## 原生库来源与本地/云端构建记录

原生库诊断或重编前读取[原生构建来源追溯](native-build-provenance.md)。当前 C6 已精确追到本地 legacy-registration591 冻结源码、构建命令和原始库；先沿改动记录引用核对，不再只查通用 target 或向用户索要已有路径。GitHub 构建记录与本地构建记录分别核验，不能把源码备份称为 CI 构建。


## 复用跨版本验收执行器

按发布错误台账的“跨版本脚本遗留requestId”核执行器实际契约：新模型请求ID不能沿用旧轮；探针/安装结果版本及事务文件的读写双方必须一致。覆盖前旧版本断言单独列允许清单。用原遗留输入和故障注入验证检查器会拒绝，再绑定最终APK。不得把仅AST通过当作语义验收，也不因本地回执名称换了就重发未知任务。
