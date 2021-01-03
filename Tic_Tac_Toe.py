import random

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

def Row_Check(A):
    # This Fuction helps in deciding Winner
    Winner = None
    for i in range(3):
        if((A[i][0] == A[i][1]) and (A[i][0] == A[i][2])):
            if(A[i][0] == 'X'):
                Winner = "Human"
                return True, Winner
            elif(A[i][0] == 'O'):
                Winner = "Computer"
                return True, Winner
    return False, Winner

def Column_Check(A):
    # This Fuction helps in deciding Winner
    Winner = None
    for i in range(3):
        if((A[0][i] == A[1][i]) and (A[0][i] == A[2][i])):
            if(A[0][i] == 'X'):
                Winner = "Human"
                return True, Winner
            elif(A[0][i] == 'O'):
                Winner = "Computer"
                return True, Winner
    return False, Winner

def Digonal_Check(A):
    # This Function helps in deciding Winner
    Winner = None
    if((A[0][0] == A[1][1]) and (A[0][0] == A[2][2])):
        if(A[0][0] == 'X'):
            Winner = "Human"
            return True, Winner
        elif(A[0][0] == 'O'):
            Winner = "Computer"
            return True, Winner
    elif((A[0][2] == A[1][1]) and (A[0][2] == A[2][0])):
        if(A[0][2] == 'X'):
            Winner = "Human"
            return True, Winner
        elif(A[0][2] == 'O'):
            Winner = "Computer"
            return True, Winner
    return False, Winner

def Check_Win(Arr):
    # This Fuction decides the Winner
    Game_Over = False
    Winner = None
    Game_Over_1, Winner_1 = Row_Check(Arr)
    Game_Over_2, Winner_2 = Column_Check(Arr)
    Game_Over_3, Winner_3 = Digonal_Check(Arr)
    if(Game_Over_1 or Game_Over_2 or Game_Over_3):
        Game_Over = True
        if(Game_Over_1):
            Winner = Winner_1
        elif(Game_Over_2):
            Winner = Winner_2
        else:
            Winner = Winner_3
    
    return Game_Over, Winner

def Player_Move(Arr):
    # This Function takes input from the human player
    X, Y = list(map(int, input().split()))
    Flag = 0
    if(Arr[X][Y] != ' '):
        print("Please enter valid mode.")
        Flag = 1
        return Arr, Flag
    Arr[X][Y] = 'X'
    return Arr, Flag

def check_tie(Arr):
    for i in range(3):
        for j in range(3):
            if(Arr[i][j] == ' '):
                return False
    return True

def minimizer_maximizer(board, isMaximizing):

    Game_Over, Winner = Check_Win(board)
    Tie = check_tie(board)

    if Winner == 'Computer':
        return 1
    elif Winner == 'Human':
        return -1
    elif Tie:
        return 0

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if(board[i][j] == ' '):
                    board[i][j] = 'X'
                    score = minimizer_maximizer(board, False)
                    board[i][j] = ' '
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if(board[i][j] == ' '):
                    board[i][j] = 'O'
                    score = minimizer_maximizer(board, True)
                    board[i][j] = ' '
                    bestScore = min(score, bestScore)
        return bestScore

def Computer_Move(board):
    bestScore = float('-inf')
    bestMove = (-1, -1)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                board[i][j] = 'O'
                score = minimizer_maximizer(board, True)
                board[i][j] = ' '
                if(score > bestScore):
                    bestScore = score
                    bestMove = (i, j)
    x, y = bestMove
    board[x][y] = 'O'
    return board

def Game():
    # This Funtion helps in starting the Game
    Arr = []
    for i in range(3):
        Arr.append([' ', ' ', ' '])
    i = 1
    Game_Over = False
    Display_Board(Arr,  0)
    Start = Toss()
    while((Game_Over != True) and i < 9):
        if(Start == 'Computer'):
            Arr = Computer_Move(Arr)
            Display_Board(Arr, i)
            i = i + 1
            Game_Over, Winner = Check_Win(Arr)
            if(Game_Over == False):
                Flag = 1
                while(Flag):
                    Arr, Flag = Player_Move(Arr)
                Game_Over, Winner = Check_Win(Arr)
                Display_Board(Arr, i)
                i = i + 1
        else:
            Flag = 1
            while(Flag):
                Arr, Flag = Player_Move(Arr)
            Game_Over, Winner = Check_Win(Arr)
            Display_Board(Arr, i)
            i = i + 1
            if(Game_Over == False):
                Arr = Computer_Move(Arr)
                Display_Board(Arr, i)
                i = i + 1
                Game_Over, Winner = Check_Win(Arr)

    if(Game_Over == False):
        print("Draw")
    elif(Game_Over == True):
        print(Winner)


Game()
