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
        self.player_role = None
        self.player_subrole_list = None

    def __str__(self):
        return "[%s] %s" % (self.player_id, self.player_name)