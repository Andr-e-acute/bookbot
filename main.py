import sys
from stats import get_book_wordCount, count_characters,sort_charCount

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    book_text=get_book_text(sys.argv[1])
    book_word_count=get_book_wordCount(book_text)
    char_count=sort_charCount(count_characters(book_text))
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {book_word_count} total words
--------- Character Count ------- """)
    for char in char_count:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")
main()
