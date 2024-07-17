from S1E7 import Baratheon, Lannister
class King(Baratheon, Lannister):
    """hybrid class from baratheon and lannister"""
    def set_eyes(self, color: str):
        """set the eyes color"""
        self.eyes = color


    def set_hairs(self, color: str):
        """set the hair's color"""
        self.hairs = color


    def get_eyes(self):
        """return the eyes's color"""
        return self.eyes


    def get_hairs(self):
        """return the hair's color"""
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)