# n-ta liczba pierwsza
def f(n):
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        is_prime = True
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return candidate

def main():
    print(f(1))
    print(f(5))

if __name__ == "__main__":
    main()