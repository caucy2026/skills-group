# Phone指南生产发布与Chrome管理会话恢复

Session-Name: vibekits 集群开发
Session-ID: 01a12aa0-1fd3-7862-8fbd-686ddc8732f2
日期：2026-10-25，Asia/Shanghai。

## 结果

公开入口：https://kemi-chat.newlinksz.com:21122/vibekits/?doc=installation 。现有安装指南新增Phone同账号协同试用接入，目录支持Phone/手机/同账号/我的设备等搜索。注册仍普通会员；Phone不需要仿真ID、customer或房间，不在手机配置目标模型Key；明确真实历史、消息、文件、断网恢复仍按最终包真机验收，不把后端接口、目录或回执completed当整体验收。

静态正式目录切为/opt/vibekits-distribution/releases/20261025-phone-guidance-v1，原room-guidance-v2保留可恢复。只改变docs/installation.md与handbook.json；29文件集合不变，原15文档ID/路径、轮播、下载/二维码及其他静态内容保持字节不变。下载目录继续按实时商城提供四平台；本轮没有发布客户端二进制，不能称商城已有Phone或796正式包。

## 资格与部署门禁

用户在本会话明确回复“恢复资格，继续原门禁”，批准索引request_user_input_async/call_f197e78152ce4f77922456dcc84b9309/0。仅本执行者台账恢复eligible，主线98cb031652d152cbd662f82504e521301c1475ce；旧错误、负控及来源revision过滤不足的更正均保留，其他执行者未恢复。本次静态部署前再次运行最新main资格检查，结果ELIGIBLE，功能门禁仍单独执行。

本地现有三项公共路由/文档清单合同在精确源码通过，重复轮次不加成独立用例。冻结旧正式目录全量SHA及新两文件；复用成熟静态激活器，只按AST改四个精确任务路径字符串，整数/权限常量不变，不使用全局版本替换。两项SFTP上传overwrite=false，逐文件SHA后单次原子切换，无新listener、数据库迁移或服务重启。

生产原PID138154、serverId da3553a32048bfe691d99ad1a27a914b保持。服务端及控制端均经正常受信HTTPS核全部28个静态资源SHA；downloads.json为动态响应，按四平台合同验证，不与旧静态快照字节混比。管理根页面仍200。

## 实际Chrome验收

用户确认原管理登录在Chrome。原页已回到登录表单，复用浏览器中指定账号已保存登录项完成同站正常认证，未取出口令、未保存新凭据。页面确认kemi一级客户管理员；QA房间只读核到Root已在房，132原成员已撤销、新邀请等待设备响应。未审批或改成员等级，不据已登录声称G08撤销矩阵完成。

浏览器扩展通道打开新页后的读取超时，先清点证实新标签已存在，再用原生Chrome选择该标签，没有重复创建。新页实际显示新版Phone指南段落、全部七步、仍在验收的说明，关闭文档成功；输入Phone后只命中对应安装指南，实际页面正文、搜索框和结果均已读取并留证。旧长期驻留标签曾显示旧内容，不能拿它冒充新页验收或判服务器发布失败；新页同时显示2026-10-25页脚及当前下载核验时间。未访问其他个人浏览器资料或绕过证书。

## 清理与容量

按cloud-build-cleanup核正式资源可取、原PID及链接保持后，冻结精确暂存集合和inode/SHA并检查/proc引用，删除本任务7个临时文件、65536分配字节。/opt可用字节152459669504→152459735040，全部暂存路径回读不存在，正式新目录及必要旧版本保留；未创建云端数据库备份。含hbbv/门户/专属journal的总分配2723942400字节，低于3000000000字节限制，不删除原数据库/WAL/配置或密钥凑指标。

证据在portal-phone-guidance-production-20261025-v1：baseline、manifest、qualification、activation-receipt、controller-public-readback、chrome-search-evidence、cleanup-result。公开页面截图只在本地按24小时保留，正式报告保留脱敏摘要与哈希索引；原始管理口令、token、私钥、聊天正文均不入Git。完整G01–G10仍未完成。
