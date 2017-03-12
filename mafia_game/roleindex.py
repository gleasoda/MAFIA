from .role import Role

class RoleIndex:
    """
    A class object which holds a copy of each Role.
    """

    def __init__(self):
        """
        RoleIndex initialization.
        """
        self.list = []

    # def __str__(self):
        # return "[%s] %s {%s, %s}" % (self.role_id, self.role_name,\
        # self.role_allegiance, self.role_verdict)


# role0  = Role("townie"  , "town" , "innocent");
# role1  = Role("mafioso" , "mafia", "guilty"  );

master_role_index = RoleIndex()
# master_role_index.list.extend((role0, role1))
for i in range(len(master_role_index.list)):
    master_role_index.list[i].role_id = i