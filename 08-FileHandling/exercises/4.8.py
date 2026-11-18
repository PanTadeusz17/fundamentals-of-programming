import re

def main():
    with open('files.txt', 'r', encoding='utf-8') as file:
        for line in file:
            filename = line.strip()
            if re.search(r'\.[a-zA-Z0-9]{4}$', filename):
                print(filename)

if __name__ == "__main__":
    main()

    # Nazwy plików z rozszerzeniem dokładnie 4-znakowym