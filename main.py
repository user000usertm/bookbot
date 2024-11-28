def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_count = get_words_count(text)
    letters_count = get_letters_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(letters_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return (len(words))

def get_letters_count(text):
    letters_dict = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letters_dict:
            letters_dict[lowered] += 1
        else:
            letters_dict[lowered] = 1
    return letters_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()  