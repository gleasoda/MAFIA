from .role import Role

class RoleIndex:
    """
    A class object which holds a copy of each Role.
    """

    def __init__(self):
        """
        RoleIndex initialization.
        """
        self.list = [None]

    # def __str__(self):
        # return "[%s] %s {%s, %s}" % (self.role_id, self.role_name,\
        # self.role_allegiance, self.role_verdict)


role0  = Role( 0, "townie"  , "town" , "innocent");
role1  = Role( 1, "mafioso" , "mafia", "guilty"  );

master_role_index = RoleIndex()
master_role_index.list.append([role0, role1])