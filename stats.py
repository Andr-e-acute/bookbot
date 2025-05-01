def get_book_wordCount(book_text):
    return len(book_text.split())
def count_characters(book_text):
    charCount={}
    for char in book_text:
        lowerChar=char.lower()
        if lowerChar in charCount:
            charCount[lowerChar]+=1
        else:
            charCount[lowerChar]=1
    return charCount

def sort_charCount(charCount):
    list_charCount=list(charCount.items())
    list_charCount.sort(key=lambda x: x[1], reverse=True)
    return list_charCount
    