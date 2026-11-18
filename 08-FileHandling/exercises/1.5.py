def main():
    with open('countries.txt', 'r') as file:
        counter = 1
        for line in file:
            print(f"{counter}. {line}", end="") #Każda wczytana linijka ma już na końcu niewidoczny znak nowej linii \n, dlatego przy wypisywaniu dodaje się print(line, end=""), żeby nie robić pustych odstępów między wierszami.
            counter += 1

if __name__ == "__main__":
    main()