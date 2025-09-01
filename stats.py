def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch, count in num_chars_dict.items():
        sorted_list.append({"char": ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
