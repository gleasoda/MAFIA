class Role:
    """
    A class object which holds role information.
    """

    def __init__(self, r_name, r_allegiance, r_verdict):
        """
        Role initialization.
        """
        self.role_id = 0
        self.role_name = r_name
        self.role_allegiance = r_allegiance
        self.role_verdict = r_verdict

    def __str__(self):
        return "[%s] %s {%s, %s}" % (self.role_id, self.role_name,\
        self.role_allegiance, self.role_verdict)