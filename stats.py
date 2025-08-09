def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def split_into_words(text):
    words = text.split()
    return words

def char_count_by_letter(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(characters):
    return characters["char"]
    

def sort_dictionary_by_value(sorted_dictionary):
    list_of_characters = []

    for char, num in sorted_dictionary.items():
        list_of_characters.append({"char": char, "num": num})
        
    list_of_characters.sort(key=sort_on, reverse=False)
    return list_of_characters

def print_output(word_count, sorted_characters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(word_count)} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")