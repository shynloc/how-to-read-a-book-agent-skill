# OpenClaw 适配

OpenClaw 读取符合 Agent Skills 的 `SKILL.md` 及随附 `references/`。当前文档列出的一个工作区 Skill 路径是 `<workspace>/skills/analytical-reading/`；还支持 `<workspace>/.agents/skills/`、`~/.agents/skills/` 和 `~/.openclaw/skills/` 等位置，并按优先级覆盖同名 Skill。

## 推荐的明确安装方式
1. 下载 [通用 Skill ZIP v2.1.0](https://github.com/shynloc/how-to-read-a-book-agent-skill/releases/download/v2.1.0/analytical-reading-agent-skill-v2.1.0.zip)。
2. 解压到当前 OpenClaw Agent 工作区 `skills/` 下，使其成为 `<workspace>/skills/analytical-reading/SKILL.md`，同时保留 `references/` 文件。
3. 启动新会话或触发宿主的 Skill 刷新机制，测试“帮我检视阅读这篇文章”。

OpenClaw 新版本也支持安装器命令及本地目录安装；但该仓库同时含核心/WorkBuddy 两版，同一 Git 仓库安装器是否选中了正确子目录须单独验证。**优先使用已发布的通用 ZIP 手动安装**，避免同名技能冲突。

只读方法论 Skill 无需 MCP、外部 Token、shell 执行权限或知识库写权限。OpenClaw 与 Obsidian/知识库的自动同步是独立的、需要用户授权的功能，**并非本版默认行为**。

**状态**：按官方加载目录设计，运行时尚待用户环境验收。[OpenClaw 官方 Skills 文档](https://docs.openclaw.ai/tools/skills)。
