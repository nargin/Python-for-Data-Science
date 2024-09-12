import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15 character long string."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Class representing a student."""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Generates a login based on the name and surname"""
        self.login = self.name[0].lower() + self.surname.lower()
