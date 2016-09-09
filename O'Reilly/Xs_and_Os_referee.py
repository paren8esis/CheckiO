def checkio(game_result):
    res = ""
    
    # Check horizontal
    for i in range(0,3):
        if (game_result[i] == "XXX"):
            res = "X"
            break
        if (game_result[i] == "OOO"):
            res = "O"
            break
            
    if (res != ""):
        return res
        
    # Check vertical
    for i in range(0,3):
        col = game_result[0][i]
        col += game_result[1][i]
        col += game_result[2][i]
        if (col == "XXX"):
            res = "X"
            break
        if (col == "OOO"):
            res = "O"
            break
    
    if (res != ""):
        return res
        
    # Check diagonal
    diag = game_result[0][0] + game_result[1][1] + game_result[2][2]
    if (diag == "XXX"):
        res = "X"
    if (diag == "OOO"):
        res = "O"
    diag = game_result[0][2] + game_result[1][1] + game_result[2][0]
    if (diag == "XXX"):
        res = "X"
    if (diag == "OOO"):
        res = "O"


    if (res != ""):
        return res
    return "D"
