def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() # f is a file object
    return file_contents
    
def main():
    print(get_book_text("/Users/torrancesemple/workspace/github.com/TorranceSemple/bookbot/books/frankenstein.txt"))

if __name__ == "__main__":
    main()