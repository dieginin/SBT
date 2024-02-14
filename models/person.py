import uuid

from sqlalchemy import Column, String

from databases import Base


class Person(Base):
    __tablename__ = "staff"

    uid = Column(String, primary_key=True, default=uuid.uuid4().hex)
    name = Column(String)
    initials = Column(String, unique=True)
    color = Column(String)

    def __init__(self, name: str, initials: str, color: str):
        self.name = name
        self.initials = initials
        self.color = color

    def _repr_str(self) -> str:
        split_name = self.name.split()
        if len(split_name) > 1:
            return f"{split_name[0]} {split_name[1][0]}"
        else:
            return self.name  # type: ignore

    def __str__(self) -> str:
        return self._repr_str()

    def __repr__(self) -> str:
        return self._repr_str()

    @staticmethod
    def generate_initials(name: str) -> str:
        split_name = name.split()
        return (
            "".join(word[0] for word in split_name)
            if len(split_name) >= 2
            else split_name[0][:2].upper()
        )
