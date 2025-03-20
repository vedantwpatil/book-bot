def calc_num_words(book_text: str):
    num_words = book_text.split()
    return len(num_words)


def count_characters(book_text: str):
    frequency = {}
    for line in book_text.split():
        for word in line.split():
            for character in word:
                if character.lower() in frequency:
                    frequency[character.lower()] = frequency[character.lower()] + 1
                else:
                    frequency[character.lower()] = 1
    return frequency


def sort_dictionary(frequency_table):
    frequency_table.sort(reverse=True, key=)
    return frequency_table
