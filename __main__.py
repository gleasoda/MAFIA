from mafia_game import Player
from mafia_game import TownieRole
from mafia_game import SheriffRole
from mafia_game import MafiosoRole
from mafia_game import GodfatherRole
from mafia_game import town_power_roles
from mafia_game import mafia_power_roles
from mafia_game import all_power_roles

import random
from random import shuffle
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
    print("\n\n\n\n\n")
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
    
    print("\nIf a name is incorrect, enter the player's ID; or, leave blank",
        "-->");
    
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
    print("\n\n\n\n\n")
    num_players = len(player_list)
    if num_players < 4:
        print("\nNot enough players to play; 4+ needed, 8+ recommended!")
        return 0
    elif num_players < 8:
        print("\nNote 8+ players recommended!")
    num_mafia = num_players//4
    if num_mafia == 0:
        num_mafia = 1
    num_townies = num_players - num_mafia
    
    print("\nA game size of %d players warrants %d mafia (%d townies);"\
    % (num_players, num_mafia, num_townies));
    print("leave blank to continue; or, enter the number of mafia -->");
    
    while (True):
        entered_num_mafia = input("# mafia: ")
        if entered_num_mafia == "": # entry: empty string
            break;
        elif not num_mafia.isdigit():
            print("INVALID INPUT - # mafia must be an integer!");
            continue;
        num_mafia = entered_num_mafia
        break;
    
    num_townies = num_players - num_mafia

    # # # # # # # # # #
    # Role assignments.
    # # # # # # # # # #
    roles_town = setup_townie_power_roles(num_townies)
    roles_mafia = setup_mafia_power_roles(num_mafia)
    role_list = roles_town + roles_mafia
    shuffle(role_list)
    
    for player, role in zip(player_list, role_list):
        player.player_role = role
    
    print("\n\nPlayer and role assignments:");
    for player in player_list:
        print("%s: %s (%s allegiance, checks as %s)" % (player.player_name,\
        player.player_role.role_name, player.player_role.role_allegiance,\
        player.player_role.role_verdict))

    return 0


    
def setup_townie_power_roles(num_townies):
    import mafia_game.role as roles
    # list of all avaiable power roles
    available_power_roles = town_power_roles()
    print("\n\n\n\n\n")
    print("\nAvailable townie power roles to add:")
    # print current index and role name
    for i, role in enumerate(available_power_roles):
        print("%d: %s" % (i, role.role_name))

    print("\nYou may add up to %d Town power roles;" % (num_townies))
    print("Leave blank to continue; or, enter the role ID of the power",
        "role you wish to add -->");
    
    power_roles_to_add = []
    num_power_roles = 0

    while len(power_roles_to_add) <= num_townies - 1:
        entered_id = input("\n[ID#] of power role to add: ")
        if entered_id == "": # entry: empty string
            break
        try:
            entered_id = int(entered_id)
        except ValueError:
            print("INVALID INPUT - Please enter the ID number!")
            continue

        # if negative number given, 'restart' this function
        if entered_id < 0:
            print("Restarting power-role select")
            return setup_townie_power_roles(num_townies)

        try:
            selected_role = available_power_roles[entered_id]
        except IndexError:
            print("INVALID INPUT - role ID not found!")
            continue
        
        num_power_roles += 1

        power_roles_to_add.append(selected_role)
        # # Popping a role causes the list to shrink and thereby invalidates the
        # # id for a given role entry. Either the role is popped and the list is
        # # reprinted with updated id's, or the list remains unchanged. The latter
        # # is preferred since a user should be able to add multiple power roles
        # # of the same type even if this is unlikely or, in many cases,
        # # undesirable. An additional check should be made that the right number
        # # of each type of role is added and allow the user to reenter roles.
        # available_power_roles.pop(entered_id)
        
    print("\n\nAdding the following power roles to the game:")
    for role in power_roles_to_add:
        print(' ', role.role_name)
    
    role_list = power_roles_to_add
    role_list += [roles.TownieRole()] * (num_townies-num_power_roles)
    return role_list
    
    
    
def setup_mafia_power_roles(num_mafia):
    import mafia_game.role as roles
    # list of all avaiable power roles
    available_power_roles = mafia_power_roles()
    print("\n\n\n\n\n")
    print("\nAvailable Mafia power roles to add:")
    # print current index and role name
    for i, role in enumerate(available_power_roles):
        print("%d: %s" % (i, role.role_name))

    print("\nYou may add up to %d Mafia power roles;" % (num_mafia))
    print("Leave blank to continue; or, enter the role ID of the power",
        "role you wish to add -->");
    
    power_roles_to_add = []
    num_power_roles = 0

    while len(power_roles_to_add) <= num_mafia - 1:
        entered_id = input("\n[ID#] of power role to add: ")
        if entered_id == "": # entry: empty string
            break
        try:
            entered_id = int(entered_id)
        except ValueError:
            print("INVALID INPUT - Please enter the ID number!")
            continue

        # if negative number given, 'restart' this function
        if entered_id < 0:
            print("Restarting power-role select")
            return setup_mafia_power_roles(num_townies)

        try:
            selected_role = available_power_roles[entered_id]
        except IndexError:
            print("INVALID INPUT - role ID not found!")
            continue
        
        num_power_roles += 1

        power_roles_to_add.append(selected_role)
        
    print("\n\nAdding the following power roles to the game:")
    for role in power_roles_to_add:
        print(' ', role.role_name)
    
    role_list = power_roles_to_add
    role_list += [roles.MafiosoRole()] * (num_mafia-num_power_roles)
    return role_list

if __name__ == "__main__":
    sys.exit(main())
