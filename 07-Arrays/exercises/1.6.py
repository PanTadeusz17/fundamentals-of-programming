def weekday(n):
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]
    return weekdays[n - 1]

def main():
    for day in [1, 4, 7]:
        print(weekday(day))

if __name__ == "__main__":
    main()