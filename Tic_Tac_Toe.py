import random

player = 'X'
oponent = "O"

def Display_Board(Arr, i):

    # This Funtion Displays Tic Tac Toe Game
    print("Move No: " + str(i))
    print()
    print("  ", Arr[0][0], "|", Arr[0][1], "|", Arr[0][2], " ")
    print("---------------")
    print("  ", Arr[1][0], "|", Arr[1][1], "|", Arr[1][2], " ")
    print("---------------")
    print("  ", Arr[2][0], "|", Arr[2][1], "|", Arr[2][2], " ")

def Toss():
    # This Fuction decides how will start the Game
    Number = random.randint(1, 2)
    if(Number == 1):
        return "Computer"
    else:
        return "Human"

def evaluate(board):

    for row in range(3):
        if(board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " "):
            if(board[row][0] == oponent):
                return 10
            else:
                return -10

    for col in range(3):
        if(board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " "):
            if(board[0][col] == oponent):
                return 10
            else:
                return -10

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " "):
        if(board[0][0] == oponent):
            return 10
        else:
            return -10
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " "):
        if(board[0][2] == oponent):
            return 10
        else:
            return -10

    return 0


def isEmpty(board):

    for row in range(3):
        for col in range(3):
            if(board[row][col] == " "):
                return True

    return False


def minimizer_maximizer(board, depth, isMaximizer):

    score = evaluate(board)
    if(score == 10):
        return 10 - depth
    elif(score == -10):
        return depth - 10

    if(isEmpty(board) == False):
        return 0

    if(isMaximizer):
        bestScore = float("-inf")
        for row in range(3):
            for col in range(3):
                if(board[row][col] == " "):
                    board[row][col] = oponent
                    score = minimizer_maximizer(board, depth + 1, not isMaximizer)
                    if(score > bestScore):
                        bestScore = score
                    board[row][col] = " "
        return bestScore
    else:
        bestScore = float("inf")
        for row in range(3):
            for col in range(3):
                if(board[row][col] == " "):
                    board[row][col] = player
                    score = minimizer_maximizer(board, depth + 1, not isMaximizer)
                    if(score < bestScore):
                        bestScore = score
                    board[row][col] = " "
        return bestScore


def bestMove(board):

    bestMove = None
    bestScore = float("-inf")
    for row in range(3):
        for col in range(3):
            if(board[row][col] == " "):
                board[row][col] = oponent
                score = minimizer_maximizer(board, 0, False)
                if(score > bestScore):
                    bestScore = score
                    bestMove = (row, col)
                board[row][col] = " "
    
    if(bestMove != None):
        x, y = bestMove
        board[x][y] = oponent
    
    return board

def Player_Move(board):
    # This Function takes input from the human player
    Flag = 1
    while(Flag):
        X, Y = list(map(int, input().split()))
        if(board[X][Y] == ' '):
            Flag = 0
            board[X][Y] = player
        else:
            print("Please enter valid mode.")
    
    return board

def Game():

    board = []
    for _ in range(3):
        board.append([' ', ' ', ' '])
    
    Display_Board(board,  0)
    Start = Toss()
    empty = True
    score = 0
    i = 1
    while(empty and score == 0):
        if(Start == "Computer"):
            board = bestMove(board)
            Display_Board(board, i)
            i = i + 1
            empty = isEmpty(board)
            score = evaluate(board)
            if(empty and score == 0):
                board = Player_Move(board)
                Display_Board(board, i)
                i = i + 1
                empty = isEmpty(board)
                score = evaluate(board)
        else:
            board = Player_Move(board)
            Display_Board(board, i)
            i = i + 1
            empty = isEmpty(board)
            score = evaluate(board)
            if(empty and score == 0):
                board = bestMove(board)
                Display_Board(board, i)
                i = i + 1
                empty = isEmpty(board)
                score = evaluate(board)

    if(score == 10):
        print("Better Luck Next Time....")
    elif (score == -10):
        print("Winner Winner Chicken Dinner!!!")
    else:
        print("Draw")

Game()

