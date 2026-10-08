# WorkBuddy 专版：安装与发布

WorkBuddy 官方支持的目录为一个 Skill 根文件夹，内部是 SKILL.md 和可选 references/scripts/templates；前置信息有中文、英文简介、作者和 SemVer 版本。详见 [官方文档](https://open.workbuddy.cn/docs/skill)。

## 下载已打包版本

**[WorkBuddy v2.1.0 ZIP](../../downloads/workbuddy-analytical-reading-v2.1.0.zip)**（从本文件所在目录返回两级到仓库根目录）；也可自行从源码构建。版本化 ZIP 中只包含安装所需的 Skill 文件，不含开发用脚本或测试。

## 构建上传包

仓库根目录执行：
```bash
python scripts/validate.py
python scripts/build_packages.py
```
输出：`dist/workbuddy-analytical-reading-v2.1.0.zip`。

检查 ZIP：
```text
analytical-reading/
  SKILL.md
  references/
    READING-METHOD.md
    EVIDENCE-PROTOCOL.md
    GENRE-RULES.md
    REPORT-TEMPLATE.md
```

通过 WorkBuddy 开放平台添加技能、提交 ZIP，先确认解析成功，再做真实触发测试，最后按市场流程提交审核。**本仓库不会也不能替代市场后台的发布操作**。

## 市场展示文案（候选）

- 展示名：AI 深度阅读｜How to Read a Book
- 简介：基于《如何阅读一本书》四层阅读法，从快速检视到系统拆书、批判性评价及跨书主题研究。严格区分原文、推断和待验证事实，帮助你形成自己的判断。
- English: A structured, evidence-first reading companion for books and long-form documents. Supports critical analysis, comparative reading, and reusable notes.
- 推荐关键词：深度阅读、拆书、读书报告、批判性思考、主题阅读、证据分析
- 维护者：Thom Jin；商店作者字段：ACKS
- 版本：2.1.0

## WorkBuddy 运行验收

至少测试：只给书名、部分 PDF、单模块、两书比较、虚构引文诱导、无法解析的 PDF、恶意嵌入指令、阅读卡片输出。记录运行模型和平台版本；**静态验证不等于商店审核或模型正确性**。
