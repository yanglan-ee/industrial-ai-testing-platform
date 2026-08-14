# GitHub 协作说明

## 推荐分支

- 同学 1：`feat/transfer-eval`
- 同学 2：`feat/robustness-test`
- 同学 3：`feat/pipeline-report`

## 常用命令

```bash
git clone <仓库地址>
cd industrial-ai-testing-platform

git switch -c feat/transfer-eval
git add .
git commit -m "docs: initialize first-week materials"
git push -u origin feat/transfer-eval
```

之后在 GitHub 网页创建 Pull Request，合并到 `main`。

## 提交信息规范

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档修改
- `test:` 测试代码
- `refactor:` 代码重构
- `chore:` 配置或杂项
