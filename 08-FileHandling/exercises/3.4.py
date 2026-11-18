import re

def main():
    email_file = 'report.txt'
    with open(email_file, 'r', encoding='utf-8') as file: # utf-8 to polskie znaki i wogole jakies takie
        email = file.read()

    pattern = r'\d+(?:\.\d+)?' # jedna lub wiecej liczb \ kropka \ jedna lub wiecej liczb, r to raw string zeby bylo tak jak jest napisane a ?: mówisz Pythonowi: „potraktuj kropkę i grosze jako jeden opcjonalny klocek, ale nie wycinaj ich osobno” — dzięki czemu dostajesz pełną kwotę: ['102.50'].
    amounts = re.findall(pattern, email)

    total = 0
    for amount in amounts:
        total += float(amount)

    print(f"Total money spent: {total:.2f}")

if __name__ == "__main__":
    main()