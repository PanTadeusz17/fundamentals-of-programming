Python
def main():
    monthly_expenses = [
        [200, 50, 100],  # Week 1
        [180, 60, 110],  # Week 2
        [220, 55, 105],  # Week 3
        [210, 65, 95]    # Week 4
    ]

    food_total = 0
    transport_total = 0
    utilities_total = 0
    weekly_totals = []

    for week in monthly_expenses:
        food_total += week[0]
        transport_total += week[1]
        utilities_total += week[2]

        week_sum = 0
        for expense in week:
            week_sum += expense
        weekly_totals.append(week_sum)

    total_expenses = food_total + transport_total + utilities_total

    print("MONTHLY EXPENSES")
    print("----------------")
    print("Food:", food_total)
    print("Transport:", transport_total)
    print("Utilities:", utilities_total)
    print("Week 1:", weekly_totals[0])
    print("Week 2:", weekly_totals[1])
    print("Week 3:", weekly_totals[2])
    print("Week 4:", weekly_totals[3])
    print("---------------")
    print("TOTAL:", total_expenses)

if __name__ == "__main__":
    main()