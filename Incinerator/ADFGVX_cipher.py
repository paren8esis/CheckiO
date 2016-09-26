# -*- coding: utf-8 -*-

def encode(message, secret_alphabet, keyword):
    
    # Create the alphabet table
    alph = {}
    i = 0
    for row in ['A', 'D', 'F', 'G', 'V', 'X']:
        for col in ['A', 'D', 'F', 'G', 'V', 'X']:
            alph[secret_alphabet[i]] = row + col
            i += 1
    print(alph)

    # Encode the message
    enc_message = ''.join([alph[m] for m in [m for m in message.lower().replace(' ', '') if (m.isalpha() or m.isdigit())]])
    print(enc_message)

    # Use the keyword
    letters_used = set()
    letters_used_add = letters_used.add
    keyword = ''.join([x for x in keyword if not (x in letters_used or letters_used_add(x))])
    d = {}
    for i in range(len(keyword)):
        d[keyword[i]] = ''
        for j in range(len(enc_message) // len(keyword)):
            d[keyword[i]] += enc_message[i + (j * len(keyword))]
        if (i < len(enc_message) % len(keyword)):
            d[keyword[i]] += enc_message[i + ((len(enc_message) // len(keyword)) * len(keyword))]
    print(d)


    # Encode the final message
    res = ''
    for el in sorted(keyword):
        res += d[el]

    return res


def decode(message, secret_alphabet, keyword):
    letters_used = set()
    letters_used_add = letters_used.add
    keyword = ''.join([x for x in keyword if not (x in letters_used or letters_used_add(x))])

    # Find the column ordering of the keyword
    d = {}
    j = 0
    for i in sorted(keyword):
        step = len(message) // len(keyword)
        if (keyword.index(i) < len(message) % len(keyword)):
            step += 1
        d[i] = message[j:j+step]
        j += step

    # Re-arrange the encrypted message
    message = [''] * len(message)
    for i, el in enumerate(keyword):
        for letter in d[el]:
            message[i] = letter
            i += len(keyword)
    print(message)

    # Create the alphabet table
    alph = {}
    i = 0
    for row in ['A', 'D', 'F', 'G', 'V', 'X']:
        for col in ['A', 'D', 'F', 'G', 'V', 'X']:
            alph[row + col] = secret_alphabet[i]
            i += 1
    print(alph)

    # Decode the encrypted message using the alphabet table
    return ''.join([alph[message[i] + message[i + 1]] for i in range(0, len(message), 2)])