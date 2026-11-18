def is_in_range(number, x, y):
    return x <= number <= y

def main():
    print(is_in_range(7, 2, 15))
    print(is_in_range(20, 2, 15))

if __name__ == "__main__":
    main()