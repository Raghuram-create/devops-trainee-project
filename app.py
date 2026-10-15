
def calculate_profit(revenue, expenses):
    if revenue < 0 or expenses < 0:
        raise ValueError("Revenue and expenses cannot be negative")

    profit = revenue - expenses

    if profit > 0:
        decision = "Positive"
    elif profit == 0:
        decision = "Break-even"
    else:
        decision = "Loss"

    return {
        "profit": profit,
        "decision": decision
    }


if __name__ == "__main__":
    result = calculate_profit(10000, 8500)
    print(result)
