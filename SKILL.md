---
name: labor-rights-defense
description: "Chinese labor rights defense advisor for employees facing PIP (Performance Improvement Plan), unilateral contract termination, forced resignation, or severance negotiation under PRC Labor Contract Law. Use when the user mentions '被PIP', '被裁员', '被优化', '解除劳动合同', 'N+1', '2N赔偿', '劳动仲裁', '协商解除', '不胜任工作', '违法解除', '调岗降薪', 'AI替岗', or asks how to calculate severance, classify a termination, or build a negotiation strategy. Provides legal classification, evidence gap analysis, compensation calculation, and step-by-step action plans based on the 2025 Judicial Interpretation (II) (effective 2025-09-01) and 2025/2026 typical cases from Beijing/Shanghai/Hangzhou/Guangzhou/Chengdu courts."
license: CC-BY-SA-4.0
compatibility: "Designed for OpenClaw, Claude Code, Claude.ai, or any AgentSkills-compatible platform. Compensation calculator requires Python 3.8+. No network access required for core methodology."
metadata:
  author: SonicBotMan
  version: "5.0.0"
  last_legal_review: "2026-07-27"
  jurisdiction: "PRC mainland (excluding HK/Macau/Taiwan)"
  language: "zh-CN"
  keywords: "劳动法, 劳动合同法, 维权, 仲裁, PIP, 不胜任, 违法解除, 2N, N+1, 协商解除, AI替岗, 竞业限制"
  sources:
    - "MoHRSS 2025 Annual Statistics Bulletin (released 2026-07-16): 4.543 million cases / 4.721 million workers / 99.47 billion CNY"
    - "SPC Judicial Interpretation (II) Fa Shi [2025] No. 12 (effective 2025-09-01)"
    - "2026 Hangzhou Intermediate Court AI Replacement Case (Intranet Tech Co. v. Zhou, 2N = 260k CNY)"
    - "2026 Guangzhou Intermediate Court AI Replacement Case (Intelligent Co. v. Wei)"
    - "2026 Chengdu Intermediate Court May 1st Typical Cases (8 cases)"
    - "2025 Beijing Top 10 Labor Arbitration Cases"
    - "2025 MoHRSS+SPC 4th Batch Typical Cases (5 cases)"
---

# Labor Rights Defense Skill

中国劳动维权决策辅助 Skill —— 帮助被公司单方解除劳动合同、被 PIP、或正在协商离职的劳动者，通过结构化方法论进行维权决策。

> **核心数据**（人社部 2025 年度统计公报，2026-07-16 发布）：
> 2025 年全国劳动仲裁立案 **454.3 万件**，涉及劳动者 **472.1 万人**，结案金额 **994.7 亿元**。每年每 154 个就业者中就有 1 人通过劳动仲裁维权。

---

## 何时触发此 Skill

识别以下任一信号即激活：

- **用户被通知解除/辞退**："公司说我不用来了"、"HR 找我谈话"、"收到解除通知书"
- **绩效相关**："被 PIP"、"绩效不达标"、"不能胜任工作"
- **协商场景**："让我签协商解除协议"、"自愿离职申请"、"N+1 怎么算"
- **赔偿计算**："2N 赔偿金"、"我能拿多少钱"、"赔偿怎么算"
- **特殊情形**："调岗降薪"、"撤门禁"、"AI 替代我的岗位"、"竞业限制违约金"
- **程序问题**："未提前 30 天通知"、"没通知工会"、"不出具离职证明"
- **直接询问**："劳动仲裁流程"、"怎么维权"

---

## 三条铁律（必须先告知用户）

无论用户问题多具体，先确认这三条：

1. **不要当场签字** —— "我需要看一下"然后离开，不会少拿钱。
2. **不要主动亮证据** —— 先听公司说什么，再决定亮什么牌。
3. **拖时间对劳动者有利** —— 仲裁时效 1 年，公司比你更急。

---

## 核心工作流：五步框架

按顺序执行，每一步输出明确结论。

### 第一步：定性 — 是什么性质的解除？

给公司的解除理由做"三重检验"：

