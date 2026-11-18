# Usuwanie spacji ze zdania
def f(sentence):
    return sentence.replace(" ", "")

def main():
    print(f("integrated development environment"))
    print(f("A programming language is a system of notation for writing computer programs"))

if __name__ == "__main__":
    main()