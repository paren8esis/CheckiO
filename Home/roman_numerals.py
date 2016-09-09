def checkio(data):
    roman = ""
    Ms = data // 1000
    data -= (Ms * 1000)
    if (Ms != 0):
        for i in range(0, Ms):
            roman += "M"
    if (data - 900 < 100) and (data - 900 >= 0):
        roman += "CM"
        data -= 900
    elif (data - 400 < 100) and (data - 400 >= 0):
        roman += "CD"
        data -=400
    else:
        Ds = data // 500
        data -= (Ds * 500)
        if (Ds != 0):
            for i in range(0, Ds):
                roman += "D"
    Cs = data // 100
    data -= (Cs * 100)
    if (Cs != 0):
        for i in range(0, Cs):
            roman += "C"
    if (data - 90 < 10) and (data - 90 >= 0):
        roman += "XC"
        data -= 90
    elif (data - 40 < 10) and (data - 40 >= 0):
        roman += "XL"
        data -= 40
    else:
        Ls = data // 50
        data -= (Ls * 50)
        if (Ls != 0):
            for i in range(0, Ls):
                roman += "L"
    Xs = data // 10
    data -= (Xs * 10)
    if (Xs != 0):
        for i in range(0, Xs):
            roman += "X"
    if (data == 9):
        roman += "IX"
    else:
        Vs = data // 5
        data -= (Vs * 5)
        if (Vs != 0):
            for i in range(0, Vs):
                roman += "V"
        if (data == 4):
            roman += "IV"
        else:
            for i in range(0, data):
                roman += "I"

    return roman
