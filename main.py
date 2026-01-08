import sys, os
from stats import get_word_count, get_char_count, dict_to_sorted_list

def main():
    book_dir = "books/"
    book_selection, new_book_path = start_message(book_dir)
    book_text = get_book_text(new_book_path)
    num_chars = get_char_count(book_text)
    num_words = get_word_count(book_text)
    chars_sorted = dict_to_sorted_list(num_chars)
    book_report(new_book_path, book_selection, num_words, chars_sorted)

# get the text of a specified document.
# book files kept in /books directory of program as .txt.

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
        return book_text

# This is the starting messages and input for the user. 
# If valid, the book report will run. 
# If invalid, the program exits.
def start_message(book_path):
    books = book_list(book_path)
    print ("============ WELCOME TO BOOKBOT ============")
    print ("What book would you like to analyze?")
    book_selection = input(f"{books} ")
    for i in books:
        if i == book_selection:
            new_book_path = f"{book_path}{book_selection}.txt"
            break   
    else:
        print("Invalid selection. Type a book from the list. Exiting program, run again.")
        sys.exit(1)

    return book_selection, new_book_path

#This is the book report upon successful pick of a valid book.
# This will get the number of words and number of characters and reverse sort them (high to low).    
def book_report(book_path, book_selection, num_words, chars_sorted):

    print(f"You've picked {book_selection}")
    print (f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for i in chars_sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

# Get the list of books from the /books directory.
# Split out the .txt extension to give the user a list.
def book_list(book_dir):
    books = []
    for i in os.listdir(book_dir):
        full_path = os.path.join(book_dir, i)
        if os.path.isfile(full_path):
            base_name, extension = os.path.splitext(i)
            books.append(base_name)
    return books

main()