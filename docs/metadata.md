# 通用项目元数据

project.json 管理项目标识、知识路径、业务仓库清单、可选工具和验证命令。repositories 条目采用 name/path/url/branch，path 限 repositories 下；不得嵌入凭据。tools 是经管理员配置的工具入口说明，缺失表示未配置，不猜测命令或登录身份。

wiki 元数据使用 x_agent；新建文档与改名的时间语义分开。迁移时映射 x_xgj 的 UID、owner、feature_id、relations 与真实时间，未知值保留 null，不复制业务数据。来源和审核不能被模板初始化覆盖。
