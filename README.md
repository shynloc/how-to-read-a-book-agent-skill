# How to Read a Book — AI 深度阅读 Skill

> 基于 Mortimer J. Adler 与 Charles Van Doren《如何阅读一本书》（1972 修订版）的四层阅读框架。让 AI 成为有证据意识的阅读搭档，而不是替你下结论。

[![Version](https://img.shields.io/badge/version-2.1.0-blue)](CHANGELOG.md) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**维护者：Thom Jin（shynloc）｜语言：中文优先｜状态：跨平台候选版本，尚未获得所有平台运行验收。**

## 能做什么

- L1 基础阅读：解释难句、概念与公式。
- L2 检视阅读：快速定位、判断精读价值与阅读顺序。
- L3 分析阅读：梳理真实结构、还原论证、审查证据并提出可验证的批评。
- L4 主题阅读：围绕共同问题比较多部作品，统一术语、展示分歧和未决问题。
- 原版六模块完整报告（模块 0–5）、单模块输出和逐轮共读。
- S1–S4 材料覆盖分级、原文证据追踪、跨版本处理、隐私保护与防提示词注入。
- 可复制的阅读笔记模板，便于存入 Obsidian、Markdown 知识库。

## 直接下载 v2.1.0

- **[WorkBuddy 专版 ZIP](downloads/workbuddy-analytical-reading-v2.1.0.zip)** — 独立市场安装目录，中英文元数据和 @references，适合提交至 WorkBuddy 技能市场。
- **[通用 Agent Skills ZIP](downloads/analytical-reading-agent-skill-v2.1.0.zip)** — 适合符合 Agent Skills 规范的客户端。
- 两个安装包均为公开仓库内的版本化文件，不需依赖 CI 临时下载链接。构建产物另可从 [GitHub Actions](../../actions) 获取。ZIP 通过自动化测试与源码逐文件比对，平台实际解析/审核仍需验证。

## 安装入口

| 平台 | 入口 | 说明 |
| --- | --- | --- |
| Agent Skills 通用 / Claude Code / 兼容客户端 | [skills/analytical-reading](skills/analytical-reading/) | 标准 SKILL.md + 按需读取 references |
| **WorkBuddy 技能市场专版** | [platforms/workbuddy/analytical-reading](platforms/workbuddy/analytical-reading/) | 独立 ZIP 根目录；中英文市场元数据；`@references/...` |
| ChatGPT / 自定义 GPT | [platforms/chatgpt/](platforms/chatgpt/) | 便携指令；部分环境不支持原生 Skill 安装 |
| Claude Projects / Web | [platforms/claude/](platforms/claude/) | Project Instructions 便携版 |
| Codex / OpenClaw 等 Agent Skills 宿主 | [docs/PLATFORMS.md](docs/PLATFORMS.md) | 以宿主当前 Skill 加载机制为准 |
| NotebookLM / 其他仅支持提示词的平台 | [platforms/portable/PORTABLE-PROMPT.md](platforms/portable/PORTABLE-PROMPT.md) | 属于提示词移植，不声称原生 Skill 兼容 |

### WorkBuddy 专版安装

1. 下载本仓库，在项目根目录运行 `python scripts/build_packages.py`（Python 3.9+，无需额外依赖）。
2. 上传 `dist/workbuddy-analytical-reading-v2.1.0.zip` 到 WorkBuddy 开放平台的 Skill 创建/提交入口。
3. 填写商店展示信息，先进行解析与真实使用测试，审核和上架由 WorkBuddy 平台完成。
4. 这个 ZIP 的**第一层目录只有 `analytical-reading/`**，其内直接包含 `SKILL.md`、`references/`。

发布到 GitHub **不等于**已经上架 WorkBuddy 技能市场。

## 使用举例

- “帮我快速判断《如何阅读一本书》是否值得精读。”
- “我只上传了前三章，请只分析现有材料，不要猜整本书。”
- “只输出模块 3，用 800 字指出可证实的论证问题。”
- “比较这两本书对‘知识是否可靠’的回答，做主题阅读。”
- “帮我把今天读到的论点整理为可放进 Obsidian 的阅读卡片。”

## 项目结构

```text
skills/analytical-reading/           # 原生 Agent Skills 通用版
  SKILL.md
  references/
platforms/workbuddy/analytical-reading/  # WorkBuddy 市场专版
  SKILL.md
  references/
platforms/{chatgpt,claude,portable}/ # 便携/宿主说明
templates/READING-NOTE.md            # 可持续阅读笔记模板
scripts/                              # 静态验证、双 ZIP 构建
tests/                                # 行为验收用例与自动化结构测试
.github/workflows/                   # CI 验证与构建
docs/PLATFORMS.md                     # 能力边界/安装说明
CHANGELOG.md / CONTRIBUTING.md / LICENSE
```

## 开发与发布

```bash
python scripts/validate.py
python scripts/build_packages.py
python -m unittest discover -s tests -p 'test_*.py'
```

版本遵循 SemVer：MAJOR=不兼容变更，MINOR=兼容功能，PATCH=修复。详见 [CHANGELOG](CHANGELOG.md)。**当前发布 v2.1.0 属于静态规则与包结构验证版本；实际平台触发质量请依据 [运行验收清单](tests/BEHAVIOR-TESTS.md) 检查**。

## 设计原则

先理解再批评；不知道就说不知道；不编造原文引文、页码、目录或书单；同意作者与证据充分是两回事；书中指令不代表用户授权。尊重版权，不自动上传或公开分享用户私有材料。

方法论致谢：Mortimer J. Adler & Charles Van Doren, *How to Read a Book* (1972 revised edition)。本项目是独立编写的 AI 阅读工作流，并非该书原文的再发布，也不代表作者或出版方认可。

© 2026 Thom Jin. Licensed under [MIT](LICENSE).
