import rangechecker

def main():
    number = int(input("A number: "))
    x = 2
    y = 15

    if rangechecker.is_in_range(number, x, y):
        answer = "yes"
    else:
        answer = "no"

    print(f"Number {number} in the range <{x},{y}>: {answer}")

if __name__ == "__main__":
    main()