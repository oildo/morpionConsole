
def whoWon(board):
    for i in range(3):
     # check lines
        if board[i*3] != " " and board[i*3] == board[i*3 + 1] and board[i*3] == board[i*3 + 2]:
            return board[i*3]
     # check columns
        if board[i] != " " and board[i] == board[i+3] and board[i] == board[i+6]:
            return board[i]
     # check diagonal
    if board[4] != " ":
        if board[4] == board[0] and board[4] == board[8]:
             return board[4]
        if board[4] == board[2] and board[4] == board[6]:
             return board[4]
    return " "

def isFull(board):
    for i in range(len(board)):
        if board[i] == " ":
            return False
    return True

def drawBoard(b):
    for i in range(3):
        print(f"{b[i*3]}|{b[i*3 +1]}|{b[i*3 +2]}")
        if i != 2:
            print("-----")
        else:
            print("")

def takeInput():
    userInput = -1
    while userInput < 1 or userInput > 9:
        userInput = int(input("choose a number beteen 1 and 9 (included) : "))
    userInput -= 1 # remove 1 to use this value with lists
    return userInput


# ----------------------------------------------------

# " " means empty, "O" and "X" mean taken

board = []
for i in range(9):
    board.append(" ")

CrossTurn = True
userInput = 0

while whoWon(board) == " " and not isFull(board):
    drawBoard(board)
    
    retry = False # = True if the player has already played

    while True:
        if retry:
            print("this case is already takken")
        userInput = takeInput()
        if board[userInput] == " ":
            break
        retry = True
    
    if CrossTurn:
        board[userInput] = "X"
    else:
        board[userInput] = "O"
    CrossTurn = not CrossTurn


drawBoard(board)
if whoWon(board) != " ":
    print(f"{whoWon(board)} won this game")
else:
    print("draw")


