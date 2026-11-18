#n-ty wyraz ciągu Fibonacciego (1. wyraz to 0, 2. to 1)

def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

def main():
    print(f(5))
    print(f(9))

if __name__ == "__main__":
    main()