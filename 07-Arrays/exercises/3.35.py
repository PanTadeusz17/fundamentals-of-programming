def print_2d(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()

def main():
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    print("Before:")
    print_2d(arr)

    for row in arr:
        row[0], row[-1] = row[-1], row[0]

    print("\nAfter:")
    print_2d(arr)

if __name__ == "__main__":
    main()