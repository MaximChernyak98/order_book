import allure
from pprint import pprint

import pytest
from db_utils.models import MainTable
from order_book.order import Order
from order_book.order_book import OrderBook
from test_data.typical_order_book import positive_order
from utils.db_checks import check_db_is_empty, check_field_in_db_row_not_none, check_value_in_db_row
from utils.db_utils import get_all_rows_from_db, get_unique_row_from_db_by_key
from utils.utils import attach_snapshot_result


class TestPositiveOrderBook:
    @allure.story('Add order')
    @allure.description('Add one order')
    @pytest.mark.parametrize('order', positive_order)
    def test_add_one_order(self, order):
        with allure.step(f'Add {order.order_type} order to DB'):
            OrderBook.add_list_of_orders(order_list=order)

        with allure.step(f'Check order in DB'):
            row = get_unique_row_from_db_by_key(db_table_model=MainTable, key_name='price', value=order.price)

            check_value_in_db_row(row_in_db=row, key_name='volume', value=order.volume)
            check_field_in_db_row_not_none(row_in_db=row, key_name='id')
            check_field_in_db_row_not_none(row_in_db=row, key_name='type')

    @allure.story('Add order')
    @allure.description('Add multiple orders')
    def test_multiple_orders(self, add_multiple_orders):
        with allure.step(f'Check orders in DB'):
            rows = get_all_rows_from_db(db_table_model=MainTable)

            expected_num_rows = len(positive_order)
            actual_num_rows = len(rows)

            assert expected_num_rows == actual_num_rows, \
                f'Mismatch in number rows, expected value - {expected_num_rows} / Actual value - {actual_num_rows}'

    @allure.story('Delete order')
    @allure.description('Delete order by id')
    def test_delete_order_by_id(self, add_typical_order):
        with allure.step(f'Check order in DB'):
            row = get_unique_row_from_db_by_key(
                db_table_model=MainTable, key_name='price', value=add_typical_order.price)
            order_id = row.id

        with allure.step(f'Delete order from DB'):
            OrderBook.delete_order_by_id(order_id=order_id)
            check_db_is_empty(db_table_model=MainTable)

    @allure.story('Get info')
    @allure.description('Check order info')
    def test_get_order_info(self, add_typical_order):
        with allure.step(f'Check order in DB'):
            row = get_unique_row_from_db_by_key(
                db_table_model=MainTable, key_name='price', value=add_typical_order.price)
            order_id = row.id

        with allure.step(f'Get order info'):
            order = OrderBook.get_order_info_by_id(order_id=order_id)
            assert order.order_id == order_id, 'order id do not match'
            assert order.order_type == add_typical_order.order_type, 'order type do not match'
            assert order.price == add_typical_order.price, 'order price do not match'
            assert order.volume == add_typical_order.volume, 'order volume do not match'

    @allure.story('Get order book')
    @allure.description('Check order book')
    def test_order_book(self, add_typical_orders_list):
        with allure.step(f'Get snapshot'):
            snapshot = OrderBook.get_order_book_snapshot()
            attach_snapshot_result(snapshot=snapshot)

            assert len(snapshot['Bids']) != 0, 'Bids section in Order book is empty (expected multiple rows)'
            assert len(snapshot['Asks']) != 0, 'Asks section in Order book is empty (expected multiple rows)'
