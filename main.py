def main():
    """Main Function For BookBot, returns desired information on Book"""
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = dict_sort(chars_dict)
    print(text)
    print(word_count)

    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f" '{item['char']}' found {item['num']} times in the text")

    print(" -- END REPORT -- ")


def get_book_text(path):
    """Book Reading Function, Returns Entire Text of File"""
    with open(path, encoding="utf-8") as f:
        return f.read()


def get_word_count(text):
    """Word Counting Function"""
    words = text.split()
    return len(words)


def get_chars_dict(text):
    """Letter Counting Function"""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    """Sub-Sorting Function"""
    return d["num"]


def dict_sort(chars_dict):
    """Dictionary Sorting Function, Alphabet Only"""
    sorted_list = []
    for key in chars_dict:
        sorted_list.append({"char": key, "num": chars_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
