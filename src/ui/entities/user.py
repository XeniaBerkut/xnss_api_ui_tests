from dataclasses import dataclass


@dataclass
class User:
    country: str
    email: str
    password: str = None
