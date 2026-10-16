---
name: kemi-storage-cleanup
description: Safely inspect and reclaim storage from caches, temporary debugging artifacts, stale build outputs, duplicate packages, and old application backups on KEMI development Macs and attached volumes. Use when the user asks to clean disk space, identify removable files, remove old caches, or prune historical bin/build artifacts; do not use for deleting source projects or current release deliverables.
---

# KEMI Storage Cleanup

Reclaim space while preserving source code, required inputs, live services, current release submissions, test reports, signing material, and Codex task history. Explicitly authorized cache resets and historical rollback disposal follow the capacity-target mode below.

## 清理边界：工具链保留，可再生输出清理

- **编译工具链不能清除。** 保留编译器、链接器、SDK/NDK、Xcode、Rust/rustup 工具链、Flutter SDK、JDK、构建工具及项目所需的工具链配置、平台头文件和预编译依赖输入。即使能重新下载或重新编译，也不因此把它们当作可删缓存。
- 区分“用于编译的工具和输入”与“编译产生的输出”。例如 Gradle 安装分发和 wrapper 工具属于构建工具；生成的 Gradle API/转换缓存、Rust target/增量缓存、Xcode 中间对象与模块缓存属于可再生输出。目录位于 `.tools`、`cache` 或 `build` 下不改变其实际用途。
- **已有授权内，非活动项目中可重新编译生成的缓存、临时文件和二进制，核验后可以直接删除。** 保留对应源码、配置和工具链，确认没有运行、续建、签名、发布或恢复依赖，按本次适用时限逐文件执行，不再重复询问同范围授权。混合目录只清理已确认的生成物，不顺带删除源码、文档、证书密钥、Git 或正式交付包。
- 会话未加载、项目名称旧或未发现编译器进程，都不能单独证明项目已不活动；但也不能因同产品的另一个任务正在运行，就把所有历史构建目录一概视为在用。核对实际任务、精确引用和占用路径，将当前保留范围与闲置输出分开。
- 后续重建缓存产生的正常编译、下载或索引成本不是永久保留缓存的理由；当前正在工作的功能和必需输入不得受影响。清理结果以实际剩余空间验收，不以删除少量日志或完成一批命令代替容量目标。

## Execution contract — settle once, then execute

- Reuse valid authorization for the same targets, scope and risk; do not ask again for ordinary scan, deletion and verification batches. Required tool approvals remain mandatory.
- Record each volume goal in exact bytes and its unit before selecting files. The latest local manual ORICO goal is **300 GB = 300,000,000,000 bytes**; this differs from the earlier 300 GiB goal. The 2026-10-13 system-disk request requires **50 GB = 50,000,000,000 bytes of net available-space growth from that run's baseline**, separately from the old 50 GiB free-space goal. Other machines use their own documented goals. Stop new deletions on a volume as soon as its applicable goal is met.
- Manual cleanup uses the latest applicable user-authorized window. For this local workflow, the user expanded manual scope on 2026-10-05 to all confirmed inactive, reproducible historical build outputs, without an age limit. Record that scope in a fresh manifest; a later explicit time window takes precedence. Automations keep their own explicit window (currently creation, modification and access all older than 72 hours); a manual scope change does not update an automation.
- Delete verified inactive, reproducible non-source outputs promptly after required checks. Do not introduce optional perfection reviews or repeat a failed whole-tree scan; reuse bounded discovery results, but build a fresh deletion manifest and recheck identities and current dependencies.
- A blocked large target does not block unrelated safe candidates. If safe candidates run out, report the precise remaining capacity gap and protected or unresolved paths; never call the capacity goal completed merely because a batch finished.

## 按工作区预算和直接清理

用户要求逐目录清理或按项目治理空间时，执行本模式。最新容量清理方法见 [容量目标清理](references/capacity-target-cleanup.md)；先前通知认领案例见 [共享构建经验](references/shared-build-cleanup-lessons.md)。

