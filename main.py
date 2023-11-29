import string

def get_word_count(text):
    return len(text.split())

def get_letter_frequency(text):
    text = text.lower()
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for char in text:
        if (char in d):
            d[char] += 1
    return d

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    letter_frequency_dict = get_letter_frequency(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_word_count(file_contents)} words found in the document\n\n")
    for key in letter_frequency_dict:
        print(f"the '{key}' character was found {letter_frequency_dict[key]} times")