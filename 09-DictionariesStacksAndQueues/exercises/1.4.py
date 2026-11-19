def main():
    person = {
        "name": "Marek",
        "surname": "Banach",
        "age": 25,
        "hobby": ["swimming", "excursions"],
        "married": True,
        "phone": {"landline": "123444321", "mobile": "777888999"} # tu mamy dict w dict lol
    }

    # 1-3. Wyświetlanie danych
    print("Name:", person["name"])
    print("Hobby:", person["hobby"])
    print("Initial dictionary:", person)

    # 4-8. Modyfikacje i dodawanie danych
    person["surname"] = "Nowak"
    person["married"] = not person["married"]
    person["gender"] = "male"
    person["hobby"].append("bicycle")
    person["phone"]["work"] = "313131444"

    # 9. Wyświetlenie po zmianach
    print("\nUpdated dictionary:")
    for key, value in person.items():
        print(f"{key} : {value}")

if __name__ == "__main__":
    main()