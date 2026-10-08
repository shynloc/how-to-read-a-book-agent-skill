# Codex / Codex CLI

Codex 的 Skill Installer 可以从 GitHub 仓库的指定子目录安装技能，目标通常是 `$CODEX_HOME/skills`（默认 `~/.codex/skills`）；具体以当前客户端自带 Skill Installer 的说明为准。

## 方法一：通过已安装的 skill-installer
让 Codex 安装：
```text
GitHub 仓库：shynloc/how-to-read-a-book-agent-skill
源目录：skills/analytical-reading
版本：v2.1.0
```
使用 Codex 自带安装技能工作流指定仓库、`--path skills/analytical-reading` 和 `--ref v2.1.0`。不要安装整仓库根目录，也不要误装 `platforms/workbuddy/`。

## 方法二：手动
1. 从 [v2.1.0 Release](https://github.com/shynloc/how-to-read-a-book-agent-skill/releases/tag/v2.1.0) 下载通用 Agent Skills ZIP。
2. 解压得到 `analytical-reading/` 目录。
3. 将完整目录放进当前 Codex 的 Skills 目录（典型路径是 `$CODEX_HOME/skills/analytical-reading`，默认 `~/.codex/skills/analytical-reading`）。
4. 按客户端要求启动新会话/刷新技能目录，测试“请对我上传的这本书做检视阅读”。

**状态**：结构适配，尚未完成用户侧 Codex 真实模型验收。参考 [OpenAI skill-installer](https://github.com/openai/skills/blob/main/skills/.system/skill-installer/SKILL.md)。
