def count_letter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    return count

def main():
    print(count_letter("test text", "t"))

if __name__ == "__main__":
    main()