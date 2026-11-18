# Potęgowanie x^n rekurencyjnie (5^3)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def main():
    print(power(5, 3))

if __name__ == "__main__":
    main()