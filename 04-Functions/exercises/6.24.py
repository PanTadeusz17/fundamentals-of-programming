# Obliczanie wyrażenia dodawania i odejmowania cyfr
def f(expression):
    total = int(expression[0])
    for i in range(1, len(expression), 2):
        if expression[i] == "+":
            total += int(expression[i + 1])
        elif expression[i] == "-":
            total -= int(expression[i + 1])
    return total

def main():
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))

if __name__ == "__main__":
    main()