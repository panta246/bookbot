def main ():
    book_path = "books/frankenstein.txt"
    print(f"Beginning analysis of {book_path}...")
    book_contents = open_book(book_path)
    word_count = count_words(book_contents)
    print(f"The book contains {word_count} words.")
    character_count = count_characters(book_contents.lower())
    for character, count in character_count.items():
        print(f"{character}: {count}")

def open_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_characters(book_contents):
    character_dict = {}
    for character in book_contents:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

main()