from mafia_game import Player
from mafia_game import Role

import random
import sys

def main(argv = None):
    """
    The 'main' function for executing MAFIA.
    """
    # # # # # # # # # #
    # Startup and opening messages.
    # # # # # # # # # #
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 0:
        print("WELCOME TO MAFIA; GREET SOMEONE WITH BETRAYAL.")

    else:
        pass


    # # # # # # # # # #
    # Player name entry.
    # # # # # # # # # #
    print("\nEnter player names (leave blank to complete player entry);");
    print("if a name is entered improperly, it may be reenetered later -->");
    
    player_list = []
    while (True):
        player_name = input("[Player %d]: " % (len(player_list)+1))
        if player_name == "": # entry: empty string
            break;
        new_player = Player(len(player_list)+1, player_name)
        player_list.append(new_player)

    if len(player_list) > 0:
        print("\nNumber of players: %d" % len(player_list))

    for player in player_list:
        print(player)
    
    print("\nIf a name is incorrect, enter the player's ID; or, leave blank -->");
    
    while (True):
        entered_id = input("\n[ID#] of player to rename: ")
        if entered_id == "": # entry: empty string
            break;
        elif not entered_id.isdigit():
            print("INVALID INPUT - player ID not found!");
            continue;
            
        entered_id = int(entered_id) -1;
        if (entered_id < 0 or entered_id >= len(player_list)):
            print("INVALID INPUT - player ID not found!");
            continue;
        
        print("Reenter the player's name; or, leave blank -->");
        player_name = input("[Player %d]: " % (entered_id+1))
        if player_name == "": # entry: empty string
            continue;
        player_list[entered_id].player_name = player_name
        
    if len(player_list) > 0:
        print("\nNumber of players: %d" % len(player_list))

    for player in player_list:
        print(player)


    # # # # # # # # # #
    # Game details/options entry.
    # # # # # # # # # #
    num_players = len(player_list)
    num_mafia = num_players//4
    num_townies = num_players - num_mafia
    
    print("\nA game size of %d players warrants %d mafia (%d townies);"\
    % (num_players, num_mafia, num_townies));
    print("leave blank to continue; or, enter the number of mafia -->");
    
    while (True):
        num_mafia = input("# mafia: ")
        if num_mafia == "": # entry: empty string
            break;
        elif not num_mafia.isdigit():
            print("INVALID INPUT - # mafia must be an integer!");
            continue;
        break;
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
