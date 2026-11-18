def main():
    arr = [2.5, 7.1, 3.0, 9.8, 1.2, 6.4]
    threshold = float(input("Enter a number: "))
    count = 0
    for num in arr:
        if num > threshold:
            count += 1
    print("Elements greater than given value:", count)

if __name__ == "__main__":
    main()