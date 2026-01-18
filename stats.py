def get_num_words(text):
    words = text.split()
    return len(words)

def get_unique_char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def sort_on(d):
    return d ["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_chars_list = []
    for char, num in chars_dict.items():
        if char.isalpha():
            sorted_chars_list.append({"char": char, "num": num})
    sorted_chars_list.sort(key=sort_on, reverse=True)
    return sorted_chars_list