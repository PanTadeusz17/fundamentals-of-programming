# Suma powtarzających się cyfr w liczbie
def f(number):
    digits = str(number)
    total = 0
    for d in digits:
        if digits.count(d) > 1:
            total += int(d)
    return total

def main():
    print(f(1027))
    print(f(230335))
    print(f(513553007))

if __name__ == "__main__":
    main()