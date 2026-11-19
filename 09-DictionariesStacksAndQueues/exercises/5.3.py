def main():
    translations = {
        'computer': 'komputer',
        'mouse': 'myszka',
        'keyboard': 'klawiatura',
        'printer': 'drukarka'
    }
    word = input("Enter a word in English: ").strip().lower()
    if word in translations:
        print("Translation:", translations[word])
    else:
        print("Translation is unavailable.")

if __name__ == "__main__":
    main()