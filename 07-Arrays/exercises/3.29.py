def main():
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()

if __name__ == "__main__":
    main()