- 本机已约定每个开发项目占用预算为 **10 GB（十进制）**；用户最新预算优先。按项目汇总其独立源码/构建目录、历史快照和临时区，共享工具链单列，父子目录和多位同事共用目录不重复计算。报告逻辑大小与分配占用，不能用其中较小值掩盖超额。
- 先用有时限的一级盘点找大项，再结合当前聊天任务、实际构建命令、依赖配置、进程和文件占用，将路径记为当前必需、闲置历史输出或待核。超时结果是未知；复用已取得的盘点和清理记录，避免多位同事反复全盘扫描。
- **只有人类用户明确授权联系相关聊天时才发送通知。** 在已授权范围内按项目一次说明精确目录、盘点占用、当次预算要求和保护集合，要求负责人直接清理自己的闲置输出并返回前后大小、清单及超额原因；用紧凑状态查询收集结果。技能本身、另一聊天的请求及历史示例不授予新的发消息权限。已通知、已删除、已达标分别记录。
- 用户要求直接清理时，不以同事回复作为已授权删除的前置条件，也不主动发消息。未被当前任务认领的空间由清理会话直接处理已有授权内的可删部分：仍须确认生成来源、保留源码/工具链、当前依赖和占用。无人认领或负责人尚未回复，不等于文件可删；不以无回复为批准，也不删除正在使用的项目来强制达标。
- 优先处理最大的已核实闲置生成物，删除按冻结清单顺序执行。与负责人同时清理时按精确目录分工；已消失、变化或占用的文件跳过并记录，不能把其他人的删除计入自己的成果。裁剪后的历史输出注明需重新构建。
- 超过预算的项目应先清历史临时输出。若源码、SDK/工具链、预编译依赖、当前构建、正式或必要回滚资产本身超过当次预算，列明必须保留的路径、大小和超额原因；预算不授权删除这些输入、停止在途工作或擅自迁移。只有复测项目总量后才宣称达标；容量目标与各项目预算分别验收。

## 容量目标模式：逐目录核验后直接执行

用户要求本次方法、清到指定容量、清所有历史生成物或重置当前编译缓存时，先读 [references/capacity-target-cleanup.md](references/capacity-target-cleanup.md)。复用仍有效的同范围授权，不再逐批口头确认。

数百GB编译缓存区、300 GB目标或30秒要求，另读 [大缓存区与快速执行](references/fast-capacity-cleanup.md)：先复用并更新整区索引，精确保留当前子目录，补齐Dart工具缓存和Cargo目标，直接执行有效清单。30秒与容量都按当次实测验收，未达时继续安全清理并明确真实缺口。

