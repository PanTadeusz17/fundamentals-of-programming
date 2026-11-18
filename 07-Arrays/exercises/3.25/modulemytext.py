import mytext

def main():
    text = "An apple a day keeps the doctor away"
    print("Text:", text)
    print("Number of words:", mytext.word_count(text))
    print("Words from the longest:", ",".join(mytext.words_by_length(text)))
    print("Words ordered alphabetically:", ",".join(mytext.words_alphabetically(text)))

if __name__ == "__main__":
    main()