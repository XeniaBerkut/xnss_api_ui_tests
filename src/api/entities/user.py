import json
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class User:
    login: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None

    def to_json(self):
        user_to_dict = asdict(self)
        return json.dumps(user_to_dict, indent=4)
