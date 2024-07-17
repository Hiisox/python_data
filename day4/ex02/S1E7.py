from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


    def __str__(self):
        return f"Vector: ('Baratheon', 'brown', 'dark')"


    def __repr__(self):
        return f"Vector: ('Baratheon', 'brown', 'dark')"


    def die(self):
        """Set is_alive to false"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, name, is_alive=True):
        self.first_name = name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"


    def __str__(self):
        return f"Vector: ('Lannister', 'blue', 'light')"


    def __repr__(self):
        return f"Vector: ('Lannister', 'blue', 'light')"


    def die(self):
        """Set is_alive to false"""
        self.is_alive = False


    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """for create a new lannister"""
        return cls(first_name, is_alive)