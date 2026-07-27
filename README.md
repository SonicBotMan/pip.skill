# 被公司通知解除了？先别签字。

> 如果你正在看这个页面，说明你可能遇到了麻烦。
> 先深呼吸——下面这些是你现在就该做的事。

**[在线计算器 ↗](https://sonicbotman.github.io/labor-rights-defense/#calculator)** — 输入在职年限和月薪，立刻看到你能主张的赔偿金额。

---

## 你现在是什么情况？

| 你遇到的 | 该做什么 |
|---------|--------|
| HR 让我签字 | 说**「我考虑一下」**然后离开。签了 = 可能少拿几万到几十万 |
| 被通知解除 | 5 秒定性：公司说的理由是否属于法定？是否违法？ |
| 不知道能拿多少 | 用计算器算 2N / N+1 / N |
| 被 PIP（绩效改进计划）| PIP ≠ 培训。公司必须**三重举证**，否则违法解除 |
| 公司说 AI 替代了我的岗位 | 2026 年判例明确：不属"客观情况重大变化"→ 2N |
| 公司主张竞业限制违约金 | 非高管、未接触商业秘密 → 条款不生效（解释二第 13 条）|
| 被迫签了"放弃社保"协议 | **协议无效**（解释二第 19 条），可主张补缴 + 经济补偿 |

---

## 一条命令安装

```bash
openclaw skills install git:SonicBotMan/labor-rights-defense@master
```

装完后对 AI 说：「我被 PIP 了」或「2N 怎么算」或「劳动仲裁流程」。

> 不用 OpenClaw？[Claude Code 安装方式](DEPLOY.md#在-claude-code-中测试) · [直接阅读](SKILL.md) · [复制到任意 AI 助手](SKILL.md)

---

## 别人怎么赢的

| 赔偿金额 | 案例 | 法院 |
|---------|------|------|
| **26 万** | 周某 vs 杭州某科技公司（AI 替岗案，月薪 25K→15K 降薪 40%）| 杭州中院 2026-04 二审 |
| **9.2 万** | 宋某 vs 北京某科技公司（Web 工程师，不能胜任 + 三重举证）| 北京三中院 2026-01 二审 |
| **3.5 万** | 魏某 vs 广州某智能公司（平面设计师，AI 替代）| 广州中院 2026-06 二审 |

完整 23+ 个官方案例 → [`cases/`](cases/)

---

## 三条铁律

> **不要当场签字。** 说"我需要看一下"然后离开，这不会让你少拿钱。

> **不要主动亮证据。** 先听公司说什么，再决定亮什么牌。

> **拖时间对你有利。** 仲裁时效 1 年，公司比你更急。

---

## 文档导航

**不知道从哪开始？**

| 你想做什么 | 看这个文件 |
|----------|----------|
| 理解维权全流程 | [`references/combat-guide.md`](references/combat-guide.md) |
| 算赔偿金 | [`scripts/compensation-calculator.py`](scripts/compensation-calculator.py) |
| 找类似案例 | [`cases/`](cases/) — 23+ 官方一手 |
| 查法条原文 | [`references/legal-articles.md`](references/legal-articles.md) — 含解释二 21 条全文 |
| 写仲裁申请书 | [`references/templates/arbitration-application.md`](references/templates/arbitration-application.md) |
| 写劳动监察投诉信 | [`references/templates/complaint-letter.md`](references/templates/complaint-letter.md) |
| 学谈判话术 | [`negotiation/scripts-library.md`](negotiation/scripts-library.md) — 11 个场景话术 |
| 查旧法条是否还有效 | [`references/law-migration-table.md`](references/law-migration-table.md) |

---

## 数据

> **2025 年全国劳动仲裁立案 454.3 万件**，涉及劳动者 472.1 万人，结案金额 994.7 亿元。平均每件 2.25 万元。
>
> 4 年间（2021→2025），案件数增幅 72.7%。每年每 154 个就业者中就有 1 人通过劳动仲裁维权。

来源：[人社部 2025 年度统计公报](http://114.255.111.180/SYrlzyhshbzb/zwgk/szrs/tjgb/202607/t20260716_580348.html)（2026-07-16 发布）

---

## 法律依据

截至 2026-07-27 核验，全部现行有效：

- 《劳动合同法》（2013 修正）
- 《民法典》（2021-01-01 施行，取代已废止的《合同法》《民法总则》）
- **《劳动争议司法解释（二）》法释〔2025〕12 号**（2025-09-01 施行）— 21 条全文收录在 [`references/legal-articles.md`](references/legal-articles.md)

---

## 贡献

欢迎提交案例（必须脱敏 + 提供裁判文书号或官方案号）。详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

License: [CC-BY-SA-4.0](LICENSE)

---

⚠️ **本项目不构成法律意见。** 复杂案件建议咨询专业劳动法律师。

免费法律咨询：[12348 法律服务热线](https://www.12348.gov.cn) · 裁判文书检索：[wenshu.court.gov.cn](https://wenshu.court.gov.cn)
