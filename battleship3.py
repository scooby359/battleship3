from random import randint

board = []
hit1 = 0
ship_col = 0
ship_col2 = 0
ship_col_row = 0  
ship_row = 0
ship_row2 = 0
ship_row_col = 0


for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship 3: They Go Both Ways!"
print ""
#print_board(board)

def random_row(board):
    return randint(0, len(board) - 2)

def random_col(board):
    return randint(0, len(board[0]) - 2)

ship_direction = randint(0,1) # 0 = horizontal  1 = vertical

print ship_direction #just sticking this in for now so I know which way were playing

if ship_direction == 0:
    ship_col = random_col(board)
    ship_col2 = ship_col + 1
    ship_col_row = random_row(board) + 1  
    board[ship_col_row][ship_col] = "?" # so I know where we are
    board[ship_col_row][ship_col2] = "?"

else:
    ship_row = random_row(board)
    ship_row2 = ship_row + 1
    ship_row_col = random_col(board) + 1
    board[ship_row][ship_row_col] = "?" # so I know where we are
    board[ship_row2][ship_row_col] = "?"

print_board(board) #to show where were playing

print ""

if ship_direction == 0:
    print "Ship col %s" % ship_col
    print "Ship col two %s" % ship_col2
    print "Ship row %s" % ship_col_row
else:
    print "Ship row %s" % ship_row
    print "Ship row two %s" % ship_row2
    print "Ship col %s" % ship_row_col


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print ""
    print ""
    print "Turn", turn + 1
    print ""
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
    elif (guess_row == (ship_row or ship_row2 or ship_col_row)) and (guess_col == (ship_col or ship_col2 or ship_row_col)):
        board[guess_row][guess_col] = "*"
        print_board(board)
        if hit1 == 0:
            hit1 = 1
            print "You hit something! Keep going!"
        else:
            print "Well done! You beat me!"
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        else:
            if turn == 3:
                print ""
                print "Sorry, You've used all your guesses! Game Over"
                break
            else:                
                print ""
                print "You missed my battleship!"
                print ""
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
        print_board(board)
