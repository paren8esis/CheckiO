def checkio(expr):
    O_BRACKETS = ("(", "{", "[")
    C_BRACKETS = (")", "}", "]")
    
    stack = []
    for i in range(0, len(expr)):
        if (expr[i] in O_BRACKETS):
            stack.append(expr[i])
        elif (expr[i] in C_BRACKETS):
            if (len(stack) == 0):
                return False
            prev = stack.pop(-1)
            if (O_BRACKETS.index(prev) != C_BRACKETS.index(expr[i])):
                return False
        else:
            continue
            
    if (len(stack) > 0):
        return False
            
    return True
