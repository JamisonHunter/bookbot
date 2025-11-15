def get_word_count(book_text):
    word_list = book_text.split()
    return len(word_list)

def get_char_count(book_text):
    char_count = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_dict(char_dict):
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse = True))
    return sorted_dict