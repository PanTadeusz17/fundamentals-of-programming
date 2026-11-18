def main():
    arr = [-15, 8, -31, 47, -2, 19]
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print("Min:", min_val)
    print("Max:", max_val)

if __name__ == "__main__":
    main()