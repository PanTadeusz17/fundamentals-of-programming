# Sprawdzanie palindromu
def f(palindrome):
    return palindrome == palindrome[::-1]

def main():
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))

if __name__ == "__main__":
    main()