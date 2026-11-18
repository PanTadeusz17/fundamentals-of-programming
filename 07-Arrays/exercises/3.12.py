def main():
    arr1 = [4, 36, 12, 28, 9, 44, 5]
    arr2 = [5, 1, 36]
    for num in arr1:
        if num not in arr2:
            print(num, end=" ")
    print()

if __name__ == "__main__":
    main()