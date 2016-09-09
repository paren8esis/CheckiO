def checkio(words):
    count = 0
    for word in words.split(' '):
        if (word.isalpha()):
            count += 1
            if (count == 3):
                return True
        else:
            count = 0
    return False

