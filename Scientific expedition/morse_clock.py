def getPadding(num, l):
    padd = ""
    numLen = len(num)
    while (numLen < l):
        padd += '.'
        numLen += 1
        
    if (num == '0'):
        padd += '.'
        
    return padd

def convToMorse(num):
    conv = ""
    for i in range(0, len(num)):
        if (num[i] == '1'):
            conv += '-'
        else:
            conv += '.'
    return conv

def getMorse(binNum, which):
    mrs = ""
    if (which == 'hh'):
        mrs += getPadding(binNum[0], 2)
        if (binNum[0] != '0'):
            mrs += convToMorse(binNum[0])
        mrs += ' '
        mrs += getPadding(binNum[1], 4)
        if (binNum[1] != '0'):
            mrs += convToMorse(binNum[1])
    else:
        mrs += getPadding(binNum[0], 3)
        if (binNum[0] != '0'):
            mrs += convToMorse(binNum[0])
        mrs += ' '
        mrs += getPadding(binNum[1], 4)
        if (binNum[1] != '0'):
            mrs += convToMorse(binNum[1])
    return mrs

def checkio(data):
    splitdata = data.split(':')
    morse = ""
    
    # Get morse hours
    hh = int(splitdata[0])
    binHh = []
    binHh.append(bin(hh // 10).replace('0b', ''))
    hh -= (10 * (hh // 10))
    binHh.append(bin(hh).replace('0b', ''))
    morse += getMorse(binHh, 'hh') 
    
    morse += " : "
    
    # Get morse minutes
    mm = int(splitdata[1])
    binMm = []
    binMm.append(bin(mm // 10).replace('0b', ''))
    mm -= (10 * (mm // 10))
    binMm.append(bin(mm).replace('0b', ''))
    morse += getMorse(binMm, 'mm') 
    
    morse += " : "
    
    # Get morse seconds
    ss = int(splitdata[2])
    binSs = []
    binSs.append(bin(ss // 10).replace('0b', ''))
    ss -= (10 * (ss // 10))
    binSs.append(bin(ss).replace('0b', ''))
    morse += getMorse(binSs, 'ss') 
    
    return morse
