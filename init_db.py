from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine(f'sqlite:///order_book.db', echo=True)

meta = MetaData()

ask = Table(
    'main', meta,
    Column('id', Integer, primary_key=True),
    Column('type', String),
    Column('price', Integer),
    Column('volume', Integer)
)

if __name__ == "__main__":
    meta.create_all(engine)
