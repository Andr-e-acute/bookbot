def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_book_wordCount(book_text):
    return len(book_text.split())
def main():
    book_text=get_book_text('books/frankenstein.txt')
    book_word_count=get_book_wordCount(book_text)
    print(f'{book_word_count} words found in the document')

main()
