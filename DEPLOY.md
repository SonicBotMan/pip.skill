# 部署指南

> 本文件指导如何将 labor-rights-defense v5.0.0 部署到 GitHub + OpenClaw + Claude Code

---

## 📋 部署前置检查

部署前确认：

- [ ] 本地 `/home/h523034406/labor-rights-defense/` 已通过质量审查（22 个文件）
- [ ] Git 已初始化（main 分支，首次 commit 完成）
- [ ] GitHub 账号可访问（SonicBotMan）
- [ ] 本地有 `gh` CLI 或可用 HTTPS/SSH push
- [ ] 已决定仓库命名策略（见下方选项）

---

## 🚀 部署方案 A：新建独立仓库（推荐）

**适用场景**：保留原 `pip.skill` 仓库作为历史档案，新仓库作为正式版

### 步骤 1：在 GitHub 创建新仓库

```bash
# 方式 1：用 gh CLI（推荐）
gh repo create SonicBotMan/labor-rights-defense \
  --public \
  --description "🛡️ 中国劳动维权方法论 AI Agent Skill — 基于 2025 司法解释二 + 2026 最新判例" \
  --homepage ""

# 方式 2：浏览器创建
# 访问 https://github.com/new
# Repository name: labor-rights-defense
# Description: 🛡️ 中国劳动维权方法论 AI Agent Skill
# Public / 不要勾选 "Add a README file"（我们已经有）
# 不要勾选 "Choose a license"（我们已经有 CC-BY-SA-4.0）
```

### 步骤 2：关联远程仓库并推送

```bash
cd /home/h523034406/labor-rights-defense

# 关联远程
git remote add origin https://github.com/SonicBotMan/labor-rights-defense.git
# 或 SSH：
# git remote add origin git@github.com:SonicBotMan/labor-rights-defense.git

# 推送
git push -u origin main
```

### 步骤 3：在 GitHub 仓库设置

- **About**：添加 topics `labor-law`, `ai-agent-skill`, `openclaw`, `claude-code`, `chinese-law`
- **Settings → General → Features**：
  - ✅ Issues（接收案例贡献）
  - ✅ Discussions（用户讨论区）
  - ❌ Wiki（用 README 替代）
  - ✅ Projects（建立案例征集看板）
- **Settings → General → Pull Requests**：
  - ✅ Allow merge commits
  - ✅ Allow squash merging（推荐用于案例贡献）
  - ✅ Automatically delete head branches

### 步骤 4（可选）：原 `pip.skill` 仓库标记为归档

```bash
# 用 gh CLI
gh repo edit SonicBotMan/pip.skill \
  --description "⚠️ 已迁移到 https://github.com/SonicBotMan/labor-rights-defense — 本仓库为 v4.0 历史档案"

# 或浏览器访问原仓库 → Settings → 拉到底部 → Archive
# Archive 后仓库变为只读，但保留所有历史
```

或在原 `pip.skill/README.md` 顶部添加迁移通知：

```markdown
> ⚠️ **本仓库已迁移**
> 最新版本：[SonicBotMan/labor-rights-defense](https://github.com/SonicBotMan/labor-rights-defense)
> 本仓库保留为 v4.0 历史档案，不再更新。
```

---

## 🚀 部署方案 B：在原仓库改名（保留 star/fork/history）

**适用场景**：保留 `pip.skill` 已有的 4 stars / 1 fork / 9 commits 历史

### 步骤 1：在 GitHub 改名

```bash
# 用 gh CLI
gh repo rename labor-rights-defense --repo SonicBotMan/pip.skill

# 或浏览器：Settings → General → Repository name → 改为 labor-rights-defense → Rename
```

GitHub 会自动设置从 `pip.skill` → `labor-rights-defense` 的重定向，旧链接仍可用。

### 步骤 2：清空原仓库内容，替换为新版

```bash
# 克隆改名后的仓库
git clone https://github.com/SonicBotMan/labor-rights-defense.git
cd labor-rights-defense

# 删除所有旧文件
git rm -rf .
git commit -m "chore: 清空 v4.0 旧内容，准备 v5.0 重构"

# 复制新版文件
cp -r /home/h523034406/labor-rights-defense/* .
cp /home/h523034406/labor-rights-defense/.gitignore .

git add -A
git commit -m "v5.0.0: 项目重构 + 法律更新到解释二 + 案例库填充"
git push origin main
```

---

## 📦 可选：把证据库一起推送

证据库 `pip-skill-research/` 包含所有引用材料的本地副本（35 个文件 / 2.3 MB）。

**推荐：作为子目录同步到主仓库**：

```bash
cd /home/h523034406/labor-rights-defense

# 复制证据库到 research/ 子目录
mkdir -p research
cp -r /home/h523034406/pip-skill-research/* research/

# 但要排除 .gitignore 中的大文件
# 检查大小
du -sh research/

# 提交
git add research/
git commit -m "docs: 添加证据库（35 个文件，全部官方一手溯源）

- indexes/: 主索引 + 引用模板 + 补充核验记录
- sources/01-laws/: 解释二原文 + 制定背景
- sources/02-statistics/: 2024 + 2025 人社部公报
- sources/03-cases/: 16 个官方案例文件
- sources/04-specs/: AgentSkills + OpenClaw 规范"
git push origin main
```

**注意**：证据库会让仓库变大 ~2.3 MB。如果在意仓库体积，可以只推送 `indexes/` 不推送 `sources/`，让用户自行核验 URL。

---

## 🧪 在 OpenClaw 中测试

### 步骤 1：安装 OpenClaw（如未安装）

参考 https://docs.openclaw.ai/

### 步骤 2：从 GitHub 安装 Skill

