def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() # f is a file object
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(input):
    chars = {}
    text = input.lower()
    for word in text:
        for char in word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def get_report(chars_dict, total_words, file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    # Dict.sorted() method (iterable, key=?, reverse=True/False)
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    # Check to make sure the key is an alpha character
    for i in sorted_dict:
        # If it is: print it on the report
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")
    print("============= END ===============")