from globalVar import *

def saveResults():
    if player == 0:
        print("It's a tie!")
    else:
        print("Player " + str(player) + " Wins!")
        text_file_message = "Winner: Player " + str(player)
    user_input = input("Would you like to save the results? (Y/N)\n").lower()
    while str(user_input) not in ['y', 'n']:
        user_input = input("Invalid Respons. Please enter Y or N\n")
    if user_input == 'y':
        player_one_name = str(input("Enter Player 1's Name: "))
        player_two_name = str(input("Enter Player 2's Name: "))
        f = open('Match Results.txt', 'a+')
        contents = f.readlines()
        open("Match Results.txt", "w").close()
        f = open('Match Results.txt', 'a')
        if player == 0:
            text_file_message = '\n{} Tie Game Between {} and {}'. \
                format(str(datetime.datetime.now())[:16], player_one_name, player_two_name)
        elif player == 1:
            text_file_message = '\n{} {} | Loser: {}'. \
                format(str(datetime.datetime.now())[:16],
                       text_file_message.replace("Player 1", "{}".format(player_one_name)), player_two_name)
        else:
            text_file_message = '\n{} {} | Loser: {}'. \
                format(str(datetime.datetime.now())[:16],
                       text_file_message.replace("Player 2", "{}".format(player_two_name)), player_one_name)
        contents.insert(0, text_file_message)
        f.writelines(contents)
        f.close()