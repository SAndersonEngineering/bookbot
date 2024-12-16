def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    word_count = get_word_count(book_text)
    sorted_character_counts = dict(sorted(get_character_counts(book_text).items(), reverse=True, key=lambda item: item[1]))


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")

    for character in sorted_character_counts:
        print(f"The '{character}' character was found {sorted_character_counts[character]} times")
    
    print("--- End report ---")

def get_word_count(text):
    count = len(text.split())
    return count

def get_text(path):
    with open(path) as f:
        return f.read()

def get_character_counts(text):
    character_counts = {}
    text = text.lower()

    for c in text:
        if c.isalpha():
            if c not in character_counts:
                character_counts[c] = 1
            else:
                character_counts[c] += 1
    
    return character_counts
    


main()
