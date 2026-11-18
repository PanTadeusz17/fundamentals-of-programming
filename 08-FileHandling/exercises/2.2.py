def main():
    seven_wonders = [
        "Great Wall of China",
        "Petra",
        "Christ the Redeemer",
        "Machu Picchu",
        "Chichen Itza",
        "Roman Colosseum",
        "Taj Mahal"
    ]
    file_name = 'seven_wonders.txt'
    sorted_wonders = sorted(seven_wonders)

    with open(file_name, 'w') as file:
        for item in sorted_wonders:
            file.write(item + "\n")

if __name__ == "__main__":
    main()