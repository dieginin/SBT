from typing import List

from models import Person

from .database import Database


class Staff(Database):
    @property
    def members(self) -> List[Person]:
        return self._session.query(Person).all()

    def add(self, person: Person):
        self._session.add(person)
        self._session.commit()

    def edit(self, person: Person):
        pm = self._session.query(Person).filter(Person.uid == person.uid).one()
        pm.name = person.name
        pm.initials = person.initials
        pm.color = person.color
        self._session.commit()

    def remove(self, person: Person):
        self._session.delete(person)
        self._session.commit()
