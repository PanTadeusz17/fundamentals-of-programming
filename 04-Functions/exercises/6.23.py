# Walidacja hasła (min. 6 znaków, bez powtórzeń) (Zbiór set(password) usuwa duplikaty więc jeśli jego długość równa się długości hasła żaden znak się nie powtórzył)
def f(password):
    return len(password) >= 6 and len(set(password)) == len(password)

def main():
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))

if __name__ == "__main__":
    main()
    