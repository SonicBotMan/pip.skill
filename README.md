# 🛡️ Labor Rights Defense

**被通知"PIP"了？绩效明明正常却被优化？先把这个看完。**

一个开源的中国劳动维权方法论 AI Agent Skill，基于 2025 年最新司法解释和 2026 年最新判例。

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![AgentSkills Spec](https://img.shields.io/badge/AgentSkills-compatible-blue.svg)](https://agentskills.io/)
[![Legal Review](https://img.shields.io/badge/Legal%20Review-2026--07--27-green.svg)](CHANGELOG.md)
[![Version](https://img.shields.io/badge/version-5.0.0-blue.svg)](CHANGELOG.md)

---

## 📊 现实背景（你不是一个人）

> **2025 年全国劳动仲裁立案 454.3 万件**，涉及劳动者 **472.1 万人**，结案金额 **994.7 亿元**。
>
> 4 年间（2021→2025），案件数从 263.1 万件激增至 454.3 万件，**增幅 72.7%**。
> 这意味着**每年每 154 个就业者中就有 1 人通过劳动仲裁维权**。
>
> 📌 来源：人社部《2025 年度人力资源和社会保障事业发展统计公报》（2026-07-16 发布）
> 🔗 http://114.255.111.180/SYrlzyhshbzb/zwgk/szrs/tjgb/202607/t20260716_580348.html

**劳动仲裁没有你想的那么难，赔偿金也没有你想的那么少。**

---

## ⚡ 30 秒决策树（立刻知道该做什么）

```
你现在是什么状态？
│
├─ 公司刚通知我解除 / 让我签协议 / 让我自愿离职
│  └─👉 立即阅读 references/combat-guide.md「三条铁律」
│      核心动作：不要当场签字 + 拖时间 + 不主动亮证据
│
├─ 我已经签了字（解除协议 / 离职申请）
│  └─👉 读 SKILL.md「检验 C」+ references/evidence-rules.md「协议可撤销条件」
│      可能仍有翻盘机会（解释一第 35 条：低于法定 80% 可撤销）
│
├─ HR 此刻正在找我谈话
│  └─👉 立即查 negotiation/scripts-library.md 找对应话术
│      按 HR 态度（强硬/温和/拖延）选择怼回策略
│
├─ 想知道能拿多少赔偿
│  └─👉 跑 scripts/compensation-calculator.py
│      或读 methodology/compensation-tiers.md「三层赔偿金」
│
├─ 怀疑公司违法解除，但说不清哪里违法
│  └─👉 读 SKILL.md「五步框架」+ cases/official-cases-2026.md
│      对号入座到杭州 AI 替岗案 / 成都变相解除案 / 北京三中院 16369 号案
│
└─ 准备申请劳动仲裁
   └─👉 读 references/templates/arbitration-application.md
       直接套模板写仲裁申请书
```

---

## 🎯 三个最重要的原则

> **1. 不要当场签字。** 说"我需要看一下"然后离开，这不会让你少拿钱。

> **2. 不要告诉公司你有哪些证据。** 先听公司说什么，再决定亮什么牌。

> **3. 拖时间对你有利。** 仲裁时效 1 年，公司比你更想尽快解决。

---

## 🆕 v5.0.0 重大更新（2026-07-27）

### 新增 3 个劳动者维权关键武器（基于 2025-09-01 施行的解释二）

| 条文 | 武器 |
|------|------|
| **解释二第 19 条** | 公司约定"无需缴纳社保" → **约定无效**；可据此解除并主张经济补偿 |
| **解释二第 13 条** | 劳动者未知悉商业秘密 → 竞业限制条款**不生效** |
| **解释二第 18 条** | 违法解除后工资损失按**"正常劳动工资"**标准计算 |

来源：法释〔2025〕12 号，https://www.court.gov.cn/fabu/xiangqing/472691.html

### 新增 2026 年最新判例

- **杭州中院"AI 替岗"案**（2026-04 二审）：周某 vs 某网讯科技公司，2N 赔偿 **26 万余元** —— 全国首例 AI 替岗二审公开判例
- **广州中院"AI 替代"案**（2026-06 二审）：魏某 vs 某智能公司，平面设计师 AI 替代案
- **成都中院"五一"典型案例**（2026-04）：8 个完整案例，含变相解除、试用期三重刚性要件等
- **北京三中院宋某 PIP 案**（2026-01 二审，案号 `(2025)京03民终16369 号`）：违法解除赔偿 92,386.92 元，确立"不能胜任+调岗仍不胜任"**三重举证责任**

完整变更见 [CHANGELOG.md](CHANGELOG.md)。

---

## 📁 文件清单

```
labor-rights-defense/
├── SKILL.md                          # AI Skill 核心定义（AgentSkills 规范）
├── README.md                         # 本文件
├── LICENSE                           # CC-BY-SA-4.0
├── CHANGELOG.md                      # 版本变更记录
├── CONTRIBUTING.md                   # 贡献指引
│
├── methodology/                      # 方法论
│   ├── five-step-framework.md        # 五步框架详解
│   ├── compensation-tiers.md         # 三层赔偿金计算
│   ├── negotiation-cards.md          # 谈判四张牌
│   └── evidence-burden.md            # 举证责任规则
│
├── cases/                            # 案例库（全部官方一手）
│   ├── README.md                     # 案例导航 + 评级标准
│   ├── official-cases-2026.md        # 2026 年最新判例
│   ├── official-cases-2025.md        # 2025 年北京十大 + 第四批典型案例
│   └── community-cases.md            # 律所转述案例（明确标注待核）
│
├── references/                       # 参考资料
│   ├── legal-articles.md             # 法条汇编（截至解释二）
│   ├── law-migration-table.md        # 新旧法条对照表
│   ├── combat-guide.md               # 实战实操指南
│   ├── evidence-rules.md             # 举证规则参考
│   └── templates/
│       ├── arbitration-application.md # 仲裁申请书模板
│       └── complaint-letter.md        # 劳动监察投诉信模板
│
├── negotiation/
│   └── scripts-library.md            # 谈判话术库（6 大类）
│
└── scripts/
    └── compensation-calculator.py    # 赔偿金计算器
```

---

## 🚀 使用方式

### 方式 1：在 OpenClaw 中安装（推荐）

```bash
# 安装 OpenClaw（如未安装）
# 见 https://docs.openclaw.ai/

# 从 GitHub 安装本 Skill
openclaw skills install git:SonicBotMan/labor-rights-defense@main

# 或本地安装
git clone https://github.com/SonicBotMan/labor-rights-defense.git
openclaw skills install ./labor-rights-defense --as labor-rights-defense
```

安装后，在你的 AI Agent 对话中提到"被 PIP"、"解除劳动合同"、"2N 赔偿"等关键词，Skill 会自动激活。

### 方式 2：在 Claude Code 中使用

```bash
# 复制到 Claude Code 的 skills 目录
git clone https://github.com/SonicBotMan/labor-rights-defense.git
cp -r labor-rights-defense ~/.claude/skills/
```

### 方式 3：直接阅读

不需要任何 AI 平台，直接在 GitHub 上阅读：
- 先看本 README 的「30 秒决策树」
- 根据你的场景跳转到对应文件
- 重点推荐：`references/combat-guide.md`（最实战）

### 方式 4：复制内容到你常用的 AI 助手

把 `SKILL.md` 内容复制到 ChatGPT / Claude / 文心一言 / 通义千问 / Kimi 等任意 AI 助手的对话框，告诉它"按照这个 Skill 帮我分析我的情况"，然后提供你的具体信息。

---

## 📝 输入信息建议

使用此 Skill 时，按以下结构提供你的情况可获得最准确的分析：

```
【基本情况】
- 在职年限：X 年 X 个月
- 月均工资：约 X 元（含奖金/补贴/津贴）
- 合同类型：固定期限 / 无固定期限
- 是否签过竞业限制协议：是 / 否
- 年假是否休完：是 / 否 / 不清楚

【解除情况】
- 公司说的理由是什么？（原话）
- 公司是否给了书面通知？
- HR 态度：协商 / 强制 / 威胁
- 你被要求签什么文件？

【我的证据】
- 绩效记录：有 / 无
- 培训/调岗记录：有 / 无
- 工资流水：有 / 无（覆盖几个月）
- 社保记录：有 / 无
- 考勤记录：有 / 无
- 录音/照片：有 / 无

【特殊情形】
- 是否孕期/产期/哺乳期
- 是否工伤
- 是否签过"放弃社保"协议
- 是否涉及 AI 替代岗位
```

---

## ✅ 适用情况

- ✅ HR 突然叫你去谈话，说你"绩效不达标"或"公司调整"
- ✅ 收到 PIP（绩效改进计划）通知
- ✅ 公司让你签"协商解除协议"或"自愿离职申请"
- ✅ 被强制调岗、降薪、撤门禁、拔网线、移出工作群
- ✅ 合同到期公司说不续签
- ✅ 公司以"AI 替代你的岗位"为由解除
- ✅ 被要求签"放弃社保"协议
- ✅ 被威胁"背调会说坏话"
- ✅ 被主张竞业限制违约金
- ✅ 准备申请劳动仲裁

---

## 📜 法律依据版本

本 Skill 所有法律判断基于以下**现行有效**法律体系（截至 2026-07-27 核验）：

- 《中华人民共和国劳动合同法》（2013 修正本）
- 《中华人民共和国民法典》（2021-01-01 施行，**取代已废止的《合同法》《民法总则》**）
- 《中华人民共和国劳动争议调解仲裁法》
- 《最高人民法院关于审理劳动争议案件适用法律问题的解释（一）》法释〔2020〕26 号（2021-01-01 施行）
- **《最高人民法院关于审理劳动争议案件适用法律问题的解释（二）》法释〔2025〕12 号**（2025-09-01 施行）

> ⚠️ 法条会修订，使用前请到 court.gov.cn 核对最新版本。

---

## 🤝 贡献

欢迎贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

特别欢迎：
- 真实案例（必须脱敏 + 提供裁判文书号或官方案号）
- 法条更新提醒
- 地方仲裁口径差异
- 翻译（英文/广东话/方言）

---

## ⚠️ 免责声明

本 Skill 提供基于公开法律条文的通用信息整理，**不构成律师函法律意见**。

- 各地仲裁标准有差异，具体策略需要结合当地情况调整
- 复杂案件建议咨询专业劳动法律师
- 本 Skill 最后审阅日期：**2026-07-27**
- 免费法律咨询渠道：
  - 12348 法律服务热线
  - 12348 中国法律服务网 https://12348.gov.cn
  - 当地法律援助中心

---

## 📈 版本历史

- **v5.0.0**（2026-07-27）：法律体系重大升级，纳入解释二 + 2026 判例 + 项目重构
- v4.0（2026-04-24）：开源化，新增案例库（占位符）+ 话术库
- v3.0（2026-04-24）：基于 Karpathy 原则重构
- v2.3（2026-04-22）：三层赔偿金 + 谈判四张牌
- v2.0（2026-04-19）：初始版本，五步框架

完整变更见 [CHANGELOG.md](CHANGELOG.md)。

---

## 📜 License

本项目采用 [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)。

你可以自由地：
- ✅ 分享 — 复制和重新分发本材料
- ✅ 适配 — 修改、转换和基于本材料创作

但必须：
- 📌 署名 — 注明来源（SonicBotMan/labor-rights-defense）
- 🔄 相同方式共享 — 衍生作品采用相同许可协议

---

**被 PIP 了？别慌。**绩效正常却被优化，知道这些能救命。
