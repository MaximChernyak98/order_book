from db_utils.models import MainTable
from order_book.order import Order
from typing import List
from db_utils.db import db_session


class OrderBook():
    def __init__(self):
        pass

    def add_order(self, order_list: List[Order]) -> None:
        if type(order_list) is not list:
            order_list = [order_list]

        with db_session() as session:
            for order in order_list:
                first_bid = MainTable(type=order.order_type,
                                      price=order.price,
                                      volume=order.volume)
                session.add(first_bid)
            session.commit()
