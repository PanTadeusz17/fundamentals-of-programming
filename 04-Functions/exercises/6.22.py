# Akronim z pierwszych liter słów
def f(name):
    acronym = ""
    for word in name.split():
        acronym += word[0]
    return acronym

def main():
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))

if __name__ == "__main__":
    main()