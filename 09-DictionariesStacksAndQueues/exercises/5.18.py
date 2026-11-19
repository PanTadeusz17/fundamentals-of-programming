import json

def main():
    with open('dogs.json', 'r', encoding='utf-8') as file:
        dogs = json.load(file)

    for dog in dogs:
        if dog['age'] < 5:
            for key, value in dog.items():
                print(f"{key}: {value}")
            print()

if __name__ == "__main__":
    main()