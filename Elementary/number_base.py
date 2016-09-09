def checkio(str_number, radix):
    # Check if number exceeds given radix
    if (radix >= 10):
        if ((65 + radix - 10) <= max([ord(x) for x in str_number])):
            return -1
    else:
        if (ord(str(radix)) <= max([ord(x) for x in str_number])):
            return -1
    # Convert number
    return int(str_number, radix)

