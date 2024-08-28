import copy
import os
import time

nr = 8
nc = 8


def display(board):
    os.system("clear")
    for row in range(nr):
        print("+---" * nc + "+")
        print("| ", end="")
        for col in range(nc):
            print(board[row][col], end=" | ")
        print()
    print("+---" * nc + "+")


def play():
    global board
    newboard = copy.deepcopy(board)

    for row in range(nr):
        for col in range(nc):
            neighbors = [
                (row - 1, col),
                (row - 1, col + 1),
                (row, col + 1),
                (row + 1, col + 1),
                (row + 1, col),
                (row + 1, col - 1),
                (row, col - 1),
                (row - 1, col - 1),
            ]
            neighbors = list(
                filter(lambda t: t[0] in range(nr) and t[1] in range(nc), neighbors)
            )

            c = 0
            for i in neighbors:
                if board[i[0]][i[1]] == "#":
                    c += 1

            if newboard[row][col] == "#":
                if c == 2 or c == 3:
                    pass
                else:
                    newboard[row][col] = " "
            elif newboard[row][col] == " ":
                if c == 3:
                    newboard[row][col] = "#"
                else:
                    pass
    board = newboard
    display(board)


# board=[[' ']*nc]*nr
board = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "#", " ", " ", " ", " "],
    [" ", " ", " ", "#", "#", " ", " ", " "],
    [" ", " ", " ", "#", "#", " ", " ", " "],
    [" ", " ", " ", " ", "#", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
]

display(board)
time.sleep(1)
while True:
    play()
    time.sleep(1)

