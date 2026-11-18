def main():
    total_words = 0
    with open('pets.txt', 'r') as file:
        for line in file:
            print(line, end="")
            words = line.split()
            total_words += len(words)
    print("\nTotal words:", total_words)

if __name__ == "__main__":
    main()