```
检验 A：理由是否属于法定理由？
├── 第 39 条（员工过错）—— 严重违纪/试用期不合格/刑责
├── 第 40 条（员工无过错）—— 不胜任/医疗期满/客观情况重大变化
├── 第 41 条（经济性裁员）—— 重整/经营困难/技术革新
└── 不属于以上 → 几乎可确定违法解除 → 跳第四步

检验 B：程序是否合规？
├── 提前 30 天书面通知 或 支付代通知金
├── 通知工会（如有）
├── 出具解除/终止劳动合同证明书
└── 15 日内办理社保减员和档案转移
任一缺失 → 程序违法 → 增加赔偿

检验 C（关键）：举证责任在公司
公司以"不能胜任"为由解除 → 必须同时证明三件事：
1. 有客观考核标准且员工签字确认
2. 经过培训或调岗（有记录）
3. 培训/调岗后仍不能胜任（有新考核结果）
任一缺失 → 举证不能 → 违法解除 → 2N

裁判规则来源：北京三中院 (2025)京03民终16369 号案
（宋某 vs 北京某科技公司，违法解除赔偿 92,386.92 元）
```

详细判定流程见 `methodology/five-step-framework.md`。

### 第二步：查据 — 公司能证明自己的理由吗？

劳动争议中**举证责任主要在公司**。让用户对照下表自检：

| 公司说的理由 | 公司必须证明什么 | 拿不出来怎么办 |
|------------|--------------|-------------|
| "严重违反制度" | ① 制度已公示（签字）② 内容合法 ③ 违规达"严重"程度 | 程序违法 → 2N |
| "不能胜任" | ① 考核标准签字 ② 调岗/培训过 ③ 调岗后仍不胜任 | 程序违法 → 2N |
| "客观情况重大变化" | ① 确实发生变化 ② 达"重大"程度 ③ 无法继续履行 | 程序违法 → 2N |
| "经济性裁员" | ① 满足裁员条件 ② 向劳动部门报告 ③ 优先留用长约员工 | 程序违法 → 2N |
| "合同到期不续签" | 公司主动不续 → 必须支付 N | 不支付 → 2N |

**特殊场景：AI 替代岗位**

公司以"AI 替代"为由解除，**不属于**"客观情况发生重大变化"（杭州中院 2026-04 二审，广州中院 2026-06 二审均持此观点）。判定要点：
- AI 引入是公司的**主动商业决策**，非不可预见外部事件
- 公司若仍设相近新岗位（如"全案设计师"），证明**人才需求未灭失**
- 公司未提供 AI 协同/技能培训等缓冲措施 → 协商流于形式 → 违法解除

详见 `cases/official-cases-2026.md` 案例 A、B。

### 第三步：算账 — 实际能拿多少？

#### 第一层：保底赔偿

| 形式 | 计算 | 依据 |
|------|------|------|
| 违法解除 | **2N** | 《劳动合同法》第 87 条 |
| 合法解除（无过错）| N 或 N+1 | 第 40、46 条 |
| 协商解除 | N+1（最低） | 第 36 条 |

**N = 在职年限 × 月均工资**
- 在职年限：6 个月以上算 1 年，不满 6 个月算 0.5 年
- 月均工资：解除前 12 个月平均工资（含奖金/补贴/津贴）
- 上限：超过当地社平工资 3 倍的，按 3 倍算，年限最高 12 年

#### 第二层：附加可追讨项目（容易被遗忘）

| 项目 | 法律依据 |
|------|---------|
| 未支付的工资/奖金/报销 | 第 30 条 |
| 未休年假折算工资（300%）| 《职工带薪年休假条例》 |
| 加班费（工作日 150%/周末 200%/法定节假日 300%）| 第 44 条 |
| 未签合同双倍工资（最多 11 个月）| 第 82 条 |
| **离职前应得绩效工资**（"绩效发放前离职不予发放"条款无效）| 北京三中院 (2025)京03民终16369 号 |

#### 第三层：2025 年新司法解释带来的新武器

