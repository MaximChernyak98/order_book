from sqlalchemy import Column, Integer, String
from db_utils.db import Base


class MainTable(Base):
    __tablename__ = 'main'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    price = Column(Integer)
    volume = Column(Integer)

    def __repr__(self):
        return f'Table {self.__tablename__} - id={self.id}'
