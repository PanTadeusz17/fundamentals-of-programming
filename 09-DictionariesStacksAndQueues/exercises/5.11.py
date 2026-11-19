import json #tlumaczy pliki javascriptu zeby python ogarnial do czytania pisania i dodawania napisow r w a

def main():
    file_name = 'voting.json'
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            votes = json.load(file) #czyta otwarty plik ('r') i zamienia jego zawartość na słownik lub listę w Pythonie. w następnej linijce możesz odwoływać się do pól przez data['klucz'] albo puszczać po nich pętlę for.
    except (FileNotFoundError, json.JSONDecodeError):
        votes = {}

    person_name = input('Name of the person you are voting for: ')
    votes[person_name] = votes.get(person_name, 0) + 1

    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(votes, file, indent=4, ensure_ascii=False) #dump bierze słownik lub listę z Pythona i zapisuje je do otwartego pliku ('w'). indent 4 to 4 spacje a to ensure ascii wymusza zapisywanie polskich znaków (ą, ę, ł)

    print("Current voting results:", votes)

if __name__ == "__main__":
    main()