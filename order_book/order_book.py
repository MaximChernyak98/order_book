import re
from xmlrpc.client import Boolean
from db_utils.models import MainTable
from order_book.order import Order
from typing import List
from db_utils.db import db_session
from utils.db_utils import add_list_of_order_to_db, delete_row_from_db_by_key, get_all_rows_from_db_by_key, get_unique_row_from_db_by_key, update_row_from_db_by_key
from sqlalchemy.orm.decl_api import DeclarativeMeta


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

    def get_all_orders_by_type(self, orders_type: str) -> List[MainTable]:
        return get_all_rows_from_db_by_key(db_table_model=MainTable, key_name='type', value=orders_type)

    def sort_list_of_orders_for_order_book(self, db_rows: List[MainTable], bid_or_ask='bid') -> list:
        sorted_orders = sorted(db_rows, key=lambda x: x.price, reverse=True)
        result_list = []
        index = 0

        if sorted_orders:
            result_volume = sorted_orders[0].volume
            try:
                while index < len(sorted_orders):
                    if sorted_orders[index].price == sorted_orders[index+1].price:
                        result_volume += sorted_orders[index+1].volume
                    else:
                        order_book_row = {
                            'price': sorted_orders[index].price,
                            'volume': result_volume
                        }
                        result_list.append(order_book_row)

                        result_volume = sorted_orders[index+1].volume
                    index += 1
            except IndexError:
                order_book_row = {
                    'price': sorted_orders[index-1].price,
                    'volume': result_volume
                }
                result_list.append(order_book_row)
        else:
            print(f'Order book for {bid_or_ask} is empty')

        return result_list

    def get_order_book_snapshot(self) -> dict:
        ask_orders_list = self.get_all_orders_by_type(orders_type='ask')
        bid_orders_list = self.get_all_orders_by_type(orders_type='bid')
        print(self.sort_list_of_orders_for_order_book(db_rows=ask_orders_list, bid_or_ask='ask'))
        print('\n')
        print(self.sort_list_of_orders_for_order_book(db_rows=bid_orders_list, bid_or_ask='bid'))
