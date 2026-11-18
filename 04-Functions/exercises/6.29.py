#Silnia rekurencyjnie (n = 5) (Rekurencja działa jak rozkładanie problemu na mniejszy krok: factorial(5) czeka na wynik factorial(4), aż dojdzie do warunku stopu n == 1, po czym mnoży wyniki z powrotem w górę)

def factorial(n):
    # 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1
    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n - 1)

def main():
    print(factorial(5))

if __name__ == "__main__":
    main()
    