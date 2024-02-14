from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Database:
    def __init__(self):
        self._engine = create_engine("sqlite:///sbt.sqlite3", echo=True)
        Base.metadata.create_all(self._engine)

        Session = sessionmaker(self._engine)
        self._session = Session()
