import json

def main():
    favourite = {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8
    }
    with open('favourite.json', 'w', encoding='utf-8') as file:
        json.dump(favourite, file, indent=4)

if __name__ == "__main__":
    main()