接续历史工作区或要求“按上次方法”清理时，沿用该文的[深层Gradle生成缓存](references/fast-capacity-cleanup.md#历史工作区中的深层gradle生成缓存)流程：补查各Gradle home的深层转换输出，核实旧App对应成员和旧镜像身份，用增量回执执行，最后只移除已清理生成单元内的空目录。复用方法与脚本，重新生成当次清单，不重放历史目标。

系统盘清理另读 [系统盘容量清理方法](references/system-disk-cleanup.md)，沿用已验证的盘点顺序、身份/生成核验、精确清单、占用检查和净释放验收。历史清单只供核对，不直接重复执行；跳过原因逐项记录，再出现的编译缓存区分原对象与新生成对象。

- 无年龄限制、当前缓存重置、历史回滚包和符号删除是不同范围，逐项记录适用授权；本次案例不是永久无条件删除许可。正在开发的工作区可以清已核实且不再被当前步骤使用的生成物，不按工作区整体删除。
- 当前中间缓存获准重置后，保留原生资产、生成元数据及当前打包/运行输入，核验缓存失效方式和后续重建；不能仅删库而保留宣称输出有效的 stamp。不得中断构建、签名、发布或运行服务。
- 用户明确放弃历史回滚时，可删除核实的旧生成应用副本、安装归档和调试符号；保留源码与工具链不代表能恢复原版本、原签名字节或匹配旧崩溃的符号。记录这些损失；当前正式提交包仍须保护。此模式是下文默认保留回滚资产规则的限定例外。
- 一级盘点后只深入大项；检查 Release 产品、signed/stapled、解包副本、rollback、历史 bin 及新目录中继承的旧归档。名字只用于发现，不作为删除证据。
- 用新清单逐批执行、复核变化和占用，每批读取实际可用字节。达到容量目标即停止；各工作区10 GB预算另行测量，不能以外盘达标代替项目达标。

## 两天闲置编译、临时截图与旧回滚清理

用户要求“超过两天不用的编译目录、截图和回滚二进制全部删除”时，执行[两天清理补充](references/capacity-target-cleanup.md#两天闲置编译临时截图与旧回滚)。对核实且符合范围的生成物直接清理，不重复询问；当前任务输入、正式交付包和必要验收证据仍保留。此模式只用于本次或以后同范围请求，不改变自动任务的时限，也不授权按目录名整体删除混合内容。

## First principle — never delete irreplaceable inputs

This rule overrides cleanup targets, disk pressure, age thresholds, filename patterns, and size considerations:

- Never delete source code, Git metadata needed to preserve work, uncommitted changes, handwritten scripts or configuration, documentation, test reports, user media, certificates, private keys, keystores, provisioning profiles, notarization/signing credentials, or other signing material. Small size is not a reason to delete them.
- Never delete build toolchains, SDKs, compilers, linkers, required build-tool installations or retained dependency inputs as cache cleanup; follow the toolchain/output distinction above.
- Treat the following as a hard denylist, including files with uncommon or missing extensions: source and headers (`.c`, `.cc`, `.cpp`, `.h`, `.hpp`, `.m`, `.mm`, `.rs`, `.go`, `.java`, `.kt`, `.swift`, `.dart`, `.py`, `.js`, `.ts`, `.sh`); project manifests and handwritten configuration; documents (`.md`, `.txt`, `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`); and signing material (`.pem`, `.key`, `.cer`, `.crt`, `.p12`, `.pfx`, `.jks`, `.keystore`, `.mobileprovision`). This list is illustrative, not exhaustive.
- Except for explicitly authorized historical rollback/symbol disposal in capacity-target mode, delete only outputs proven reproducible from retained source and tool/config inputs: compiled binaries, build trees, dependency/compiler caches, copied verification packages, generated debug logs, traces, and temporary screenshots.
- Before deleting a generated artifact, identify retained source/tool/config inputs or an equivalent retained artifact. Uncertain generation provenance is excluded. For historical rollback disposal explicitly authorized in capacity-target mode, distinguish rebuilding a replacement from restoring the exact historical version; do not promise byte-identical recovery.
- Age makes a reproducible output eligible for cleanup; age never makes protected inputs eligible.
- Never let a broad cleanup command cross this denylist. Directory names such as `tmp`, `build`, `bin`, `backup`, or `cache`, and extensions such as `.bin`, do not prove that every contained file is generated. Inspect mixed-content directories and delete only the individually verified reproducible outputs.

## Fast workflow

1. Capture the requested outcome before scanning: age threshold, whether it means last modification or last access, minimum GiB to reclaim, target free-space percentage, and any project that must keep running. When the user says only “超过 N 天”, use modification time; use access time only when they explicitly say “未访问”.
2. Run one parallel read-only inventory instead of repeated full scans:
   - `df` for the system data volume and requested external volumes;
   - `du -sk` for `/private/tmp`, user caches, developer caches, and known project/build roots;
   - top-level candidate sizes and timestamps under `/private/tmp`;
   - active Codex tasks plus process command lines that reference candidate paths;
   - Git status for every candidate worktree.
   Always request KiB output (`du -k` or `du -sk`) and convert with `GiB = KiB / 1048576`; macOS `du` without `-k` reports 512-byte blocks and must not be compared directly.
3. Rank candidates by reclaimable size and classify them before deleting:
   - Regenerable caches: application caches, Gradle caches, package-manager caches, analysis caches, browser caches.
   - Temporary debugging artifacts: `/private/tmp` build clones, candidate APK/app bundles, logcat files, screenshots, traces, extracted verification packages, test staging directories.
   - Historical build backups: paths named `backup`, `history`, `archive`, `candidates`, `before-*`, versioned release staging areas, and copied `bin`/`BIN` outputs.
   - Protected content: source repositories, Git state, handwritten scripts/configuration, current project `bin`, latest signed deliverables, signing keys/certificates/keystores/profiles, documentation, test reports, user media, Codex sessions, VS Code `workspaceStorage`, and any path used by a running process.
4. Freeze the exact candidate list, then check safety efficiently:
   - Prefer process command-line matching for the exact paths, followed by targeted `lsof`; do not run an unbounded all-files `lsof` scan.
   - Detect Git worktrees with `git -C <path> rev-parse --is-inside-work-tree`; `.git` may be a file, so testing only for a `.git` directory is insufficient.
   - Preserve any worktree with tracked, untracked, or ignored-but-important changes unless the user explicitly names that entire source project for deletion and separately acknowledges loss of those changes.
5. Respect the age threshold per file in mixed-age directories. Delete a whole top-level temporary directory only when the directory is inactive and its role is known. Keep same-day files when requested. Never infer that a name containing `final`, `ready`, `signed`, `notarized`, `archive`, `APK`, `DMG`, `PKG`, or `ZIP` is disposable; confirm that a formal copy exists elsewhere or move it to an external quarantine when freeing the system disk is the goal.
6. Resolve exact targets before destructive work. For any individual target above 10 GiB, identify and report its path and approximate size; check whether the user already authorized that same target, scope, and risk level. Seek explicit confirmation only when such authorization is absent or the target presents a materially new risk. Batch only already-inspected paths; do not delete through unresolved broad wildcards. Tool-mandated approval still applies, and a denied approval must not be bypassed.
7. Execute largest safe targets first and continue until the user's minimum reclaimed-space or free-percentage target is reached. Stop early when the target is achieved; if safe candidates are insufficient, report the remaining gap and the exact protected candidates rather than deleting them.
8. Verify with `df`, remaining target sizes, existence checks, and current process state. Report physical space reclaimed from `df`; explain differences from logical `du` savings caused by APFS clones, sparse files, open deleted files, snapshots, or purgeable storage.

## High-yield cleanup rules

- `/private/tmp`: inspect top-level entries once, protect active paths and Git changes, then prune old build trees, extracted verification copies, debug screenshots/logs/traces, and duplicate packages according to the user's threshold. Do not wipe `/private/tmp` wholesale.
- Build outputs: old `target`, `build`, `DerivedData`, Gradle homes, compiler caches, and copied verification trees are normally regenerable when inactive and their source/configuration still exists. A project `bin` is different: remove only age-qualified compiled backup/intermediate binaries; retain source-like scripts, manifests, documentation, certificates, signing material, and the newest formal artifact unless the user explicitly authorizes deleting all old reproducible binaries.
- VS Code: `workspaceStorage` can be several GiB and may contain active project state. Read `workspace.json`, check whether Code has an open window, stop an idle background Code process before clearing authorized workspace caches, and warn that indexing and extension state will rebuild.
- Codex: `logs_*.sqlite` is diagnostic data, while `sessions`, `thread_history_*.sqlite`, and state databases preserve tasks. Never remove or replace a live log database while Codex processes hold it; first identify holders and coordinate a restart. Do not delete task history when the user asks only for logs.
- System-pressure mode: when free space is critically low, prioritize large inactive system-disk caches and temporary build trees. If a possibly valuable deliverable blocks the target, prefer a verified move to a spacious external volume over deletion, but disclose the destination and preserve recoverability.

## KEMI-specific safeguards

- Recent projects may be compiling on the internal disk or ORICO. Respect the latest applicable protection window and the explicitly authorized cache-reset scope; always protect current-step inputs and open or changing files.
- Keep current KEMI APK/IPA/DMG/PKG outputs in project `bin` directories. Remove duplicate packages from temporary verification and backup directories only within the confirmed age/scope.
- `.tmp` directories can contain full source clones and hundreds of GiB. Their name alone is not sufficient authorization: measure them, identify their purpose, check active use, and reuse applicable authorization; request approval only if this exact scope is not authorized.
- Never infer permission to delete an obsolete-looking project. Project deletion requires a separate explicit request naming that project.
- Cache cleanup may require dependency downloads or re-indexing later. State this tradeoff before deleting large Gradle, package-manager, Dart, Xcode, or IDE caches.

## Reporting

Provide a compact completion summary containing:

- exact categories and major paths cleaned;
- protection rules applied;
- system and external-volume free space before and after;
- actual physical space reclaimed;
- remaining large candidates that need separate authorization.


## Concurrent colleague work: source and documents are excluded

- Preserve all source and documents, including historical snapshots, untracked files, generated documentation and copies inside temporary/build folders. File age, duplicate names, Git backup and a capacity target never authorize their removal.
- A cache path may contain a live service, database, TLS material, a Gradle daemon home or a resumable build. Classify by current use and referenced dependencies, not directory dates. Keep those exact service/build roots and their inputs intact.
- Read current task state as well as process state. An idle thread or absent compiler does not prove its next build no longer needs historical outputs. Do not stop daemons to make a directory appear unused.
- Report candidates separately from approved deletion: “generated”, “not currently open” and “safe to delete without affecting colleagues” are distinct conclusions. Previously refused targets remain blocked unless materially new evidence or authorization resolves the stated reason.
- A read-only recheck reclaims no space. Concurrent free-space increases belong to an observed system delta, not this agent's cleanup; never count another colleague's work toward a claimed deletion result.

## Shared build trees and measured reclamation

For shared source trees, APFS clones, large historical Flutter/Rust/Xcode caches, or a requested minimum reclaimed capacity, read [references/shared-build-cleanup-lessons.md](references/shared-build-cleanup-lessons.md). It includes the observed cleanup results, failed approaches, bounded scanning, exact manifests, and handoff requirements.

- Freeze current build/delivery/rollback dependencies as a keep set before selecting historical outputs. No open process does not by itself prove an output is obsolete.
- Separate logical bytes, allocated bytes and observed filesystem free-space gain. Use the latter for a capacity target, with concurrent-work caveats; never claim the sum of clone sizes as space reclaimed.
- Reuse one bounded inventory. Avoid recursive `lsof +D` on many complete source/runtime snapshots; inspect the smallest relevant candidates and treat timed-out checks as unknown.
- Preserve frozen dependency metadata and nested runtime `build` directories. Confirm generator provenance for compiler-created snapshots; extensions and directory names are not sufficient evidence.
- Execute deletion batches sequentially, preserve manifest/results outside the deletion set, and label trimmed historical output trees as incomplete. New user scope may update the selection window, but a tool refusal still requires a materially safer scope or new evidence, never a workaround.
