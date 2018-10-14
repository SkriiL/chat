import pickle
import string
import random


def caesar(text):
    chiffre = ""
    for letter in text:
        letter = ord(letter) + 2
        letter = chr(letter)
        chiffre += letter
    return chiffre


def monoalphabetic(text):
    chiffre = ""
    dict = pickle.load(open("dict", "rb"))
    for letter in text:
        try:
            chiffre += dict[letter]
        except KeyError:
            chiffre += letter
    return chiffre


def full_encrypt(text):
    first = caesar(text)
    second = monoalphabetic(first)
    return second


def shuffle():
    dict = {}
    all = string.ascii_letters + string.digits
    all_1 = [x for x in all]
    all = [x for x in all]
    random.shuffle(all_1)
    for i in range(0, len(all)):
        dict[all[i]] = all_1[i]
    pickle.dump(dict, open("dict", "wb"))