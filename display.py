

def displayBoard(gameState):

# please send a 3x3 array with either ' ', 'o', or 'x'

#    a   b   c
# 1  o |   |
#   -----------
# 2    | x |
#   -----------
# 3    |   |

    # first line is always the same
    print ('   a   b   c')

    lineNum = 1

    for line in gameState:
           print ('%s  %s | %s | %s ' % (lineNum, line[0], line[1], line[2]))
           print ('  -----------')
           lineNum += 1


# if __name__ == "__main__":
#     testBoard = [[' ','x','o'],[' ',' ',' '],['o','x','o']]
#     displayBoard(testBoard)
