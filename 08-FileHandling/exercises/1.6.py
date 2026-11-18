def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

def main():
    file_content = read_from_file('countries.txt')
    file_lines = sorted(file_content.splitlines())
    for line in file_lines:
        print(line)

if __name__ == "__main__":
    main()