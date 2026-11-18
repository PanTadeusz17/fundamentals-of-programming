def main():
    arr = [7, 9, 2, 4, 5, 6]
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    arr = evens + odds
    print("arr =", arr)

if __name__ == "__main__":
    main()