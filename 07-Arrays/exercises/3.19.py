def main():
    t = (50, 20, 40, 50, 30, 50)
    value = 50
    print("Tuple:", ",".join(map(str, t)))
    print("Value:", value)
    print("Number of occurrences:", t.count(value))

if __name__ == "__main__":
    main()