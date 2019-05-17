from globalVar import *


def check_horizontals(player):
    for y in range(6):
        for x in range(4):
            if all(z == player for z in board[y][x: (x + 4)]):
                return True
    return False


def check_verticals(player):
    for y in range(6):
        for x in range(3):
            k = [board[x][y], board[x + 1][y],
                 board[x + 2][y], board[x + 3][y]]
            if all(z == player for z in k):
                return True
    return False


def check_diagonals(player):
    reverse_board = board.copy()
    for y in range(2):
        if y == 0:
            for i in range(3):
                for x in range(4):
                    diagonals = [board[i][x], board[i+1][x+1],
                                 board[i+2][x+2], board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return True

        elif y == 1:
            for i in range(len(reverse_board)):
                reverse_board[i] = list(reversed(reverse_board[i]))
            print(reverse_board)
            for i in range(3):
                for x in range(4):
                    diagonals = [reverse_board[i][x], reverse_board[i+1]
                                 [x+1], reverse_board[i+2][x+2], reverse_board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return True

    return False
