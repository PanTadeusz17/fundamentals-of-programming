import lettercounter

def main():
    text = "You never get a second chance to make a first impression"
    letter = "e"
    result = lettercounter.count_letter(text, letter)

    print(text)
    print(f"The number of letter '{letter}': {result}")

if __name__ == "__main__":
    main()