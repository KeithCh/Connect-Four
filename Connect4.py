import numpy as np
import datetime


# Set starting conditions
board = np.zeros((6, 7))
game_on = True
player = 1
pieces_in_board = 0
FULL = 42 # 6 rows x 7 cols

def check_horizontals(player):
    for y in range(6):
        for x in range(4):
            if all(z == player for z in board[y][x: (x + 4)]):
                return True
    return False


def check_verticals(player):
    for y in range(6):
        for x in range(3):
            k = [board[x][y], board[x + 1][y], board[x + 2][y], board[x + 3][y]]
            if all(z == player for z in k):
                return True
    return False

def check_diagonals(player):
    reverse_board = board.copy()
    for y in range(2):
        if y == 0:
            for i in range(3):
                for x in range(4):
                    diagonals = [board[i][x], board[i+1][x+1],board[i+2][x+2], board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return True

        elif y == 1:
            for i in range(len(reverse_board)):
                reverse_board[i] = list(reversed(reverse_board[i]))
            for i in range(3):
                for x in range(4):
                    diagonals = [reverse_board[i][x], reverse_board[i+1][x+1],reverse_board[i+2][x+2], reverse_board[i+3][x+3]]
                    if all(z == player for z in diagonals):
                        return True

    return False

def check_win(player):
    return check_horizontals(player) or check_verticals(player) or check_diagonals(player)


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
                win = check_win(player)
                if not win:
                    player = 2
            else:
                board[x][y] = 2
                win = check_win(player)
                if not win:
                    player = 1

            pieces_in_board += 1
            return not win, player


def main(player, game_on):
    while game_on:
        print(board,end="\n")
        valid_input = False
        while not valid_input:
            try:
                user_input = eval(input("Player " + str(player) + "'s Turn. Enter a number from 1 to 7.\n"))
                if user_input - 1 > 6 or user_input - 1 < 0:
                    print(board, end="\n")
                    print("Number out of Range")
                else:
                    valid_input = True
            except:
                print(board, end="\n")
                print("Invalid Character Entered")

        update_status = insert_piece(player, user_input - 1)
        player = update_status[1]
        game_on = update_status[0]
    print(board, end="\n")
    if player == 0:
        print("It's a tie!")
    else:
        print("Player " + str(player) + " Wins!")
        text_file_message = "Winner: Player " +  str(player)
    user_input = str(input("Would you like to save the results? (Y/N)\n")).lower()
    while str(user_input) not in  ['y','n']:
        user_input = str(input("Invalid Respons. Please enter Y or N\n"))
    if user_input == 'y':
        player_one_name = str(input("Enter Player 1's Name: "))
        player_two_name = str(input("Enter Player 2's Name: "))
        f = open('Match Results.txt', 'a+')
        contents = f.readlines()
        open("Match Results.txt", "w").close()
        f = open('Match Results.txt', 'a')
        if player == 0:
            text_file_message = '\n{} Tie Game Between {} and {}'.\
                format(str(datetime.datetime.now())[:16], player_one_name, player_two_name)
        elif player == 1:
            text_file_message = '\n{} {} | Loser: {}'.\
                format(str(datetime.datetime.now())[:16], text_file_message.replace("Player 1", "{}".format(player_one_name)), player_two_name)
        else:
            text_file_message = '\n{} {} | Loser: {}'.\
                format(str(datetime.datetime.now())[:16], text_file_message.replace("Player 2", "{}".format(player_two_name)), player_one_name)
        contents.insert(0,text_file_message)
        f.writelines(contents)
        f.close()

main(player, game_on)