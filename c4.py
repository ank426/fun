import os, copy

def display(board):
    os.system('cls')
    for row in range(6):
        print('| ',end='')
        for col in range(7):
            print(board[row][col],end=' | ')
        print()
    print('+---+---+---+---+---+---+---+')
    print('  0   1   2   3   4   5   6')
    print()

def play(board, col, turn):
    global flag
    flag=False
    if col not in range(7):
        flag=True
        return
    for row in range(5,-1,-1):
        if board[row][col]==' ':
            break
    else:
        flag=True
        return
    if turn:
        board[row][col]='R'
    else:
        board[row][col]='Y'
    display(board)

def win(board):
    for row in range(6):
        for col in range(4):
            if ' '!=board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]:
                return True, board[row][col]
    for row in range(3):
        for col in range(7):
            if ' '!=board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]:
                return True, board[row][col]
    for row in range(3):
        for col in range(4):
            if ' '!=board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]:
                return True, board[row][col]
    for row in range(3):
        for col in range(3,7):
            if ' '!=board[row][col]==board[row+1][col-1]==board[row+2][col-2]==board[row+3][col-3]:
                return True, board[row][col]
    return False, None

def draw(board):
    for row in range(6):
        for col in range(7):
            if board[row][col]==' ':
                return False
    return True

while True:
    board = [[' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ']]
    turn=True
    flag=False
    print()

    while True:
        n='R' if turn else 'Y'
        
        display(board)
        print(f"{n}'s turn")
        
        col=int(input('Enter column: '))
        play(board,col,turn)
        if flag:
            flag=False
            continue
        
        if win(board)[0]:
            print(win(board)[1],'wins')
            break

        if draw(board):
            print('Draw')
            break

        turn = not turn
    
    n=input('\nPlay again? [Y/N]: ').upper()
    if n=='Y':
        continue
    else:
        break