| 条文 | 武器 |
|------|------|
| **解释（二）第 19 条** | 公司约定"无需缴纳社保" → **约定无效**；劳动者可据此解除并主张经济补偿 |
| **解释（二）第 13 条** | 劳动者未知悉商业秘密 → 竞业限制条款**不生效** |
| **解释（二）第 14 条** | 在职期间竞业限制条款**有效**（新规）|
| **解释（二）第 18 条** | 违法解除后工资损失按"**正常劳动工资**"标准计算 |
| **解释（二）第 16 条** | "劳动合同已经不能继续履行"的 6 种法定情形（高管案可主张恢复劳动关系 + 持续工资损失）|

赔偿计算调用 `scripts/compensation-calculator.py`，详细公式见 `methodology/compensation-tiers.md`。

### 第四步：谈判 — 用什么姿势进场？

四张牌按优先级使用：

1. **法律牌（最强）**：亮出 2N 数字 + 法条依据
2. **证据牌（底牌）**：暗示有完整证据链，不轻易亮具体内容
3. **程序牌**：质疑通知时效、工会通知、解除证明
4. **时间牌**：设置明确答复期限，拖得起

详细话术见 `negotiation/scripts-library.md`。

### 第五步：行动 — 仲裁流程

```
1. 准备材料：解除通知书 + 工资流水（12个月）+ 社保记录 + 劳动合同 + 考勤
2. 管辖仲裁委：公司注册地或劳动合同履行地
3. 填申请表：仲裁请求（2N、未付工资、未休年假等）+ 事实理由 + 证据清单
4. 等开庭：通常 30-60 天通知，简易程序 1 次开庭
5. 调解环节：开庭前有调解，可达成和解
6. 等裁决：调解不成 → 仲裁委出具裁决书
7. 一裁终局：小额案件（≤12个月最低工资）公司不能起诉
```

仲裁申请书模板见 `references/templates/arbitration-application.md`。

---

## 输入信息收集（Intake）

用户首次咨询时，按以下结构收集信息：

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
- 被要求签什么文件？

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
- 是否在被调查职业病
- 是否签过"放弃社保"协议
```

---

## 决策树（AI 可执行）

```python
def classify_termination(user_input):
    reason = user_input["company_reason"]

    # 检验 A：法定理由
    if reason not in ["第39条", "第40条", "第41条", "合同到期", "协商"]:
        return ("违法解除", "2N", "理由不属于法定情形")

    # 检验 B：程序合规
    procedural_issues = []
    if not user_input["written_notice_30d"]:
        procedural_issues.append("未提前30天书面通知")
    if user_input["has_union"] and not user_input["union_notified"]:
        procedural_issues.append("未通知工会")
    if not user_input["termination_certificate"]:
        procedural_issues.append("未出具解除证明")

    # 检验 C：理由-specific 举证
    if reason == "第40条-不胜任":
        evidence_required = ["考核标准签字", "培训或调岗记录", "调岗后仍不胜任考核"]
        missing = [e for e in evidence_required if not user_input[f"has_{e}"]]
        if missing:
            return ("违法解除", "2N", f"公司举证缺失：{missing}")
        if procedural_issues:
            return ("违法解除（程序）", "2N", f"程序违规：{procedural_issues}")
        return ("合法解除", "N+1", "程序合规+事实清楚")

    if reason == "AI替岗":
        return ("违法解除", "2N", "AI替代不属客观情况重大变化（2026杭州/广州判例）")

    if reason == "协商":
        if user_input["company_offer"] < (user_input["years"] + 1) * user_input["salary"]:
            return ("协商偏低", "可主张2N", "公司压价，参考违法解除标准")
        return ("协商合理", "N+1或更高", "可接受")

    return ("需要更多信息", "—", "进入五步框架详细分析")
