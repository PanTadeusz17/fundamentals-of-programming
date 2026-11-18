# Weryfikacja cyfry kontrolnej kodu produktu
def f(product_code):
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    return digits_sum % 7 == int(product_code[3])

def main():
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))

if __name__ == "__main__":
    main()
    