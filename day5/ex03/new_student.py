import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate a random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student with automatically \
generated login and unique ID."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}"
        self.id = generate_id()
