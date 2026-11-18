def star(n):
    return "*" * n

def main():
    arr = [2, 6, 4, 9, 7]
    for num in arr:
        print(f"{num}: {star(num)}")

if __name__ == "__main__":
    main()