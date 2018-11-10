from globalVar import *
from insertPiece import *
from saveResults import *

def game(player, game_on):
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
    saveResults();

while __name__ == '__main__':
    game(player, game_on)
    user_input = input("New Game? (Y/N): ").lower()
    while user_input not in  ['y','n']:
        user_input = str(input("Invalid Respons. Please enter Y or N: \n"))
    if user_input == 'n':
        break
    board = np.zeros((6, 7))
    game_on = True
    player = 1
    pieces_in_board = 0