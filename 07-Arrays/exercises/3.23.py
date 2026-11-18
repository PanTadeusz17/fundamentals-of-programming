def is_subset(arr1, arr2):
    for item in arr1:
        if item not in arr2:
            return False
    return True

def main():
    a1 = [3, 5, 1]
    a2 = [1, 2, 3, 4, 5, 6]
    print("Is subset:", is_subset(a1, a2))

if __name__ == "__main__":
    main()