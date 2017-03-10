class Player:
    """
    A class object which holds player information.
    """

    def __init__(self, p_id, p_name):
        """
        Player initialization.
        """
        self.player_id = p_id
        self.player_name = p_name
        self.role = None
        self.subrole_list = None

    def __str__(self):
        # return "[%s] %s {%s}" % (self.player_id, self.player_name, self.role)
        return "[%s] %s" % (self.player_id, self.player_name)