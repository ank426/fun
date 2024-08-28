import os,copy,random

def display(board):
    # os.system('cls')
    for row in range(3):
        for col in range(3):
            print(' ',board[row][col],sep='', end=' ')
            if col != 2:
                print('|',end='')
        print()
        if row != 2:
            print('---+---+---')
    print()

def play(board,r,c,turn):
    global flag
    flag=False
    if r not in [0,1,2] or c not in [0,1,2]:
        flag = True
        return
    elif board[r][c] != ' ':
        flag = True
        return
    if turn:
        board[r][c] = 'x'
    else:
        board[r][c] = 'o'
    display(board)

def win(board):
    for row in board:
        if ' '!=row[0]==row[1]==row[2]:
            return True, row[0]
    for col in range(3):
        if ' '!=board[0][col]==board[1][col]==board[2][col]:
            return True, board[0][col]
    if ' '!=board[0][0]==board[1][1]==board[2][2]:
        return True, board[0][0]
    if ' '!=board[0][2]==board[1][1]==board[2][0]:
        return True, board[0][2]
    return False, None

def draw(board):
    for row in board:
        for i in row:
            if i == ' ':
                return False
    return True

def think(board, turn):
    w=win(board)
    if w[0]:
        if w[1]=='x':
            return 1, 1
        elif w[1]=='o':
            return -1, -1
    elif draw(board):
        return 0, 0
    else:
        if turn:
            L=[]
            for row in range(3):
                for col in range(3):
                    if board[row][col]==' ':
                        newboard=copy.deepcopy(board)
                        newboard[row][col]='x'
                        L.append(newboard)
            result=list(map(lambda x: think(x, not turn)[0], L))
            return max(result), (result.count(1)/len(result) if result else None)
        else:
            L=[]
            for row in range(3):
                for col in range(3):
                    if board[row][col]==' ':
                        newboard=copy.deepcopy(board)
                        newboard[row][col]='o'
                        L.append(newboard)
            result=list(map(lambda x: think(x, not turn)[0], L))
            return min(result), (result.count(1)/len(result) if result else None)

def sysplay(board, turn):
    d={}
    if turn:
        for row in range(3):
            for col in range(3):
                if board[row][col]==' ':
                    newboard=copy.deepcopy(board)
                    newboard[row][col]='x'
                    d[(row,col)] = think(newboard, not turn)
        best=max(d.values(), key=lambda x: x[0])[0]
        print('d',d)
        nd={}
        for move in d:
            if d[move][0]==best:
                nd[move]=d[move]
        print('nd',nd)
        newbest=min(nd.values(), key=lambda x: x[1])[1]
        nnd={}
        for move in nd:
            if nd[move][1]==newbest:
                nnd[move]=nd[move]
        print('nnd',nnd)
        move=random.choice(list(nnd.keys()))
        play(board,move[0],move[1],turn)
    else:
        for row in range(3):
            for col in range(3):
                if board[row][col]==' ':
                    newboard=copy.deepcopy(board)
                    newboard[row][col]='o'
                    d[(row,col)] = think(newboard, not turn)
        best=min(d.values(),key=lambda x: x[0])[0]
        nd={}
        for move in d:
            if d[move][0]==best:
                nd[move]=d[move]
        newbest=max(nd.values(), key=lambda x: x[1])[1]
        nnd={}
        for move in nd:
            if nd[move][1]==newbest:
                nnd[move]=nd[move]
        move=random.choice(list(nnd.keys()))
        play(board,move[0],move[1],turn)

while True:
    print('1. CvC   2. CvP   3. PvC   4. PvP')
    choice=int(input('Choice: '))

    board=[ [ ' ' , ' ' , ' ' ] ,
            [ ' ' , ' ' , ' ' ] ,
            [ ' ' , ' ' , ' ' ] ]

    turn=True
    flag=False

    print()
    while True:
        n='x' if turn else 'o'

        display(board)
        print(f"{n}'s turn")

        if turn:
            if choice==1 or choice==2:
                sysplay(board, True)
            else:
                r=int(input('Enter row: '))
                c=int(input('Enter column: '))
                play(board, r, c, True)
        else:
            if choice==1 or choice==3:
                sysplay(board, False)
            else:
                r=int(input('Enter row: '))
                c=int(input('Enter column: '))
                play(board, r, c, False)

        if flag:
            flag=False
            continue

        if win(board)[0]:
            print(n, 'wins')
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