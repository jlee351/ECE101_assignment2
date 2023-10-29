
def Prob1( height ):
    #### BEGIN: Your code goes after this line.
    val = 1
    res = ""

    while val <= height:
        res = " "*(height-val) + "*"*val

        val += 1
        print(res),
    #### END: Your code must end before this line.
