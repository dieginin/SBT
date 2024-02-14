from datetime import datetime, time

from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Time

from databases import Base


def _validate_hour(hour) -> time:
    try:
        hour, minute = map(int, hour.split(":"))
        return time(hour, minute)
    except ValueError:
        return time(0, 0)


class Turn(Base):
    __tablename__ = "store"

    date = Column(Date, primary_key=True, default=datetime.today())
    time_open = Column(Time)
    time_close = Column(Time)
    who_open = Column(String, ForeignKey("staff.initials"))
    who_close = Column(String, ForeignKey("staff.initials"))
    gc50 = Column(Integer)
    gc25 = Column(Integer)
    ltmns = Column(Integer)
    bl100 = Column(Integer)
    bl50 = Column(Integer)
    bl20 = Column(Integer)
    bl10 = Column(Integer)
    bl05 = Column(Integer)
    bl02 = Column(Integer)
    bl01 = Column(Integer)
    ct25 = Column(Integer)
    ct10 = Column(Integer)
    ct05 = Column(Integer)
    ct01 = Column(Integer)
    cash_sales = Column(Integer)
    card_sales = Column(Integer)
    gift_sales = Column(Integer)
    returns = Column(Integer)
    sold = Column(Float)

    def __init__(
        self,
        time_open: str,
        time_close: str,
        who_open: str,
        who_close: str,
        gc50: int,
        gc25: int,
        ltmns: int,
        bl100: int,
        bl50: int,
        bl20: int,
        bl10: int,
        bl05: int,
        bl02: int,
        bl01: int,
        ct25: int,
        ct10: int,
        ct05: int,
        ct01: int,
        cash_sales: int | None = None,
        card_sales: int | None = None,
        gift_sales: int | None = None,
        returns: int | None = None,
        sold: float | None = None,
    ):
        self.time_open = _validate_hour(time_open)
        self.time_close = _validate_hour(time_close)
        self.who_open = who_open
        self.who_close = who_close
        self.gc50 = gc50
        self.gc25 = gc25
        self.ltmns = ltmns
        self.bl100 = bl100
        self.bl50 = bl50
        self.bl20 = bl20
        self.bl10 = bl10
        self.bl05 = bl05
        self.bl02 = bl02
        self.bl01 = bl01
        self.ct25 = ct25
        self.ct10 = ct10
        self.ct05 = ct05
        self.ct01 = ct01
        self.cash_sales = cash_sales
        self.card_sales = card_sales
        self.gift_sales = gift_sales
        self.returns = returns
        self.sold = sold

    def _repr_str(self) -> str:
        sld = self.sold if self.sold else 0.0  # type: ignore
        return f"{self.date} {self.time_open} - {self.time_close} sold: ${sld}"

    def __str__(self) -> str:
        return self._repr_str()

    def __repr__(self) -> str:
        return self._repr_str()
