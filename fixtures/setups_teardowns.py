from xmlrpc.client import Boolean
import allure
import pytest
from order_book.order import Order

from order_book.order_book import OrderBook
from test_data.typical_order_book import typical_order_book, positive_order


@pytest.fixture(scope='function', autouse=True)
def clear_order_book(request) -> Boolean:
    with allure.step('Clear order book before test'):
        OrderBook.delete_all_order()
    yield True
    with allure.step('Clear order book after test'):
        OrderBook.delete_all_order()


@pytest.fixture(scope='function', autouse=False)
def add_typical_order(request) -> Order:
    with allure.step('Add typical order'):
        OrderBook.add_list_of_orders(order_list=positive_order[0])
        return positive_order[0]


@pytest.fixture(scope='function', autouse=False)
def add_multiple_orders(request):
    with allure.step(f'Add multiple orders {positive_order} to DB'):
        OrderBook.add_list_of_orders(order_list=positive_order)


@pytest.fixture(scope='function', autouse=False)
def add_typical_orders_list(request):
    with allure.step('Add typical order book with orders'):
        OrderBook.add_list_of_orders(order_list=typical_order_book)
