class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name} where {self.description}."

