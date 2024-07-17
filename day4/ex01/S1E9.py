from abc import ABC, abstractmethod
class Character(ABC):
    """main class, abstracted class"""
    def __init__(self, first_name, is_alive=True):
        """Setting the first name that the user is giving and is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass

        
class Stark(Character):
    """Class Stark who inerite from Character """
    def die(self):
        """Set is_alive to false"""
        self.is_alive = False