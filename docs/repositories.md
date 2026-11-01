# 仓库边界与接入

角色仓库的 projects.json 可登记本项目，repository=projects/<projectId>、skills=[对应 .agents/skills]；省略 knowledge 即默认 wiki。project.json 的 repositories 仅描述项目配置，不会自动注册或下载。

wiki 支持普通目录、独立 Git 或已声明子模块。独立 Git 只读本地内容；未使用 gitlink 时维护适当忽略规则。agent-repo 仅同步已声明子模块；使用普通嵌套业务仓库时按真实仓库规范管理，不宣称插件会自动同步它。

每个业务仓库独立验证和交付；更新 gitlink 必须属于当前任务。模板没有 .gitmodules 私有 URL、自动克隆钩子或固定上游合并策略。
