import re

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")

    username_pattern = r'^[a-z]{6,}$' # ^ to poczatek napisu, dalej zbior dowolnych znakow male litery, dalej wymog dlugosci minimum 6 znakow,  $ oznacza koniec napisu ToT
    password_pattern = r'^[A-Za-z0-9_]{8,}$' # tutaj no to podkreslenie po prostu podloga a 0-9 to po prostu liczba

    username_match = re.match(username_pattern, username)
    password_match = re.match(password_pattern, password)

    if username_match and password_match:
        print("Username and password are valid.")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()