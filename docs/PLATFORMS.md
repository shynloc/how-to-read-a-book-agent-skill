# 多平台适配与能力矩阵（v2.1.0）

**适配类型**：Native=宿主支持 Agent Skills SKILL.md；Adapter=需要专用元数据/路径；Prompt=只能复制提示词，不能称为原生 Skill。标注“待测”不是“兼容认证”。

| 平台/客户端 | 模式 | 安装资源 | 状态/限制 |
| --- | --- | --- | --- |
| WorkBuddy 技能市场 | Adapter | `platforms/workbuddy/analytical-reading/` ZIP | 结构基于 [官方 Skill 文档](https://open.workbuddy.cn/docs/skill)；解析、审核和真实运行待测 |
| Claude Code 或遵循 Agent Skills 的客户端 | Native | `skills/analytical-reading/` | 规范符合 [Agent Skills](https://agentskills.io/specification)，各宿主需实测 |
| Claude Project / Web 聊天 | Prompt | `platforms/claude/README.md` 与便携版 | 按 Project Instructions 配置；不声明支持本地读取 references |
| ChatGPT 自定义 GPT / 自定义指令 | Prompt | `platforms/chatgpt/README.md` 与便携版 | 具体配置入口和上下文大小取决于账户/产品，未保证原生 Skill 加载 |
| Codex / OpenClaw / 其他 Agent Skills 客户端 | Native（视实际版本） | 通用版 | 先验证宿主读取机制，路径不得臆测，遵循官方说明 |
| NotebookLM / 通用对话模型 | Prompt | `platforms/portable/PORTABLE-PROMPT.md` | 文件作为引用资料/自定义指令须手动适配；不能保证自动执行 |

## 通用版
安装 `skills/analytical-reading` **整目录**，至少保留其 `SKILL.md` 与 `references/`。选择宿主当前支持的 skills 目录/导入方式，勿仅把 SKILL.md 粘贴进去然后假装参考文件会自动生效。目录名需与 YAML 的 `name` 字段一致。

## WorkBuddy 专版
执行 `python scripts/build_packages.py`，得到 `dist/workbuddy-analytical-reading-v2.1.0.zip`；ZIP 顶层为一个 `analytical-reading/` 根目录。包内 SKILL.md 包含 `description_zh`、`description_en`、`version`、`author`，引用使用 `@references/...`。对照 [WorkBuddy 官网](https://open.workbuddy.cn/docs/skill) 2026-10-09 已核对字段。分类、图标、运营审核可能有额外页面级要求，实际提交时以平台 UI 为准。

## 防止语义漂移
源文件以通用 `references/` 为准；`python scripts/sync_workbuddy.py` 会覆盖 WorkBuddy 镜像的同名 references。提交前验证文件字节一致。WorkBuddy 专版 SKILL.md 保持本地化入口，所有规范性变更应同步修改通用版说明和该入口的约束。

## 发布定义
- **GitHub 已发布**：公开仓库可阅读和下载源文件。
- **静态验证通过**：目录、frontmatter、版本、引用、打包结构通过脚本。
- **平台运行通过**：在 WorkBuddy/指定 Agent 上完成真实书籍和异常输入案例。
- **WorkBuddy 市场上架**：平台自行审核通过并可在市场搜索。未经确认不标已上架。

## 个人资料与授权
分析用户提供的书籍不意味着获得对外发布授权。读书笔记、私有 PDF 或书中可能出现的密码/私密信息不得自动上传到外部，外部查阅资料前遵循宿主的用户授权和安全规则。
