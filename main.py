import sys
from stats import *

def get_book_text(path):
    try:
        with open(path) as f:
            contents = f.read()
        return contents
    except Exception as e:
        print(e)
    
def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        file_path = sys.argv[1]

        word_count = get_word_count(get_book_text(file_path))
        char_count = get_char_count(get_book_text(file_path))
        sorted_dict = get_sorted_dict(char_count)
        
        print("============ BOOKBOT ============")
        
        print(f"Analyzing book found at {file_path}...")

        print("----------- Word Count ----------")

        print(f"Found {word_count} total words")
        
        print("--------- Character Count -------")
        
        for key, value in sorted_dict.items():
            if key.isalpha():
                print(f"{key}: {value}")

        print("============= END ===============")
    except Exception as e:
        print(e)

main()