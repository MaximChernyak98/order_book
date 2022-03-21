from db_utils.models import MainTable
from order_book.order import Order
from typing import List
from db_utils.db import db_session
from utils.db_utils import delete_row_from_db_by_key


class OrderBook():
    def __init__(self):
        pass

    def add_list_of_orders(self, order_list: List[Order]) -> None:
        if type(order_list) is not list:
            order_list = [order_list]

        with db_session() as session:
            for order in order_list:
                first_bid = MainTable(type=order.order_type,
                                      price=order.price,
                                      volume=order.volume)
                session.add(first_bid)
            session.commit()

    def delete_order_by_id(self, order_id: int) -> None:
        delete_row_from_db_by_key(db_table_model=MainTable, key_name='id', value=order_id)
