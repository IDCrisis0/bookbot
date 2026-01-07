def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def main():
    bookPath = "books/frankenstein.txt"
    bookText = get_book_text(bookPath)

    print(bookText)

main()