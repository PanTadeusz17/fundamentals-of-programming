def occurs(number, array):
    return number in array

def main():
    arr = [15, 38, 7, 23, 14]
    number = int(input("Number: "))
    print("Array:", *arr)
    if occurs(number, arr):
        print(f"Result: number {number} appears in the array")
    else:
        print(f"Result: number {number} does not appear in the array")

if __name__ == "__main__":
    main()