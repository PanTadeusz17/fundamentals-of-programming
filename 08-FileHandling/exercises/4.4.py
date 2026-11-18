def main():
    with open('it_company.csv', 'r', encoding='utf-8') as file:
        while True:
            lines_printed = 0
            for _ in range(5):
                line = file.readline()
                if not line:
                    break
                print(line, end="")
                lines_printed += 1
            if lines_printed < 5:
                break
            input("\nPress Enter key...")

if __name__ == "__main__":
    main()