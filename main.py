import sys
from stats import get_book_text, split_into_words, char_count_by_letter, sort_dictionary_by_value, print_output

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    contents = get_book_text(sys.argv[1])
    split_contents = split_into_words(contents)
    char_count = char_count_by_letter(contents)
    sorted_count = sort_dictionary_by_value(char_count)
    print_output(split_contents, sorted_count)
    return

main()