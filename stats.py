# gets the total word count of a specified text
def get_word_count(text):
    word_count = text.split()
    return len(word_count)

# lowers all characters, and then counts the total of a specified text
def get_char_count(text):
    char = {}
    for i in text:
        lowered = i.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char

# used to sort dictionary items by a specific value.
def sort_on(items):
    value = "num"
    return items[value]

def dict_to_sorted_list(num_chars):
    sorted_list = []
    for i in num_chars:
        sorted_list.append({"char": i, "num": num_chars[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
