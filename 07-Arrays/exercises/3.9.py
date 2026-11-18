def main():
    names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
    longest = names[0]
    for name in names:
        if len(name) > len(longest):
            longest = name
    print("Names:", *names)
    print("Longest name:", longest)

if __name__ == "__main__":
    main()