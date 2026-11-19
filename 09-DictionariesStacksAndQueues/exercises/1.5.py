def main():
    countries = [
        {"name": "Poland", "population": 38000000},
        {"name": "Germany", "population": 83200000},
        {"name": "France", "population": 67800000}, #tablica pieciu dict wow
        {"name": "Spain", "population": 47400000},
        {"name": "Italy", "population": 59000000}
    ]
    print(f"{'COUNTRY':<10} {'POPULATION'}") # <10 znaczy zeby zarezerowowac 10 znakow
    for country in countries:
        print(f"{country['name']:<10} {country['population']}")

if __name__ == "__main__":
    main()


# :<10 — wyrównanie do lewej strony
# :>10 — wyrównanie do prawej strony
# :^10 — wyśrodkowanie tekstu w polu o szerokości 10 znaków