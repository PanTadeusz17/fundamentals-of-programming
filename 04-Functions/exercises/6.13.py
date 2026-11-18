#Liczby od 1 do n jako jeden ciąg znaków

def f(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result

def main():
    print(f(11))
    print(f(4))

if __name__ == "__main__":
    main()