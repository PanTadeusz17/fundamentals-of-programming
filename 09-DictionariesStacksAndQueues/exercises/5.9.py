import csv

def main():
    provinces = {}
    counts = {}

    with open('province.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # pominięcie nagłówka
        for row in reader:
            letter, name = row[0], row[1]
            provinces[letter] = name
            counts[name] = 0

    with open('vehicle.txt', 'r', encoding='utf-8') as file:
        for line in file:
            reg = line.strip()
            if reg:
                first_letter = reg[0]
                if first_letter in provinces:
                    counts[provinces[first_letter]] += 1

    for province, count in counts.items():
        print(f"{province}: {count}")

if __name__ == "__main__":
    main()