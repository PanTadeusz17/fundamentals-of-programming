# Posortowana lista gier z pętlą while i numerowaniem
def main():
    computer_games = [
        "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
        "League of Legends", "Valorant", "Grand Theft Auto V",
        "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
    ]
    sorted_games = sorted(computer_games)

    i = 0
    while i < len(sorted_games):
        print(f"{i + 1}. {sorted_games[i]}")
        i += 1

if __name__ == "__main__":
    main()