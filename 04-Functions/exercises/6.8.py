# Automat z monetami (1, 2, 5 PLN)
def f(amount_to_pay):
    coins = amount_to_pay // 5
    amount_to_pay %= 5
    coins += amount_to_pay // 2
    amount_to_pay %= 2
    coins += amount_to_pay
    return coins

def main():
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))

if __name__ == "__main__":
    main()