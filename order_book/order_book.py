from db_utils.models import MainTable
from order_book.order import Order
from typing import List
from db_utils.db import db_session
from utils.db_utils import add_list_of_order_to_db, delete_row_from_db_by_key, get_unique_row_from_db_by_key, update_row_from_db_by_key


class OrderBook():
    def __init__(self):
        pass

    def add_list_of_orders(self, order_list: List[Order]) -> None:
        if type(order_list) is not list:
            order_list = [order_list]
        add_list_of_order_to_db(db_table_model=MainTable, order_list=order_list)

    def delete_order_by_id(self, order_id: int) -> None:
        delete_row_from_db_by_key(db_table_model=MainTable, key_name='id', value=order_id)

    def get_order_info_by_id(self, order_id: int) -> Order:
        row = get_unique_row_from_db_by_key(db_table_model=MainTable, key_name='id', value=order_id)
        return Order(order_id=row.id, order_type=row.type, price=row.price, volume=row.volume)

    def update_order_price(self, order_id: int, new_price: int) -> None:
        update_row_from_db_by_key(db_table_model=MainTable,
                                  key_name='id',
                                  value=order_id,
                                  field_to_change='price',
                                  field_new_value=new_price)

    def update_order_volume(self, order_id: int, new_volume: int) -> None:
        update_row_from_db_by_key(db_table_model=MainTable,
                                  key_name='id',
                                  value=order_id,
                                  field_to_change='volume',
                                  field_new_value=new_volume)
