from db import db_session
from models import BidTable

first_bid = BidTable(type='1', price=1, volume=1)
db_session.add(first_bid)
db_session.commit()
