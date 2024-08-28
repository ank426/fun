import random

def display(board):
    print()
    for i in range(3):
        for j in range(3):
            print(' ',board[i][j],sep='', end=' ')
            if j != 2:
                print('|',end='')
        print()
        if i != 2:
            print('---+---+---')
    print()

def play():
    display(board)
    global r, c, flag
    r=int(input('Enter row: '))
    c=int(input('Enter column: '))
    if r not in [0,1,2] or c not in [0,1,2]:
        flag = True
        print('Wrong')
        return None
    if board[r][c] == ' ':
        board[r][c] = n
        display(board)
    else:
        print('Wrong')
        flag=True

def sysplay(n):
    display(board)
    global r, c, flag
    if n == 'x':
        '''
        diff_flag = False

        for i in range(3):
            lst = board[i]
            if lst == ['x','x',' ']:
                (r,c) = board[i][2]
                diff_flag = True
            elif lst == ['x',' ','x']:
                (r,c) = board[i][1]
                diff_flag = True
            elif lst == [' ','x','x']:
                (r,c) = board[i][0]
        
        for i in range(3):
            lst = [board[0][i], board[1][i], board[2][i]]
            if lst == ['x','x',' ']:
                (r,c) = board[i][2]
                diff_flag = True
            elif lst == ['x',' ','x']:
                (r,c) = board[i][1]
                diff_flag = True
            elif lst == [' ','x','x']:
                (r,c) = board[i][0]

        lst = [board[0][0], board[1][1], board[2][2]]
        if lst == ['x','x',' ']:
            (r,c) = board[i][2]
            diff_flag = True
        elif lst == ['x',' ','x']:
            (r,c) = board[i][1]
            diff_flag = True
        elif lst == [' ','x','x']:
            (r,c) = board[i][0]

        lst = [board[0][i], board[1][i], board[2][i]]
        if lst == ['x','x',' ']:
            (r,c) = board[i][2]
            diff_flag = True
        elif lst == ['x',' ','x']:
            (r,c) = board[i][1]
            diff_flag = True
        elif lst == [' ','x','x']:
            (r,c) = board[i][0]
        '''

        if board == [ [ ' ' , ' ' , ' ' ] ,
                      [ ' ' , ' ' , ' ' ] ,
                      [ ' ' , ' ' , ' ' ] ]:
            (r,c) = (1,1)
            
        elif board == [ [ ' ' , 'o' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(0,2), (1,2), (2,2), (2,0), (1,0), (0,0)])
            
        elif board == [ [ ' ' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ ' ' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(0,1), (0,2), (2,2), (2,1), (2,0), (0,0)])
            
        elif board == [ [ ' ' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(0,2), (1,2), (2,2), (2,0), (1,0), (0,0)])
            
        elif board == [ [ ' ' , ' ' , ' ' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(0,1), (0,2), (2,2), (2,1), (2,0), (0,0)])
            
        elif board == [ [ ' ' , 'o' , 'x' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ 'o' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(1,2), (2,2)])
            
        elif board == [ [ ' ' , 'o' , ' ' ] ,
                        [ 'o' , 'x' , 'x' ] ,
                        [ ' ' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(1,2), (2,2)])
            
        elif board == [ [ 'o' , 'o' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , 'x' ] ]:
            (r,c) = (0,2)
            
        elif board == [ [ ' ' , 'o' , 'o' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ 'x' , ' ' , ' ' ] ]:
            (r,c) = (0,0)
            
        elif board == [ [ ' ' , 'o' , ' ' ] ,
                        [ 'x' , 'x' , 'o' ] ,
                        [ ' ' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(0,0), (2,0)])
            
        elif board == [ [ 'x' , 'o' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , 'o' ] ]:
            (r,c) = random.choice([(2,0), (1,0)])
            
        elif board == [ [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ ' ' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(0,1), (0,0)])
            
        elif board == [ [ ' ' , ' ' , 'x' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ 'o' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(0,1), (0,0)])
            
        elif board == [ [ 'o' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ ' ' , ' ' , 'x' ] ]:
            (r,c) = random.choice([(2,1), (2,0)])
            
        elif board == [ [ ' ' , 'o' , ' ' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ ' ' , 'x' , ' ' ] ]:
            (r,c) = random.choice([(2,2), (2,0)])
            
        elif board == [ [ ' ' , ' ' , 'o' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ 'x' , ' ' , ' ' ] ]:
            (r,c) = (2,2)
            
        elif board == [ [ 'x' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , 'o' ] ,
                        [ ' ' , ' ' , 'o' ] ]:
            (r,c) = (0,2)
            
        elif board == [ [ ' ' , ' ' , 'x' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ 'o' , 'o' , ' ' ] ]:
            (r,c) = (2,2)
            
        elif board == [ [ ' ' , ' ' , ' ' ] ,
                        [ 'o' , 'x' , 'x' ] ,
                        [ ' ' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(0,2), (2,2)])
            
        elif board == [ [ 'o' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , 'o' , 'x' ] ]:
            (r,c) = random.choice([(0,2), (1,2)])
            
        elif board == [ [ ' ' , ' ' , 'o' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ 'x' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(0,1), (0,0)])
            
        elif board == [ [ ' ' , ' ' , ' ' ] ,
                        [ 'x' , 'x' , 'o' ] ,
                        [ ' ' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(2,0), (0,0)])
            
        elif board == [ [ 'x' , ' ' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ,
                        [ ' ' , 'o' , 'o' ] ]:
            (r,c) = (2,0)
            
        elif board == [ [ ' ' , 'x' , ' ' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ ' ' , 'o' , ' ' ] ]:
            (r,c) = random.choice([(0,2), (0,0)])
            
        elif board == [ [ ' ' , ' ' , 'x' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ 'o' , ' ' , ' ' ] ]:
            (r,c) = (0,0)
            
        elif board == [ [ 'o' , ' ' , ' ' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , 'x' ] ]:
            (r,c) = (2,0)
            
        elif board == [ [ ' ' , 'o' , ' ' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ ' ' , 'x' , ' ' ] ]:
            (r,c) = random.choice([(2,2), (2,0)])
            
        elif board == [ [ ' ' , ' ' , 'o' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ 'x' , ' ' , ' ' ] ]:
            (r,c) = random.choice([(2,2), (2,1)])
            
        elif board == [ [ 'x' , ' ' , ' ' ] ,
                        [ 'o' , 'x' , ' ' ] ,
                        [ ' ' , ' ' , 'o' ] ]:
            (r,c) = random.choice([(0,1), (0,2)])
            
        else:
            print('TBD')

    elif n == 'o':
        pass
    else:
        print('Error')
    board[r][c] = n
    display(board)

def win():
    for row in board:
        if ' '!=row[0]==row[1]==row[2]:
            return True
    for col in range(3):
        if ' '!=board[0][col]==board[1][col]==board[2][col]:
            return True
    if ' '!=board[0][0]==board[1][1]==board[2][2]:
        return True
    if ' '!=board[0][2]==board[1][1]==board[2][0]:
        return True
    return False

while True:
    n=input('\nPlay? [Y/N] ').upper()
    if n=='N':
        break
    elif n=='Y':
        player=input('x or o: ').lower()
    else:
        print('Wrong')
        continue

    board = [ [ ' ' , ' ' , ' ' ] ,
              [ ' ' , ' ' , ' ' ] ,
              [ ' ' , ' ' , ' ' ] ]

    flag=False
    n='x'

    print()
    while True:
        print(n,"'s turn",sep='')
        if n==player:
            play()
        else:
            sysplay(n)

        if flag:
            flag=False
            continue

        w=win()
        if w:
            print(n, 'wins')
            break    
        
        draw = True
        for row in board:
            for i in row:
                if i == ' ':
                    draw = False
        if draw:
            print('Draw')
            break

        if n=='x':
            n='o'
        elif n=='o':
            n='x'
