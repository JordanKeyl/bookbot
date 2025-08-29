def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text = text.lower()
    chars = {}

    for ch in text:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    return chars