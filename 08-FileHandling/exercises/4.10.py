import csv

def main():
    with open('clothing.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row['Price']) < 60 and int(row['Stock']) < 40:
                print(f"{row['Product_Name']} (Price: {row['Price']}, Stock: {row['Stock']})")

if __name__ == "__main__":
    main()