# Oczko wyrzucone najwięcej razy z rzędu
def f(dice):
    max_digit = int(dice[0])
    max_streak = 1
    current_streak = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
                max_digit = int(dice[i])
        else:
            current_streak = 1

    return max_digit

def main():
    print(f("5233165554211"))
    print(f("2133"))

if __name__ == "__main__":
    main()