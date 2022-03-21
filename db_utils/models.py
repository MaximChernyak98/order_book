from sqlalchemy import  Column, Integer, String
from db import Base


class BidTable(Base):
    __tablename__ = 'bid'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    price = Column(Integer)
    volume = Column(Integer)

    def __repr__(self):
        return f'Table {self.__tablename__} - id={self.id}'

class AskTable(Base):
    __tablename__ = 'ask'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    price = Column(Integer)
    volume = Column(Integer)

    def __repr__(self):
        return f'Table {self.__tablename__} - id={self.id}'



