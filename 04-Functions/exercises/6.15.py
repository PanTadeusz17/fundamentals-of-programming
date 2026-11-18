# Detektor osób w pokoju (minimum 3 jednocześnie)

def f(detector):
    people = 0
    for sign in detector:
        if sign == "+":
            people += 1
        elif sign == "-":
            people -= 1
        if people >= 3:
            return True
    return False

def main():
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))

if __name__ == "__main__":
    main()