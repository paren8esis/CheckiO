# -*- coding: utf-8 -*-

VOWELS = "aeiouy"

def translate(phrase):
    words = phrase.split()

    res = ''
    for word in words:
        i = 0
        while i < len(word):
            if (word[i] in VOWELS):
                res += word[i]
                i += 3
            else:
                res += word[i]
                i += 2
        res += ' '
    return res.rstrip()