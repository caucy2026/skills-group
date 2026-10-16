# PAD Builder 组件发布适用范围

组件不是主 APK。复用项目 `tool/check_release_error_preflight.py`；声明 `artifact_type=component`、`component_id=apk_builder`、platform=pad 后，由 `pad_builder_component_preflight.py` 校验真实 APK 包名、版本、C8证书、完整字节和资产。只有已验证的 Builder11（212549900字节，SHA256 `473a48315c38a76ab70f701fc3e5fb201cdb2226cfae75f9096325580a8ab505`）被接受；未来不同产物须重新确定适用证据，不能沿用本次 PASS。

主程序原检查器除三行组件分派外保持原字节，固定77项矩阵不变。主包不能通过回执改名进入组件分支；未知组件、错误包名/签名/产物均拒绝。

预发布八项：匹配源码与NOTICE及公开SDK资产闭包；真实包名/版本/签名合同；同签覆盖且原组件UID和开发签名/JKS连续；旧7/8完整字段与调用接口兼容、桌面隔离；真实PAD源码编译；生成APK安装及公开Receiver关联回执；失败/未知原操作对账、不盲重放；SDK选择与篡改负控。原有旧组件→最终组件覆盖证据可用，不额外发明必须直接8→11、物理607或主APK全部行为都由组件证明的前置要求。

交付另须四项：商城元数据/HTTPS/CDN完整字节；旧8正向更新与当前11无更新；真实应用中心下载→系统确认→安装回执→包版本/完整SHA→原UID/JKS和功能可用；本任务文件、认证及浏览器现场清理。发布前不能伪造这些发布后证据。用户要求的新机主APK、身份迁移、完整恢复、模型长稳及其余主程序验收仍保留，不能由组件成功替代。

检查器只证明回执文件完整性与包身份。Root须阅读真实结果及适用边界；合成测试回执不能作发布证据。发布仍沿 `kemi-market-publish`：当前官方合同、当前账号与目标归属、启用公开的组件分类、同一正式包以及真实商城安装稳定性。没有交付证据不能称正式交付完成；未知写或上传先对账，不重复提交。

本轮原始依据：项目W54及既有覆盖连续性规则。源码与证据入口为本机RUN下 `builder-component-preflight651-refined-candidate`、`builder11-ownedreceiver650-prepared`、`builder11-notices-complete`；RUN具体路径由环境文档定位，不要求同事复用个人路径。公开Main2628的正常Builder11合同/客户端/AIDL已做字节对比；其缺少后续pending确认归属竞态修复，不能外推为与Main651同等安全。
