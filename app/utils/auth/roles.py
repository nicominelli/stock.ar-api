import enum


class Roles(enum.Enum):
    ADMIN = ('admin', 1)
    USER = ('user', 2)

    def __init__(self, role, weight):
        self.role = role
        self.weight = weight

    @classmethod
    def get_from_name(cls, name: str):
        try:
            return next(x for x in cls if x.role == name)
        except Exception:
            return None
