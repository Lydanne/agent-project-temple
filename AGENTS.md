# 项目 Agent 工作约定

先读 project.json，按当前宿主实际工具和授权执行。业务任务默认先查 wiki/index.md，再定位 Feature、sources 与当前源码；知识不代替代码、配置和运行验证。docs 保存方案，不把提议写为已实现。

技能只在 .agents/skills 维护，命中时读取 SKILL.md；不安装企业 CLI 或复制个人登录态。进入 repositories/<name> 修改前读取该仓库规范，分别检查、验证、提交；不把业务代码复制到根目录。根仓忽略 repositories 只是模板默认，不提供隐私隔离。

默认按项目配置的 review 策略交付，尊重用户当前指令。不自动合并、发布、部署或发送对外消息；不把源企业的例外授权带入新项目。验证结果、执行、消息交付与生产验收分别报告。只暂存本任务文件，保留无关改动，不强推、不自动 stash。初始化模板不是生产授权。

Git 操作命中 git-workflow 技能时，先读 `.agents/skills/git-workflow/SKILL.md` 及其引用，再按本仓配置执行；配置字段只是工作约定，不替代当前授权或平台保护。

脚本优先使用 Node.js（ESM .mjs，Node.js 22+），测试优先使用 node:test。Python 可用于已有依赖或适合的专用任务，但需说明用途与依赖，不将其设为通用模板的默认运行时。
