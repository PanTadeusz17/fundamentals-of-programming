def to_1d(arr_2d):
    result = []
    for row in arr_2d:
        for val in row:
            result.append(val)
    return result

def main():
    a1 = [[2, 3], [1, 5]]
    a2 = [[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]
    a3 = [[2, 1], [3, 5], [7, 4], [2, 6]]

    for a in [a1, a2, a3]:
        print(to_1d(a))

if __name__ == "__main__":
    main()