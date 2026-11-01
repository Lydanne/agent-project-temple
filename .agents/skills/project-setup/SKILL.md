---
name: project-setup
description: 初始化或检查通用项目元数据及知识、业务仓库边界。
---

读取 project.json、docs/metadata.md 和 docs/repositories.md。先检查实际 Git 状态与路径，对需要初始化的仓库列明 URL、分支和目标；仅在当前任务授权初始化时执行。已有目录核对真实 remote/branch，保留脏文件与未推送提交；不自动切分支或覆盖目录。工具缺失仅报告缺失，不安装企业专属工具。执行项目 verification.commands 的已审阅命令；初始化结束报告哪些已完成、哪些未配置，不将模板创建视为生产就绪。
