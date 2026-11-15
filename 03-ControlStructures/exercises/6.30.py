# Zewnętrzna pętla: 7 wierszy (zaczynamy w każdym wierszu od innej liczby: 1..7)
for row in range(1, 8):
    # Wewnętrzna pętla: 7 kolumn
    for col in range(7):
        # Wypisujemy liczbę startową wiersza + wielokrotność siódemki
        number = row + (col * 7)
        print(f"{number}", end=" ")
    print() 