#---Part 1---#
# This part will check for 

# Iterating through the board to find empty positions (Blank position/ No digits)
def SudukoGrid_Empty(Grid, length):
    #We know that the board will have 9 rows and columns [2D Array]
    #If the current position we are in is empty, we store it.
    for row in range(0,9):
        for col in range (0,9):
            if(Grid[row][col] == 0):
                length[0] = row
                length[1] = col
                return True
    return False

# Iterating through each row to find filled digits (A number value in a position)
def SudukoGrid_Row(Grid, row, num):
    #We know that a row will contain 9 rows
    #If the position of the current row contains a digit; return True
    for i in range(0,9):
        if(Grid[row][i] == num):
            return True
    return False


# Iterating through each col to find filled digits (A number value in a position)
def SudukoGrid_Col(Grid, col, num):
    #We know that a col will contain 9 rows
    #If the position of the current row contains a digit; return True
    for i in range(0,9):
        if(Grid[col][i] == num):
            return True
    return False

# Iterating through each row and col to check/validate (A number value is in that position)
def SudukoGrid_Check(Grid, row, col, num):
    #We know that a whole Suduk Board is (9 * 9); which is made of a 9 grids of (3*3)
    #If the position of the current row contains a digit; return True
    for i in range(0,3):
        for j in range(0,3):
            if (Grid[i + row][j + col] == num):
                return True
    return False
