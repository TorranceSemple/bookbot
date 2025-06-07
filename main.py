from stats import *
import sys
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_dict = get_num_char(text)
    get_report(char_dict, word_count, path)


if __name__ == "__main__":
    main()