def checkio(*args):
    if (len(args) == 0):
        return 0
    return round(max(args) - min(args), 3)
