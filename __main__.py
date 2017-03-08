import player

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

    player_list = []
    while (True):
        player_name = input("Enter player name (leave blank to complete player entry):")
        print("\n%s" % player_name);
        if player_name == "": # entry: empty string
            break;
        new_player = Player(len(player_list)+1, player_name)
        player_list.append(new_player)

    if len(player_list) > 0:
        print("Number of players: %d" % len(player_list))

    for player in player_list:
        print(player)

    return 0

if __name__ == "__main__":
    sys.exit(main())
