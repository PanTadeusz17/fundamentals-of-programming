def hide(card_number):
    return card_number[:2] + "*" * 10 + card_number[-4:]

def main():
    print(hide("5290312400019022"))

if __name__ == "__main__":
    main()