import re

def main():
    text = input("Enter text: ")
    vowels = re.findall(r'[aeiouAEIOU]', text)
    print("Number of vowels:", len(vowels))

if __name__ == "__main__":
    main()