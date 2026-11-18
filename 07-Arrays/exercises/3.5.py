def main():
    arr = [8, 2, 5, 1, 9]
    print("Array:", *arr)
    print("2nd power:", end=" ")
    for x in arr:
        print(x ** 2, end=" ")
    print()

if __name__ == "__main__":
    main()