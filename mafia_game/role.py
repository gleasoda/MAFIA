class Role:
    """
    A class object which holds role information.
    """

    def __init__(self):
        """
        Role initialization.
        """
        # self.role_id = 0
        # self.role_name = "Unspecified"
        # self.role_allegiance = "Unspecified"
        # self.role_verdict = "Unspecified"

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




class TownieRole(Role):
    role_id = 0
    role_name = "Townie"
    role_allegiance = "Town"
    role_verdict = "Innocent"

class SheriffRole(Role):
    role_id = 1
    role_name = "Sheriff"
    role_allegiance = "Town"
    role_verdict = "Innocent"

class MafiosoRole(Role):
    role_id = 2
    role_name = "Mafioso"
    role_allegiance = "Mafia"
    role_verdict = "Guilty"

class GodfatherRole(Role):
    role_id = 3
    role_name = "Godfather"
    role_allegiance = "Mafia"
    role_verdict = "Innocent"