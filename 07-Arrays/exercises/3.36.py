def identity_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def print_2d(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()

def main():
    for size in [3, 5, 8]:
        print(f"Size {size}:")
        print_2d(identity_matrix(size))
        print()

if __name__ == "__main__":
    main()