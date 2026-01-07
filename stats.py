def get_word_count(text):
    word_count = text.split()
    return len(word_count)

def get_character_count(text):
    characters = {}
    for i in text:
        lower = i.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters