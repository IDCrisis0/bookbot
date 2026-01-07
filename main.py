from stats import get_word_count, get_char_count, dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    num_chars = get_char_count(book_text)
    chars_sorted = dict_to_sorted_list(num_chars)
    book_report(book_path, num_words, chars_sorted)

# get the text of a specified document.
# book files kept in /books directory of program as .txt.
def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text
    
def book_report(book_path, num_words, chars_sorted):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for i in chars_sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")


main() 