def main():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    for i in range(len(matrix)):
        matrix[i][i] = 1

    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

if __name__ == "__main__":
    main()