# agent-project-temple

单项目 Agent 协作工作区模板。结构沿用项目根规范、项目级技能、wiki 知识库、docs 方案与 repositories 业务仓库分离模式。

1. 使用 GitHub Use this template 建立自己的仓库，填写 project.json 的 project_id/name、tools 和 repositories。
2. 默认 wiki/ 为普通目录，先读 wiki/index.md。需要完整知识治理时，用 agent-wiki-temple 创建独立知识仓库：将种子目录保留在其他位置后，由管理员按所需模式挂载到 wiki/；不要对有内容的目录直接 clone。
3. 业务仓库按 repositories/<name> 独立维护；本模板不自动克隆、切换分支、安装工具或继承企业权限。需要 agent-repo 自动同步时，由管理员在 .gitmodules 中声明相应子模块，不能将 project.json 当作插件的同步配置。
4. 验证：node scripts/check.mjs 与 npm test。

参见 [元数据](docs/metadata.md)、[仓库边界](docs/repositories.md)、[技能索引](.agents/skills/README.md)、[设计来源](ORIGIN.md)。项目级 project.json 是模板配置，不替代角色仓库 projects.json，不是 agent-repo 新增 API。

配套：https://github.com/Lydanne/agent-wiki-temple ，https://github.com/Lydanne/agent-plugins 。仓库名 temple 按项目约定保留。

Git 工作模式在 project.json.git 配置，支持 read-only/local/direct/review；默认 review。完整步骤见 [Git 工作流](.agents/skills/git-workflow/references/workflow.md)，现场只读检查使用 `node scripts/git-check.mjs`。

默认脚本运行时为 Node.js 22+，无需 npm install 即可执行 npm run check、npm test 和 npm run git:check。Python 为按任务需要选择的可选语言，不是本模板依赖。
