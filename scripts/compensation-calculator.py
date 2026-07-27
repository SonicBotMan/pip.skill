#!/usr/bin/env python3
"""
Labor Rights Compensation Calculator
劳动维权赔偿金计算器

Usage:
  Interactive mode:
    python3 compensation-calculator.py

  JSON stdin mode (for AI Agent calls):
    echo '{"years":3.5,"monthly_salary":25000}' | python3 compensation-calculator.py --json

  JSON with all options:
    echo '{
      "years": 3.5,
      "monthly_salary": 25000,
      "city_avg_salary": 12000,
      "unused_annual_leave": 8,
      "notice_days_given": 0,
      "termination_type": "illegal"
    }' | python3 compensation-calculator.py --json

Based on:
- 《劳动合同法》第 47 条 (N 计算)
- 《劳动合同法》第 87 条 (2N 违法解除)
- 《劳动合同法》第 40 条 (代通知金)
- 《职工带薪年休假条例》第 5 条 (年假 300%)
- 解释（二）第 18 条 (工资损失按正常劳动工资)

Legal review: 2026-07-27
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from typing import Literal, Optional


MONTHLY_WORK_DAYS = 21.75  # 月计薪天数
WORK_HOURS_PER_DAY = 8


TerminationType = Literal["illegal", "legal_n", "legal_n_plus_1", "negotiated", "resume"]


@dataclass
class CompensationInput:
    """赔偿金计算输入参数"""

    years: float  # 在职年限（如 3.5 = 3 年 6 个月）
    monthly_salary: float  # 月均工资（含奖金/补贴/津贴）
    city_avg_salary: Optional[float] = None  # 当地上年度职工月平均工资（用于 3 倍上限判断）
    unused_annual_leave: int = 0  # 未休年假天数
    notice_days_given: int = 30  # 公司提前通知的天数（不足 30 需付代通知金）
    termination_type: TerminationType = "illegal"  # 解除类型
    unpaid_wages: float = 0  # 未支付的工资/奖金
    unpaid_overtime_hours: float = 0  # 未付加班小时数
    overtime_rate: float = 1.5  # 加班费倍率（1.5/2.0/3.0）
    waiting_months_for_resume: int = 0  # 选择恢复劳动关系时的等待月数（解释二第 18 条）


@dataclass
class CompensationResult:
    """赔偿金计算结果"""

    # 基础信息
    raw_years: float
    service_years: float  # 折算后的年限系数
    monthly_salary: float
    actual_salary_base: float  # 实际计算基数（3 倍封顶后）
    capped: bool  # 是否触发 3 倍上限

    # 第一层：保底赔偿
    N: float  # 经济补偿金
    double_N: float  # 2N 违法解除赔偿金
    one_month_notice: float  # 代通知金

    # 第二层：附加项目
    annual_leave_compensation: float  # 未休年假折算（额外补 200%）
    unpaid_wages_total: float  # 未付工资
    unpaid_overtime_total: float  # 未付加班费

    # 第三层：恢复劳动关系的工资损失（解释二第 18 条）
    wage_loss_if_resume: float  # 工资损失（按正常劳动工资）

    # 推荐方案
    recommended_claim: float  # 推荐主张总额
    recommended_strategy: str  # 推荐策略说明


def calculate_service_years(years: float) -> float:
    """
    在职年限折算。
    规则：6 个月以上算 1 年，不满 6 个月算 0.5 年。
    """
    if years < 0:
        raise ValueError(f"在职年限不能为负数：{years}")
    full_years = int(years)
    remaining_months = (years - full_years) * 12
    # 处理浮点精度
    remaining_months = round(remaining_months, 1)
    if remaining_months >= 6:
        return float(full_years + 1)
    elif remaining_months > 0:
        return float(full_years + 0.5)
    else:
        return float(full_years)


def calculate_salary_base(monthly_salary: float, city_avg_salary: Optional[float]) -> tuple[float, float, bool]:
    """
    计算赔偿金基数。
    如果月薪 > 当地社平工资 3 倍，按 3 倍计算。
    返回：(实际基数, 3 倍上限值, 是否触发上限)
    """
    if monthly_salary < 0:
        raise ValueError(f"月薪不能为负数：{monthly_salary}")

    if city_avg_salary is None or city_avg_salary <= 0:
        return monthly_salary, 0.0, False

    triple_limit = 3 * city_avg_salary
    if monthly_salary > triple_limit:
        return triple_limit, triple_limit, True
    return monthly_salary, triple_limit, False


def calculate_n(service_years: float, salary_base: float, capped: bool) -> float:
    """
    计算经济补偿金 N。
    规则：N = 在职年限 × 月均工资。
    如果触发 3 倍上限，年限最高 12 年。
    """
    actual_years = min(service_years, 12) if capped else service_years
    return actual_years * salary_base


def calculate_annual_leave(monthly_salary: float, unused_days: int) -> float:
    """
    未休年假折算工资。
    规则：日工资 × 未休天数 × 300%。
    公司已发正常工资，实际可主张额外补 200%。
    """
    if unused_days <= 0:
        return 0.0
    daily_wage = monthly_salary / MONTHLY_WORK_DAYS
    # 额外补 200%（300% 中已支付的 100% 要扣除）
    return daily_wage * unused_days * 2.0


def calculate_overtime(monthly_salary: float, hours: float, rate: float) -> float:
    """
    加班费计算。
    rate: 1.5 (工作日) / 2.0 (周末) / 3.0 (法定节假日)
    """
    if hours <= 0:
        return 0.0
    hourly_wage = monthly_salary / MONTHLY_WORK_DAYS / WORK_HOURS_PER_DAY
    return hourly_wage * hours * rate


def calculate_notice_compensation(monthly_salary: float, notice_days_given: int) -> float:
    """
    代通知金：公司未提前 30 天通知需额外付 1 个月工资。
    """
    if notice_days_given >= 30:
        return 0.0
    return monthly_salary


def calculate_wage_loss_if_resume(monthly_salary: float, waiting_months: int) -> float:
    """
    解释（二）第 18 条：违法解除后选择恢复劳动关系，等待期工资损失。
    按"正常劳动工资"标准计算。
    """
    if waiting_months <= 0:
        return 0.0
    return monthly_salary * waiting_months


def calculate_compensation(inp: CompensationInput) -> CompensationResult:
    """主计算函数"""
    # 1. 年限折算
    service_years = calculate_service_years(inp.years)

    # 2. 工资基数（3 倍上限判断）
    salary_base, triple_limit, capped = calculate_salary_base(
        inp.monthly_salary, inp.city_avg_salary
    )

    # 3. 第一层：保底赔偿
    N = calculate_n(service_years, salary_base, capped)
    double_N = 2 * N
    notice_pay = calculate_notice_compensation(inp.monthly_salary, inp.notice_days_given)

    # 4. 第二层：附加项目
    annual_leave = calculate_annual_leave(inp.monthly_salary, inp.unused_annual_leave)
    overtime = calculate_overtime(inp.monthly_salary, inp.unpaid_overtime_hours, inp.overtime_rate)

    # 5. 第三层：恢复劳动关系的工资损失
    wage_loss = calculate_wage_loss_if_resume(inp.monthly_salary, inp.waiting_months_for_resume)

    # 6. 推荐策略
    recommended_claim, strategy = _recommend_strategy(
        inp.termination_type, N, double_N, notice_pay,
        annual_leave, overtime, inp.unpaid_wages, wage_loss
    )

    return CompensationResult(
        raw_years=inp.years,
        service_years=service_years,
        monthly_salary=inp.monthly_salary,
        actual_salary_base=salary_base,
        capped=capped,
        N=N,
        double_N=double_N,
        one_month_notice=notice_pay,
        annual_leave_compensation=annual_leave,
        unpaid_wages_total=inp.unpaid_wages,
        unpaid_overtime_total=overtime,
        wage_loss_if_resume=wage_loss,
        recommended_claim=recommended_claim,
        recommended_strategy=strategy,
    )


def _recommend_strategy(
    termination_type: TerminationType,
    N: float,
    double_N: float,
    notice_pay: float,
    annual_leave: float,
    overtime: float,
    unpaid_wages: float,
    wage_loss: float,
) -> tuple[float, str]:
    """根据解除类型推荐主张策略"""
    base_addons = annual_leave + overtime + unpaid_wages

    if termination_type == "illegal":
        total = double_N + notice_pay + base_addons
        strategy = (
            f"违法解除：主张 2N={double_N:,.2f}"
            + (f" + 代通知金={notice_pay:,.2f}" if notice_pay > 0 else "")
            + (f" + 附加项={base_addons:,.2f}" if base_addons > 0 else "")
            + f" = {total:,.2f}"
        )
    elif termination_type == "legal_n":
        total = N + base_addons
        strategy = f"合法解除（N）：主张 N={N:,.2f} + 附加项={base_addons:,.2f} = {total:,.2f}"
    elif termination_type == "legal_n_plus_1":
        total = N + notice_pay + base_addons
        strategy = (
            f"合法解除（N+1）：主张 N={N:,.2f} + 代通知金={notice_pay:,.2f}"
            + f" + 附加项={base_addons:,.2f}"
            + f" = {total:,.2f}"
        )
    elif termination_type == "negotiated":
        total = N + notice_pay + base_addons
        strategy = (
            f"协商解除：最低标准 N+1={N + notice_pay:,.2f}，"
            f"可争取 2N={double_N:,.2f}（如能证明违法解除）"
        )
    elif termination_type == "resume":
        total = wage_loss + base_addons
        strategy = (
            f"恢复劳动关系（解释二第 18 条）：工资损失={wage_loss:,.2f} "
            f"+ 附加项={base_addons:,.2f} = {total:,.2f}"
        )
    else:
        total = double_N
        strategy = f"默认主张 2N={double_N:,.2f}"

    return total, strategy


def format_result(r: CompensationResult, inp: CompensationInput) -> str:
    """格式化为人类可读输出"""
    lines = [
        "=" * 60,
        "劳动维权赔偿金计算结果",
        "=" * 60,
        "",
        "【基础信息】",
        f"  在职年限：{r.raw_years} 年 → 折算 {r.service_years} 年（N 的系数）",
        f"  月均工资：{r.monthly_salary:,.2f} 元",
    ]

    if r.capped:
        lines.append(f"  ⚠️  触发 3 倍上限：实际计算基数 = {r.actual_salary_base:,.2f} 元")
        lines.append(f"     年限最高不超过 12 年")
    elif inp.city_avg_salary:
        lines.append(f"  ✅ 未触发 3 倍上限（当地社平 3 倍 = {3 * inp.city_avg_salary:,.2f} 元）")

    lines.extend([
        "",
        "【第一层：保底赔偿】",
        f"  经济补偿金 N      = {r.N:>12,.2f} 元",
        f"  违法解除赔偿金 2N = {r.double_N:>12,.2f} 元",
        f"  代通知金（如适用）= {r.one_month_notice:>12,.2f} 元",
        "",
        "【第二层：附加可追讨项目】",
        f"  未休年假折算（200%）= {r.annual_leave_compensation:>12,.2f} 元",
        f"  未付工资            = {r.unpaid_wages_total:>12,.2f} 元",
        f"  未付加班费          = {r.unpaid_overtime_total:>12,.2f} 元",
    ])

    if r.wage_loss_if_resume > 0:
        lines.extend([
            "",
            "【第三层：解释（二）第 18 条 工资损失】",
            f"  恢复劳动关系等待期工资损失 = {r.wage_loss_if_resume:>12,.2f} 元",
            f"  （按'正常劳动工资'标准计算）",
        ])

    lines.extend([
        "",
        "-" * 60,
        "推荐主张",
        "-" * 60,
        f"  {r.recommended_strategy}",
        f"  推荐主张总额：{r.recommended_claim:,.2f} 元",
        "",
        "=" * 60,
        "⚠️  以上为理论计算结果，实际维权时请结合证据情况",
        "⚠️  复杂案件建议咨询专业劳动法律师（12348 法律服务热线）",
        "=" * 60,
    ])

    return "\n".join(lines)


def interactive_mode() -> None:
    """交互式输入模式"""
    print("=" * 60)
    print("劳动维权赔偿金计算器")
    print("=" * 60)
    print()

    try:
        years = float(input("在职年限（年，如 3.5 表示 3 年 6 个月）："))
        monthly_salary = float(input("月均工资（元，含奖金/津贴）："))
    except ValueError:
        print("❌ 输入无效，请输入数字。")
        sys.exit(1)

    city_avg_input = input("\n当地上年度职工月平均工资（元，回车跳过）：").strip()
    city_avg = float(city_avg_input) if city_avg_input else None

    leave_input = input("未休年假天数（默认 0）：").strip()
    unused_leave = int(leave_input) if leave_input else 0

    notice_input = input("公司提前通知天数（默认 30，不足 30 需付代通知金）：").strip()
    notice_days = int(notice_input) if notice_input else 30

    print("\n解除类型：")
    print("  1. 违法解除（默认，主张 2N）")
    print("  2. 合法解除-无过错（主张 N）")
    print("  3. 合法解除-N+1（主张 N+1）")
    print("  4. 协商解除（主张 N+1 起，可争取 2N）")
    print("  5. 恢复劳动关系（主张工资损失，解释二第 18 条）")
    type_input = input("选择（1-5，默认 1）：").strip()
    type_map = {
        "1": "illegal", "2": "legal_n", "3": "legal_n_plus_1",
        "4": "negotiated", "5": "resume"
    }
    term_type = type_map.get(type_input, "illegal")

    waiting_input = input("如果选 5，等待月数（默认 0）：").strip()
    waiting_months = int(waiting_input) if waiting_input else 0

    inp = CompensationInput(
        years=years,
        monthly_salary=monthly_salary,
        city_avg_salary=city_avg,
        unused_annual_leave=unused_leave,
        notice_days_given=notice_days,
        termination_type=term_type,
        waiting_months_for_resume=waiting_months,
    )

    result = calculate_compensation(inp)
    print()
    print(format_result(result, inp))


def json_mode() -> None:
    """JSON stdin 模式（供 AI Agent 调用）"""
    raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"error": "no input provided via stdin"}, ensure_ascii=False))
        sys.exit(1)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"invalid JSON: {e}"}, ensure_ascii=False))
        sys.exit(1)

    # 兼容默认值
    inp = CompensationInput(
        years=float(data.get("years", 0)),
        monthly_salary=float(data.get("monthly_salary", 0)),
        city_avg_salary=data.get("city_avg_salary"),
        unused_annual_leave=int(data.get("unused_annual_leave", 0)),
        notice_days_given=int(data.get("notice_days_given", 30)),
        termination_type=data.get("termination_type", "illegal"),
        unpaid_wages=float(data.get("unpaid_wages", 0)),
        unpaid_overtime_hours=float(data.get("unpaid_overtime_hours", 0)),
        overtime_rate=float(data.get("overtime_rate", 1.5)),
        waiting_months_for_resume=int(data.get("waiting_months_for_resume", 0)),
    )

    result = calculate_compensation(inp)
    output = {
        "input": asdict(inp),
        "result": asdict(result),
        "legal_basis": {
            "N": "《劳动合同法》第 47 条",
            "2N": "《劳动合同法》第 87 条",
            "notice": "《劳动合同法》第 40 条",
            "annual_leave": "《职工带薪年休假条例》第 5 条（300%）",
            "wage_loss": "解释（二）第 18 条（按正常劳动工资）",
        },
        "legal_review_date": "2026-07-27",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="劳动维权赔偿金计算器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON stdin 模式（供 AI Agent 调用）",
    )
    args = parser.parse_args()

    if args.json:
        json_mode()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
