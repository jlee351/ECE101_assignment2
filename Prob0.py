
def Prob0( num ):
    #### BEGIN: Your code goes after this line.
    num_str = str(num)
    l = list(num_str)

    temp = ""

    for x in l:

        if x == "1":
            x = "One"

        elif x == "2":
            x = "Two"

        elif x == "3":
            x = "Three"

        elif x == "4":
            x = "Four"

        elif x == "5":
            x = "Five"

        elif x == "6":
            x = "Six"

        elif x == "7":
            x = "Seven"

        elif x == "8":
            x = "Eight"

        elif x == "9":
            x = "Nine"

        else:
            x = "Zero"

        temp += x + " "

    print (temp, end = ' ')
    #### END: Your code must end before this line.
