class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} where {self.description}."


home = Room("home", "home sweet home")

print("home described in full is " + home)

print(home.description)
