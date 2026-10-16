# 构建、验收与商城发布

## 冻结输入

核当前main、共享脏树、锁、生成输入、平台与版本；独立冻结目录只用于本次产物，不另起持续开发源码。不可递归排除依赖内部build/dist/lib，不复用旧文件名清单漏新增源码。运行项目完整输入、实际native协议和版本门禁后再昂贵编译。

Mac版本须同时匹配pubspec、AppVersion、两份生成配置、真实构建argv与最终Info.plist。Windows必须同一完整Release组装并核CRT、EXE/DLL/AOT、原生载荷与来源。PAD组件及主APK按各自包名/签名/最低组件资格和固定事故矩阵验收。

## 测试和签名

先保留旧实现负控与首败，修后重跑受影响项及必要回归。真实UI/中文/首次输入、授权延续、会话/删除/重启持久性、模型/工具、资源/生命周期和实际设备矩阵在最终包上验收。源码、合成测试、签名/公证或目录不代替真机功能。

内层先签，外层后签；厂商字节按合同保留。任何源码/签名/最终包变化都生成新候选，复验受影响门禁，不把不同SHA的结果混用。

## 发布到正确记录

只在已有对应package_name+os_type的商城记录更新，不创建重复应用。只上传完整验收通过的最终字节；版本码递增，file_size是精确十进制字节字符串，file_size_bytes同值整数。账号、目标记录、包名、平台和授权需在发布前核实。

发布后核开发者记录、公开详情、无分类平台列表、CDN全量大小/SHA、旧版有更新/新版不重复更新，以及真实商店下载安装。上传成功不等于发布成功，页面出现也不等于包可安装。

## 网页与交付

本门户不手填“最新版本”，同站目录按访问读取官方公开记录并缓存约一分钟；商城元数据或CDN地址变更随目录刷新。页面失败时显示上次核验和稳定商城入口，不谎报新版本。正式报告记录最终包、源码commit、设备、SHA与当前未验项。

只用过云端编译时执行cloud-build-cleanup：可获取验证后，清自己不再用的云缓存/中间文件/重复旧产物，保留源码、签名材料、证据和最新正式包，回读确认。不能用清缓存冒充清零累计用量或提高预算代替可行清理。

## 完整技能与深入阅读

- [商城发布](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/kemi-market-publish/GUIDE.md)
- [完整发布错误检查](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/vibekits-release-error-preflight/GUIDE.md)
- [云构建收尾](https://github.com/caucy2026/skills-group/blob/main/vibekits-cluster-operations/references/modules/cloud-build-cleanup/GUIDE.md)
