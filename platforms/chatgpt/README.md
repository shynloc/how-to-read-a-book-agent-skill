# ChatGPT 适配说明

有两种不同用法：
1. **GPT 配置/项目指令**：把 `../portable/PORTABLE-PROMPT.md` 的全文作为行为指令，另将需要的书籍或文档提供给当前会话。是否允许上传知识文件、可用长度等取决于当前产品配置。
2. **普通对话**：直接粘贴便携 Prompt，然后给出材料和任务，例如“只完成模块 3”。

该方式是**提示词移植**，不保证 ChatGPT 普通对话自动加载仓库中的 references，也不等同于原生 Agent Skills 安装。大文档必须由当前可用的文件工具逐段访问；仅给书名不能承诺全文分析。无权操作用户外部知识库或发布其笔记。

便携版：[PORTABLE-PROMPT.md](../portable/PORTABLE-PROMPT.md)。
