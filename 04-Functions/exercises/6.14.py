# Prosty kalkulator z operatorem tekstowym
def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2

def main():
    print(f(2, 3, "+"))
    print(f(2, 3, "%"))
    print(f(2, 3, "**"))
    print(f(2, 3, "*"))
    print(f(2, 3, "-"))

if __name__ == "__main__":
    main()