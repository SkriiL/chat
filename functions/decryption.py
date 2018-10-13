import pickle


def caesar(text):
    clear = ""
    for letter in text:
        letter = ord(letter) + -2
        letter = chr(letter)
        clear += letter
    return clear


def monoalphabetic(text):
    clear = ""
    dict = pickle.load(open("dict", "rb"))

    for letter in text:
        for key, value in dict.items():
            if value == letter:
                clear += key
    return clear


def full_decrypt(text):
    first = monoalphabetic(text)
    second = caesar(first)
    return second
