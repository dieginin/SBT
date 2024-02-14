from sqlalchemy import Column, Integer, String

from .database import Base, Database


class _LocModel(Base):
    __tablename__ = "location"

    lid = Column(Integer, primary_key=True, default=1)
    name = Column(String)

    def __init__(self, name: str):
        self.name = name

    _repr_str = lambda self: self.name  # type: ignore

    def __str__(self) -> str:
        return self._repr_str()

    def __repr__(self) -> str:
        return self._repr_str()


class Location(Database):
    @property
    def name(self) -> _LocModel:
        return self._session.query(_LocModel).first()

    def set(self, name: str):
        if not self.name:
            self._session.add(_LocModel(name))
        else:
            pm = self._session.query(_LocModel).filter(_LocModel.lid == 1).one()
            pm.name = name
        self._session.commit()
