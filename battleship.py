shipping = {  # Dict of boats
    "plane"            : 6,     # key = "Boat name" : val = "Case amount"
    "cruiser"         : 4,
    "destroyer": 3,
    "torpedo"       : 2
}

grid = {  # Dict of boats positions
    ("E10","J10"): "plane",     # key = ("First extremity", "Last extremity")  : val = "Boat's name"
    ("A3","A6")  : "cruiser",
    ("G1","J1")  : "cruiser",
    ("D1","D3")  : "destroyer",
    ("F3","H3")  : "destroyer",
    ("J6","J8")  : "destroyer",
    ("A1","B1")  : "torpedo",
    ("J3","J4")  : "torpedo",
    ("F6","F7")  : "torpedo",
    ("A8","B8")  : "torpedo"
}

       
def battle(dict, ch):

    '''
    
    "battle" is a func to check if the given boat is on the given case.

        type : dict = dict | ch = str.

            - dict : Dict is a dict with the game's case.
            - ch : Ch is a str which represents the case's position.

    This func return "Touched" if the boat is on the case, and "Failed" if there is nothing.

        Use : To use, call the func battle() replacing the two parameters.

        Example : battle(grid, "A7")
                    output : >>> Failed

    '''

    letters = "ABCDEFGHIJ"   # lst with the game's letters
    for key, val in dict.items():     # Loop on the dict
        if key[0][0] == key[1][0]:      # Check if the position is vertical
            x = key[0][0]               # Var "x" with the letter
            for y in range(int(key[0][1:]), int(key[1][1:])+1):     # Loop on the first and last number
                if f"{x}{y}" == ch:     # Check if the case as the same value than x and y (x = the position's letter / y = the loop's number)
                    return "Touched"         # Return "Touched" if the informations are equivalent
        else:
            y = key[0][1:]  # Var "y" with the number
            for x in range(letters.find(key[0][0]), letters.find(key[1][0])+1):   # Loop on the letter's position
                if f"{letters[x]}{y}" == ch:     # Check if the case as the same value than x and y (x = the letter on the var "letters" / y = the position's letter)
                    return "Touché"                 # Return "Touched" if the informations are equivalent

    return "Failed"        # Return "Failed" if the informations are different and no boats are on the case

