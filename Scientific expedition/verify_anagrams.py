# -*- coding: utf-8 -*-

def verify_anagrams(first_word, second_word):
    first_word = first_word.lower().replace(' ', '')
    second_word = second_word.lower().replace(' ', '')
    letter_set_1 = [x for x in first_word]
    letter_set_2 = [x for x in second_word]

    for letter in letter_set_1:
        if (letter not in letter_set_2):
            return False
        letter_set_2.remove(letter)
    if (len(letter_set_2) == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    assert verify_anagrams("---...---...", "-- . -... -- . -.") == True, "The Correct Morse Code"
    assert verify_anagrams("---...---...", "-- . -.. -- . -.") == False, "The False Morse Code"