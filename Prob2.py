
def Prob2( rows, columns ):
    #### BEGIN: Your code goes after this line.
    ro = 1
    while ro <= rows:
        col = 1
        
        while col <= columns:
            print(ro*col, end = ' ')
            col += 1
            
        ro += 1
        print()
    #### END: Your code must end before this line.
