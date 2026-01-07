from stats import get_word_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)

    print(book_text)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

main() 