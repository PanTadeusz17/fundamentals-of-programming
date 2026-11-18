def weekday(n):
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    return weekdays[n - 1]

def day_meal_plan(meal_plan, day_number):
    return ", ".join(meal_plan[day_number - 1])

def main():
    meal_plan = [
        ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
        ["Pancakes", "Sandwich", "Steak"],
        ["Smoothie", "Chicken Wrap", "Salmon"],
        ["Eggs", "Pasta", "Soup"],
        ["Toast", "Burrito", "Pizza"],
        ["Cereal", "Salad", "Fish Tacos"],
        ["Bagel", "Rice and Beans", "Stir-fry"]
    ]

    print("WEEKLY MEAL PLAN")
    print("(Breakfast, Lunch, Dinner)")
    print("==========================")
    for day in range(1, 8):
        print(f"{weekday(day)}: {day_meal_plan(meal_plan, day)}")

if __name__ == "__main__":
    main()