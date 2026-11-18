import csv #ładuje wbudowany w Pythona moduł do wygodnego odczytu i zapisu plików CSV (Comma-Separated Values), czyli prostych tabel zapisanych w formie tekstu, gdzie kolejne kolumny oddzielone są przecinkami

def main():
    print("GRAPHIC DESIGNERS")
    print("=================")
    with open('it_company.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Job Title'] == 'Graphic Designer':
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")

if __name__ == "__main__":
    main()