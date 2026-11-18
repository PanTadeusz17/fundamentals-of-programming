import csv

def read_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def filter_by_genre(books, genre):
    return [book for book in books if book['Genre'] == genre]

def save_books(filename, books):
    with open(filename, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(",".join(book.values()) + "\n")

def main():
    genre_files = {
        "Fantasy": "books_fantasy.txt",
        "Historical": "books_historical.txt",
        "Romance": "books_romance.txt",
        "Classic": "books_classic.txt"
    }
    all_books = read_books('books.csv')

    for genre, out_file in genre_files.items():
        matched = filter_by_genre(all_books, genre)
        save_books(out_file, matched)

if __name__ == "__main__":
    main()