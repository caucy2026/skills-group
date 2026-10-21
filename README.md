# VibeKits 团队技能与操作文档

[下载与使用门户](https://kemi-chat.newlinksz.com:21122/vibekits/) · [分类文档](docs/README.md)

## 从任务进入

- 维护四端下载网站、商城版本同步和云端共用端口部署：[vibekits-distribution/SKILL.md](vibekits-distribution/SKILL.md)。

- 完整接手房间与集群：[vibekits-cluster-operations/SKILL.md](vibekits-cluster-operations/SKILL.md)。
- 按设备ID仿真与PAD远程ADB：[vibekits-remote-simulator/SKILL.md](vibekits-remote-simulator/SKILL.md)。
- 使用房间现有Windows/Mac签名资源：[vibekits-room-signing/SKILL.md](vibekits-room-signing/SKILL.md)。

## 操作手册

- [安装与首次接入](docs/installation.md)、[自更新与回滚](docs/self-update.md)。
- [仿真完整流程](docs/simulation.md)、[PAD远程ADB与双屏](docs/pad-adb.md)。
- [房间、管理员、任务与能力](docs/rooms.md)。
- [Windows令牌签名](docs/windows-signing.md)、[Mac签名与公证](docs/mac-signing.md)、[构建与商城发布](docs/build-release.md)。
- [调试方法](docs/debugging.md)、[异常恢复](docs/recovery.md)、[监控与清理](docs/maintenance.md)。

## 安装完整技能

将需要的整个技能目录安装到自己的Codex技能目录，默认 ~/.codex/skills/，CODEX_HOME存在时按自己的配置。保留references、scripts、modules，不只下载SKILL.md。已有同名目录先比较合并，保护本地定制。

统一集群包的专项资料位于references/modules，每个模块保留GUIDE.md、详细参考与脚本，按需读取，避免重复注册同名技能。使用自己的获授权账号和设备清单；凭据、密码、Key、PIN和私钥不在仓库。

原始仿真云端目录：https://github.com/caucy2026/skills/tree/main/vibekits-remote-simulator 。本仓库是团队同步副本。历史机器、路径和版本不是新的默认配置；以当前房间目录、原身份、项目规则和真实工具为准。

## 按需求找资源

- [在本机写代码，借房间Windows编译](docs/windows-build.md)。
- [需要Linux ARM64仿真设备](docs/linux-arm64.md)。
- [从找设备到交付任务](docs/collaboration-tasks.md)。

## Cloud service release

- [hbbv server build and deployment](hbbv-server-build-deploy/SKILL.md).
- [Mandatory cloud build and post-deployment cleanup](cloud-build-cleanup/SKILL.md).
