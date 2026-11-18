def main():
    arr = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(5):
        for j in range(5):
            arr[i][j] = (i + 1) * (j + 1)

    for row in arr:
        for val in row:
            print(f"{val:2}", end=" ")
        print()

if __name__ == "__main__":
    main()