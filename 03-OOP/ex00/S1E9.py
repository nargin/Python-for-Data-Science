from abc import ABC, abstractmethod


class Character(ABC):
    """Character class name: str, is_alive: bool"""
    name = ""
    is_alive = True

    def die(self):
        """Die method"""
        pass

    @abstractmethod
    def __init__(self, name, alive=True):
        """Character init"""
        self.name = name
        self.is_alive = alive


class Stark(Character):
    """Stark: Docstring au top :D"""

    def __init__(self, name, alive=True):
        """Stark: init"""
        super().__init__(name, alive)

    def die(self):
        """Stark: set alive to False"""
        self.is_alive = False
