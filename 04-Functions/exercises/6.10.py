#Liczba ujemnych liczb parzystych w przedziale <x, y>

def f(x, y):
    count = 0
    for n in range(x, y + 1):
        if n < 0 and n % 2 == 0:
            count += 1
    return count

def main():
    print(f(-7, 8))
    print(f(-1, 11))

if __name__ == "__main__":
    main()