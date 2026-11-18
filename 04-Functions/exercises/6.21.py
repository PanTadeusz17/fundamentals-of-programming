# Różnica między największą a najmniejszą z trzech liczb
def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)

def main():
    print(f(7, 4, 9))
    print(f(2, 12, 8))

if __name__ == "__main__":
    main()