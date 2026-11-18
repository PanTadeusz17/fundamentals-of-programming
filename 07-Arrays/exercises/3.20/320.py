import MyArrays

def main():
    numbers = [7, 3, 8, 5, 2]
    mm = MyArrays.min_max_array(numbers)
    print("Numbers:", ",".join(map(str, numbers)))
    print("Second largest number:", MyArrays.second_largest(numbers))
    print("Median:", MyArrays.median(numbers))
    print(f"Smallest and largest number: {mm[0]},{mm[1]}")
    print("Numbers as a string:", MyArrays.to_string(numbers))

if __name__ == "__main__":
    main()