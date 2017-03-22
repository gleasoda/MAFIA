class Role:
    """
    A class object which holds role information.
    """

    def __str__(self):
        return "[{id}] {name} {{{allegiance}, {verdict}}}".format(
            id=self.role_id,
            name=self.role_name,
            allegiance=self.role_allegiance,
            verdict=self.role_verdict,
            )
            
    def is_innocent(self):
        if self.role_verdict == "Innocent":
            return True
        else:
            return False



role_index = []

class TownieRole(Role):
    role_id = 0
    role_name = "Townie"
    role_allegiance = "Town"
    role_verdict = "Innocent"
role_index.append(TownieRole())
    
class MafiosoRole(Role):
    role_id = 0
    role_name = "Mafioso"
    role_allegiance = "Mafia"
    role_verdict = "Guilty"
role_index.append(MafiosoRole())

class SheriffRole(Role):
    role_id = 0
    role_name = "Sheriff"
    role_allegiance = "Town"
    role_verdict = "Innocent"
role_index.append(SheriffRole())

class NurseRole(Role):
    role_id = 0
    role_name = "Nurse"
    role_allegiance = "Town"
    role_verdict = "Innocent"
role_index.append(NurseRole())

class GodfatherRole(Role):
    role_id = 0
    role_name = "Godfather"
    role_allegiance = "Mafia"
    role_verdict = "Innocent"
role_index.append(GodfatherRole())
 
for ii in range(len(role_index)):
    role_index[ii].role_id = ii
    
    
    
    
    
def town_power_roles():
    # list of all avaiable townie power roles
    role_list = [
        NurseRole(),
        SheriffRole(),
    ]
    return role_list
    
def mafia_power_roles():
    # list of all avaiable mafia power roles
    role_list = [
        GodfatherRole(),
    ]
    return role_list
    
def all_power_roles():
    # list of all avaiable power roles
    role_list = townie_power_roles()
    role_list = role_list + mafia_power_roles()
    return role_list