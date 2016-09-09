def checkio(number):
    res = ""
    divided = False
    if (number % 3 == 0):
        res += "Fizz" + " "
        divided = True
    if (number % 5 == 0):
        res += "Buzz"
        divided = True

    if (divided):
        return res.strip()
    return str(number)

