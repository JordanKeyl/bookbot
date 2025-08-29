from stats import get_num_words, get_num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    num_char = get_num_characters(text)
    print(num_char)

# gets a file path and returns the contents
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
