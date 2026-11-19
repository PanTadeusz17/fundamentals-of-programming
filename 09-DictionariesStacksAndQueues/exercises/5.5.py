def main():
    paragraph = "cat dog mouse cat rat cat mouse"
    counts = {}
    for word in paragraph.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()