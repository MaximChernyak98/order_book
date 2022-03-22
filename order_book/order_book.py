import re
from xmlrpc.client import Boolean
from db_utils.models import MainTable
from order_book.order import Order
from typing import List
from db_utils.db import db_session
from utils.db_utils import add_list_of_order_to_db, delete_all_row_from_db, delete_row_from_db_by_key, get_all_rows_from_db_by_key, get_unique_row_from_db_by_key, update_row_from_db_by_key
from sqlalchemy.orm.decl_api import DeclarativeMeta


class OrderBook():

    @staticmethod
    def add_list_of_orders(order_list: List[Order]) -> None:
        if type(order_list) is not list:
            order_list = [order_list]
        add_list_of_order_to_db(db_table_model=MainTable, order_list=order_list)

    @staticmethod
    def delete_order_by_id(order_id: int) -> None:
        delete_row_from_db_by_key(db_table_model=MainTable, key_name='id', value=order_id)

    @staticmethod
    def delete_all_order() -> None:
        delete_all_row_from_db(db_table_model=MainTable)

    @staticmethod
    def get_order_info_by_id(order_id: int) -> Order:
        row = get_unique_row_from_db_by_key(db_table_model=MainTable, key_name='id', value=order_id)
        return Order(order_id=row.id, order_type=row.type, price=row.price, volume=row.volume)

    @staticmethod
    def update_order_price(order_id: int, new_price: int) -> None:
        update_row_from_db_by_key(db_table_model=MainTable,
                                  key_name='id',
                                  value=order_id,
                                  field_to_change='price',
                                  field_new_value=new_price)

    @staticmethod
    def update_order_volume(order_id: int, new_volume: int) -> None:
        update_row_from_db_by_key(db_table_model=MainTable,
                                  key_name='id',
                                  value=order_id,
                                  field_to_change='volume',
                                  field_new_value=new_volume)

    @staticmethod
    def get_all_orders_by_type(orders_type: str) -> List[MainTable]:
        return get_all_rows_from_db_by_key(db_table_model=MainTable, key_name='type', value=orders_type)

    @staticmethod
    def sort_list_of_orders_for_order_book(db_rows: List[MainTable], bid_or_ask='bid') -> list:
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
                    'price': sorted_orders[index].price,
                    'volume': result_volume
                }
                result_list.append(order_book_row)
        else:
            print(f'Order book for {bid_or_ask} is empty')

        return result_list

    @staticmethod
    def get_order_book_snapshot() -> dict:
        ask_orders_list = OrderBook.get_all_orders_by_type(orders_type='ask')
        bid_orders_list = OrderBook.get_all_orders_by_type(orders_type='bid')
        asks_order_book_list = OrderBook.sort_list_of_orders_for_order_book(db_rows=ask_orders_list, bid_or_ask='ask')
        bids_order_book_list = OrderBook.sort_list_of_orders_for_order_book(db_rows=bid_orders_list, bid_or_ask='bid')
        result_dict = {}
        result_dict['Asks'] = asks_order_book_list
        result_dict['Bids'] = bids_order_book_list
        return result_dict
