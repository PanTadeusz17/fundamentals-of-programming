def main():
    arr = [2, 3, 2, 5, 8, 1, 9, 8]
    print("Array:", *arr)
    print("Unique elements:", end=" ")
    for num in arr:
        if arr.count(num) == 1:
            print(num, end=" ")
    print()

if __name__ == "__main__":
    main()