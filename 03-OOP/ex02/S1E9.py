from abc import ABC, abstractmethod


class Character(ABC):
    """Character class name: str, is_alive: bool"""
    first_name = "Character"
    is_alive = True

    @abstractmethod
    def __init__(self, name, alive=True):
        """Character: init"""
        self.first_name = name
        self.is_alive = alive

    def die(self):
        """Die method"""
        pass
