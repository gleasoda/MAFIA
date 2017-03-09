from mafia_game import Player

import sys

def main(argv = None):
    """
    The 'main' function for executing MAFIA.
    """

    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 0:
        print("WELCOME TO MAFIA; GREET SOMEONE WITH BETRAYAL.")

    else:
        pass
    
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
        
    return 0

if __name__ == "__main__":
    sys.exit(main())
