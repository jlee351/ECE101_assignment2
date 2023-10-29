
def Prob3( value ):
    #### BEGIN: Your code goes after this line.
    print (value)
    while value != 1:

        if value%2 == 0:
            value //= 2
            print (value)
            
        else:
            value = 3*value + 1
            print (value)
    #### END: Your code must end before this line.
