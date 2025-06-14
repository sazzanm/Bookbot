from stats import number_of_words, number_of_characters, sort_characters
import sys
import os

def get_book_text(book):
    """
    This function reads the content of a text file and returns it as a string.
    :param book: The path to the text file.
    :return: The content of the text file as a string.
    """
    new_string = open(book, 'r').read()
    return new_string


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    # Check if the file exists
    if not os.path.exists(path):
        print(f"Error: File '{path}' not found.")
        sys.exit(1)

    
    book = sys.argv[1]
    texto = get_book_text(book)
    texto2 = number_of_words(texto)
    texto3 = number_of_characters(texto)
    sorted_characters = sort_characters(texto3)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book}")
    print("----------- Word Count ----------")
    print(f"Found {texto2} total words")
    print("---------- Character Count -------")
    for char, count in sorted_characters:
        print(f"{char}: {count}")

main()