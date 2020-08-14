class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} where {self.description}."


class Sword(Item):
    def __init__(self, name, description, sharp=False):
        super().__init__(name, description)


class GoldTrinket(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value


class Trash(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value


class Armor(Item):
    def __init__(self, name, description, material="cloth"):
        super().__init__(name, description)

