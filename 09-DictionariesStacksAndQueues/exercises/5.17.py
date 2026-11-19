import json

def main():
    with open('cities.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for city in data:
        for key, value in city.items():
            print(key, ':', value)
        print()

if __name__ == "__main__":
    main()