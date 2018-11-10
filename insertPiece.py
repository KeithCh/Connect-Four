from globalVar import *
from checkWin import *

def insert_piece(player, y):
    global pieces_in_board
    done = False
    if pieces_in_board == FULL:
        return False, 0
    elif board[0][y] != 0:
        print("Column " + str(y + 1) + " is already filled")
        return True, player
    for x in range(5, -1, -1):
        if not done and (board[x, y] != 1 and board[x, y] != 2):
            if player == 1:
                board[x][y] = 1
                win = check_horizontals(player) or check_verticals(player) or check_verticals(player)
                if not win:
                    player = 2
            else:
                board[x][y] = 2
                win = check_horizontals(player) or check_verticals(player) or check_verticals(player)
                if not win:
                    player = 1

            pieces_in_board += 1
            return not win, player