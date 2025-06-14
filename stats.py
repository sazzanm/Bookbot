def number_of_words(get_book_text):
    """
    This function counts the number of words in a given text.
    :param get_book_text: The text to count words in.
    :return: The number of words in the text.
    """
    words = get_book_text.split()
    return len(words)

def number_of_characters(get_book_text):
    convert = get_book_text.lower()
    dic_char = {'': 0}  # Initialize with an empty character to avoid KeyError}
    for char in convert:
        if char in dic_char:
            dic_char[char] += 1
        else:
            dic_char[char] = 1
    return dic_char # Return the dictionary of character counts

def sort_characters(dic_char):
      # Filter out non-alphabetic characters
    fixed_characters = {k: v for k, v in dic_char.items() if k.isalpha()}
    """
    This function sorts the characters in a dictionary by their frequency.
    :param dic_char: The dictionary of character counts.
    :return: A sorted list of tuples (character, count).
    """
    sorted_characters = sorted(fixed_characters.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters 