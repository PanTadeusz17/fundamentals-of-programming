def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    return [[m[r][c] for r in range(rows)] for c in range(cols)]

def print_2d(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()

def main():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ]
    m3 = [
        [5, 6, 7, 8]
    ]
    for m in [m1, m2, m3]:
        print_2d(transpose_matrix(m))
        print()

if __name__ == "__main__":
    main()