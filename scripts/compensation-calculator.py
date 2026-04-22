#!/usr/bin/env python3
"""
劳动维权赔偿金计算器
Labor Rights Compensation Calculator

使用方法：
  python3 compensation-calculator.py

输入：在职年限、月薪、当地上年度职工月平均工资（可选，用于3倍上限判断）
输出：N、2N、代通知金、各类补偿金的计算结果

基于《劳动合同法》第47条、第87条
"""

import sys
from datetime import date

def calculate_compensation():
    print("=" * 60)
    print("劳动维权赔偿金计算器")
    print("=" * 60)
    print()

    # 基础输入
    try:
        years = float(input("在职年限（年，例如 3.5 表示3年6个月）："))
        monthly_salary = float(input("月均工资（元，输入解除前12个月平均工资，包含奖金/津贴）："))
    except ValueError:
        print("输入无效，请输入数字。")
        return

    # 当地上年度职工月平均工资（3倍上限用）
    city_avg_input = input("\n当地上年度职工月平均工资（元，输入3倍上限，不确定可跳过）：")
    city_avg = float(city_avg_input) if city_avg_input.strip() else None

    print()
    print("-" * 60)
    print("计算结果")
    print("-" * 60)

    # ========== 基本计算 ==========
    # 在职年限折算（6个月以上算1年，不满6个月算0.5年）
    full_years = int(years)
    months = (years - full_years) * 12
    if months >= 6:
        service_years = full_years + 1
    else:
        service_years = full_years + 0.5

    print(f"在职年限：{years} 年 → 折算为 {service_years} 年（N的系数）")

    # N 的计算
    base_n = service_years * monthly_salary
    print(f"\n经济补偿金 N = {service_years} × {monthly_salary} = {base_n:,.2f} 元")

    # 2N 违法解除赔偿金
    double_n = 2 * base_n
    print(f"违法解除赔偿金 2N = 2 × {base_n:,.2f} = {double_n:,.2f} 元")

    # 代通知金（1个月工资）
    print(f"\n代通知金（如适用）= {monthly_salary:,.2f} 元（公司选择不提前30天通知时需支付）")

    # ========== 3倍上限计算 ==========
    if city_avg:
        triple_city_avg = 3 * city_avg
        print(f"\n【3倍上限判断】")
        print(f"当地上年度职工月平均工资：{city_avg:,.2f} 元")
        print(f"3倍上限 = {triple_city_avg:,.2f} 元")

        if monthly_salary > triple_city_avg:
            print(f"⚠️  月薪 {monthly_salary:,.2f} 元 > 3倍上限 {triple_city_avg:,.2f} 元")
            print(f"   实际计算基数按 {triple_city_avg:,.2f} 元（3倍上限）计算")

            # 重新计算（年限不超过12年）
            capped_years = min(service_years, 12)
            base_n_capped = capped_years * triple_city_avg
            double_n_capped = 2 * base_n_capped

            print(f"\n【封顶后的结果】")
            print(f"经济补偿金 N（封顶）= {capped_years} × {triple_city_avg:,.2f} = {base_n_capped:,.2f} 元")
            print(f"违法解除赔偿金 2N（封顶）= 2 × {base_n_capped:,.2f} = {double_n_capped:,.2f} 元")
            print(f"（年限最高不超过12年，你的折算年限是 {service_years} 年）")
        else:
            print(f"✅ 月薪未超过3倍上限，按实际工资计算")

    print()
    print("-" * 60)
    print("维权参考")
    print("-" * 60)

    scenarios = [
        ("公司提出协商解除", "N + 1", "正常协商解除的最低标准，可谈判争取更高"),
        ("合法解除（员工无过错）", "N 或 N+1", "取决于是否提前通知"),
        ("违法解除（无正当理由单方解除）", "2N", "公司必须证明解除的合法性和程序合规性"),
        ("员工选择继续履行合同", "工资损失 + 2N", "也可选择不解除合同，要求继续履行"),
    ]

    print(f"\n{'场景':<28} {'最低补偿':<12} {'说明'}")
    print("-" * 60)
    for scenario, compensation, note in scenarios:
        print(f"{scenario:<28} {compensation:<12} {note}")

    print()
    print("=" * 60)
    print("⚠️  以上为理论计算结果，实际维权时请结合证据情况")
    print("⚠️  复杂案件建议咨询专业劳动法律师")
    print("=" * 60)


def quick_calc(years: float, monthly_salary: float, city_avg: float = None):
    """快速计算接口，可被其他模块调用"""
    full_years = int(years)
    months = (years - full_years) * 12
    service_years = full_years + 1 if months >= 6 else full_years + 0.5
    base_n = service_years * monthly_salary
    double_n = 2 * base_n

    result = {
        "raw_years": years,
        "service_years": service_years,
        "monthly_salary": monthly_salary,
        "N": base_n,
        "2N": double_n,
        "one_month_notice": monthly_salary,
    }

    if city_avg:
        triple_limit = 3 * city_avg
        if monthly_salary > triple_limit:
            capped_years = min(service_years, 12)
            result["N_capped"] = capped_years * triple_limit
            result["2N_capped"] = 2 * result["N_capped"]
            result["triple_limit"] = triple_limit
            result["capped"] = True

    return result


if __name__ == "__main__":
    calculate_compensation()