```bash
# 方式 1：从 GitHub 直接安装
openclaw skills install git:SonicBotMan/labor-rights-defense@main

# 方式 2：本地安装
git clone https://github.com/SonicBotMan/labor-rights-defense.git
openclaw skills install ./labor-rights-defense --as labor-rights-defense
```

### 步骤 3：验证 Skill 已加载

```bash
openclaw skills list
# 应该能看到 labor-rights-defense
```

### 步骤 4：测试触发

在 OpenClaw 对话中输入：

```
我被公司通知 PIP 了，怎么办？
```

或：

```
我的劳动合同被公司单方面解除了，理由是绩效不达标，怎么维权？
```

应该能触发 `labor-rights-defense` skill，按 SKILL.md 的"五步框架"输出分析。

### 步骤 5：测试计算器

在 OpenClaw 对话中输入：

```
帮我计算赔偿金：在职 3 年 6 个月，月薪 25000 元，违法解除
```

Agent 应该能调用 `scripts/compensation-calculator.py --json` 输出结果。

---

## 🤖 在 Claude Code 中测试

### 步骤 1：复制到 Claude Code skills 目录

```bash
cp -r /home/h523034406/labor-rights-defense ~/.claude/skills/
```

### 步骤 2：启动 Claude Code

```bash
cd any-project
claude
```

### 步骤 3：测试触发

在 Claude Code 对话中：

```
/summarize-changes  # 测试默认 skill
# 然后输入：
我被裁员了，公司说绩效不达标，月薪 2 万，在职 3 年
```

Claude 应该能自动识别触发短语并加载本 skill。

---

## 🌐 在其他平台使用

### ChatGPT / Kimi / 通义千问 等

复制 `SKILL.md` 全文 → 粘贴到对话框 → 告诉 AI："按照这个 Skill 帮我分析我的情况" → 提供你的具体信息。

### 微信公众号 / 博客

`README.md` 可直接作为推文素材。建议拆分为系列：
1. 30 秒决策树 + 三条铁律
2. 五步框架详解
3. 2026 年最新判例解读
4. 谈判话术实战

---

## ✅ 部署后验证清单

部署完成后，逐项验证：

- [ ] GitHub 仓库可访问：https://github.com/SonicBotMan/labor-rights-defense
- [ ] README.md 在 GitHub 渲染正确（徽章、表格、决策树）
- [ ] LICENSE 被 GitHub 识别为 CC-BY-SA-4.0（仓库首页右侧边栏会显示）
- [ ] 原 `pip.skill` 链接重定向到新仓库（如选方案 B）
- [ ] `openclaw skills install git:SonicBotMan/labor-rights-defense@main` 能成功安装
- [ ] `openclaw skills list` 能看到 labor-rights-defense
- [ ] 在 OpenClaw 对话中输入触发短语能激活 skill
- [ ] `python3 scripts/compensation-calculator.py` 交互模式可用
- [ ] `echo '{...}' | python3 scripts/compensation-calculator.py --json` JSON 模式可用
- [ ] Issues 已开启，鼓励用户提交案例贡献
- [ ] Discussions 已开启，提供用户讨论区

---

## 🔄 持续维护

### 定期核验频率（来自 CHANGELOG.md）

| 项目 | 频率 | 核验方式 |
|------|------|--------|
| 司法解释是否仍现行有效 | 每年 1 月 | 访问 court.gov.cn |
| 人社部年度统计公报 | 每年 7 月 | 访问 mohrss.gov.cn |
| AgentSkills 规范更新 | 每季度 | 访问 agentskills.io |
| OpenClaw 规范更新 | 每季度 | 访问 docs.openclaw.ai |
| 法院新典型案例 | 每季度 | 关注 court.gov.cn + 各中院公众号 |

### 接收社区贡献

- 设置 Issue 模板（案例贡献 / 法条更新 / 翻译 / Bug 报告）
- 设置 PR 模板（包含自检清单，详见 `CONTRIBUTING.md`）
- 在 Discussions 建立"案例征集"分类

### 发布新版本

遵循 SemVer：

- **主版本号**（6.0.0）：法律体系重大变化（如解释三出台）
- **次版本号**（5.1.0）：新增案例、新增方法论章节
- **修订号**（5.0.1）：勘误、文案优化、引用补充

每次发布：
1. 更新 `CHANGELOG.md`
2. 更新 `SKILL.md` 的 `metadata.version`
3. Git tag：`git tag v5.1.0 && git push --tags`
4. GitHub Release：用 `gh release create v5.1.0 --notes-file CHANGELOG.md`

---

## 🆘 故障排除

### Skill 无法在 OpenClaw 中加载

检查：
1. SKILL.md 在仓库根目录（不是子目录）
2. frontmatter 有 `name` 和 `description` 字段
3. `name` 仅含 `[a-z0-9-]`
4. 运行 `openclaw skills verify labor-rights-defense` 查看错误

### 计算器运行报错

```bash
# 检查 Python 版本（需 3.8+）
python3 --version

# 检查脚本权限
chmod +x scripts/compensation-calculator.py

# 测试最小输入
echo '{"years":1,"monthly_salary":10000}' | python3 scripts/compensation-calculator.py --json
```

### GitHub 推送被拒

```bash
# 检查远程配置
git remote -v

# 检查认证
gh auth status

# 强制推送（仅限首次部署，谨慎使用）
git push -u origin main --force
```

---

## 📞 部署后支持

- **GitHub Issues**：用户问题反馈
- **GitHub Discussions**：社区讨论
- **邮件**：通过 GitHub 个人页面联系

---

**部署完成后，本项目即可服务全国 450 万+/年的劳动仲裁当事人。**
