def bubblesort(array):
    arr = array.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    a1 = [64, 34, 25, 12, 22, 11, 90]
    a2 = [5, 1, 4, 2, 8]
    a3 = [10, -3, 7, 0, -1, 4]
    for arr in [a1, a2, a3]:
        print("Before:", arr, "-> After:", bubblesort(arr))

if __name__ == "__main__":
    main()