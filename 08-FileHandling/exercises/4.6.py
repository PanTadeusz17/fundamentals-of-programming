def main():
    file_name = input("File name: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        lines = len(content.splitlines())
        characters = len(content)
        words = len(content.split())

        print("Number of lines:", lines)
        print("Number of characters:", characters)
        print("Number of words:", words)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' does not exist.")

if __name__ == "__main__":
    main()