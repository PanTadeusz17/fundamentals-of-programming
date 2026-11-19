def main():
    basic_data = {
        "name": "Barbara",
        "age": 21
    }
    advanced_data = {
        "status": "student",
        "married": False,
        "interest": ["reading", "swimming"]
    }
    person = {**basic_data, **advanced_data} # ** znaczy rozpakowanie calego dict ze pokazuje wszystko
    print(person)

if __name__ == "__main__":
    main()