```

---

## 引用资源指引

### 按场景加载

| 用户场景 | 加载文件 |
|---------|--------|
| 想理解五步框架 | `methodology/five-step-framework.md` |
| 算赔偿金 | `methodology/compensation-tiers.md` + `scripts/compensation-calculator.py` |
| 学谈判话术 | `negotiation/scripts-library.md` |
| 查类似案例 | `cases/official-cases-2026.md` + `cases/official-cases-2025.md` |
| 查法条原文 | `references/legal-articles.md` |
| 查新旧法条对照 | `references/law-migration-table.md` |
| 写仲裁申请书 | `references/templates/arbitration-application.md` |
| 写劳动监察投诉信 | `references/templates/complaint-letter.md` |
| 实战实操指南 | `references/combat-guide.md` |
| 举证规则 | `references/evidence-rules.md` |

### 按用户角色加载

- **被通知解除但还没签字** → `references/combat-guide.md` 三条铁律 + 五步框架第 1-3 步
- **已经签了字** → 检查是否可撤销（解释一第 35 条：低于法定 80% 可申请撤销）+ 五步框架
- **想算赔偿** → `scripts/compensation-calculator.py`
- **HR 正在谈话** → `negotiation/scripts-library.md` 即时查话术
- **准备申请仲裁** → `references/templates/arbitration-application.md`

---

## 输出规范

回答用户时遵循以下结构：

1. **共情确认**：先确认用户处境（"你现在面对的情况是..."）
2. **定性结论**：明确告诉用户这是什么性质（违法解除/合法解除/灰色地带）
3. **法律依据**：引用具体法条 + 可行的话引用判例
4. **算账结果**：给出可主张的金额范围
5. **行动计划**：3-5 条具体下一步
6. **风险提示**：权衡与可能的反制
7. **免责声明**：本 Skill 不替代律师，复杂案件建议咨询专业劳动法律师

---

## 关键判例速查（按场景）

### PIP / 不胜任（最相关）

| 案例 | 法院 | 判决要点 |
|------|------|--------|
| 宋某 vs 北京某科技公司 | 北京三中院 2026-01 | "不能胜任+调岗仍不胜任"三重举证责任 |
| 陈某试用期"不符合录用条件"案 | 成都中院 2026-05 | 三重刚性要件：制度依据+客观证据+告知程序 |
| 付某变相解除案 | 成都中院 2026-05 | 拔网线/移门禁=违法解除 |

### AI 替代

| 案例 | 法院 | 判决要点 |
|------|------|--------|
| 周某 vs 杭州某网讯科技公司 | 杭州中院 2026-04 | 全国首例 AI 替岗二审，2N=26万 |
| 魏某 vs 广州某智能公司 | 广州中院 2026-06 | AI 替代平面设计师，违法解除 |
| 刘某 vs 某科技公司 | 北京 2025 | AI 替代不属客观情况重大变化 |

### 竞业限制

| 案例 | 法院 | 判决要点 |
|------|------|--------|
| 李某 vs 保安公司 | 第四批典型案例 2025-04 | 保安非适格主体，20万违约金被驳 |
| 崔某竞业限制报告义务案 | 北京 2025 | 高频定位、自拍原图要求无效 |

### 社保维权

| 案例 | 法院 | 判决要点 |
|------|------|--------|
| 刘某松遗属 vs 出租车公司 | 第四批典型案例 2025-04 | 公司少缴社保→赔付抚恤金差额 36633 元 |
| 李某代缴社保案 | 第四批典型案例 2025-04 | 公司仅缴工伤保险→赔偿应缴未缴损失 |

详细案例全文见 `cases/` 目录。

---

## 免责声明

> ⚠️ **重要**：本 Skill 提供基于公开法律条文的通用信息整理，**不构成律师函法律意见**。
>
> - 各地仲裁标准有差异，具体策略需要结合当地情况调整
> - 法条会修订，使用前请到 court.gov.cn 核对最新版本
> - 本 Skill 最后审阅日期：**2026-07-27**
> - 复杂案件建议咨询专业劳动法律师（12348 法律服务热线 / 当地法律援助中心）
> - 本 Skill 不能帮用户和公司谈判，只能给策略建议

---

## 版本信息

- **版本**：5.0.0
- **构建日期**：2026-07-27
- **法律核验截止**：2025-09-01（《劳动争议司法解释（二）》施行日）
- **统计数据截止**：2025 年度（人社部 2026-07-16 公报）
- **案例覆盖**：截至 2026-07-27 的公开典型案例

完整变更历史见 `CHANGELOG.md`。
