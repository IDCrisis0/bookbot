def main():
    bookPath = "books/frankenstein.txt"
    bookText = get_book_text(bookPath)
    num_words = get_word_count(bookText)

    print(bookText)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

def get_word_count(bookText):
    word_count = bookText.split()
    return len(word_count)

main() 