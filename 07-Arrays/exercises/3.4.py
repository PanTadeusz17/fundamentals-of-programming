def main():
    arr = [15, 8, 31, 47, 2, 19]
    print("existed array:", *arr)
    print("reverse array:", end=" ")
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    main()