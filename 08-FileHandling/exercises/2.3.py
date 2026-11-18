def main():
    original_file = 'healthy_lifestyle.txt'
    target_file = 'copy_healthy_lifestyle.txt'

    with open(original_file, 'r') as file:
        content = file.read()

    with open(target_file, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    main()