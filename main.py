from stats import calc_num_words
from stats import count_characters


def get_book_text(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        return str(content)


def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    frequency_table = count_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    print("----------- Word Count ----------")
    print(f"Found {calc_num_words(text)} total words")

    print("--------- Character Count -------")


main()
