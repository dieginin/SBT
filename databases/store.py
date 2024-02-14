from datetime import date

from models import Turn

from .database import Database


class Store(Database):
    @property
    def turn(self) -> Turn:
        return self._session.query(Turn).filter(Turn.date == date.today()).first()

    def start(self, turn: Turn):
        self._session.add(turn)
        self._session.commit()

    def modify(self, turn: Turn):
        dm = self.turn
        dm.time_open = turn.time_open
        dm.time_close = turn.time_close
        dm.who_open = turn.who_open
        dm.who_close = turn.who_close
        dm.gc50 = turn.gc50
        dm.gc25 = turn.gc25
        dm.ltmns = turn.ltmns
        dm.bl100 = turn.bl100
        dm.bl50 = turn.bl50
        dm.bl20 = turn.bl20
        dm.bl10 = turn.bl10
        dm.bl05 = turn.bl05
        dm.bl02 = turn.bl02
        dm.bl01 = turn.bl01
        dm.ct25 = turn.ct25
        dm.ct10 = turn.ct10
        dm.ct05 = turn.ct05
        dm.ct01 = turn.ct01
        self._session.commit()

    def finish(self, turn: Turn):
        dm = self.turn
        dm.gc50 = turn.gc50
        dm.gc25 = turn.gc25
        dm.ltmns = turn.ltmns
        dm.bl100 = turn.bl100
        dm.bl50 = turn.bl50
        dm.bl20 = turn.bl20
        dm.bl10 = turn.bl10
        dm.bl05 = turn.bl05
        dm.bl02 = turn.bl02
        dm.bl01 = turn.bl01
        dm.ct25 = turn.ct25
        dm.ct10 = turn.ct10
        dm.ct05 = turn.ct05
        dm.ct01 = turn.ct01
        dm.cash_sales = turn.cash_sales
        dm.card_sales = turn.card_sales
        dm.gift_sales = turn.gift_sales
        dm.returns = turn.returns
        dm.sold = turn.sold
        self._session.commit()
