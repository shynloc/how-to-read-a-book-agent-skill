# Contributing / 参与贡献

欢迎报告阅读方法、引文溯源、文本覆盖、WorkBuddy 安装或其他平台适配中的缺陷。

1. 创建 Issue，描述目标平台、Skill 版本、重现步骤以及预期/实际输出，**请先脱敏**。不要上传完整受版权保护的书或未授权的私人笔记。
2. 核心分析规则以 `skills/analytical-reading/` 为源。WorkBuddy 镜像的 `references/` 文件须与核心一致；用 `scripts/sync_workbuddy.py` 显式同步，再检查 diff。
3. 增加平台适配时说明其属于原生 Skill、通过宿主自定义指令导入，还是只支持便携 Prompt，避免虚假“开箱兼容”声明。
4. 运行 `python scripts/validate.py`、`python -m unittest discover -s tests -p 'test_*.py'`、`python scripts/build_packages.py`。
5. 参考 [行为验收](tests/BEHAVIOR-TESTS.md) 在目标平台记录通过/部分/失败及输出样本；静态测试通过不代表真实阅读效果通过。

版本：PATCH 用于修正、MINOR 用于兼容性新增功能、MAJOR 用于破坏性协议更改。修改版本时同步通用元数据、WorkBuddy frontmatter、脚本常量、README、CHANGELOG。

提交不等于上架：WorkBuddy 技能市场还需要解析、审核及平台实际验证。
