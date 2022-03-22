
from pprint import pprint
from order_book.order import Order
from order_book.order_book import OrderBook


c = [
    Order(order_type='bid', price=33, volume=1),
    Order(order_type='bid', price=37, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=40, volume=1),
    Order(order_type='ask', price=41, volume=1),
    Order(order_type='ask', price=42, volume=1),
    Order(order_type='ask', price=42, volume=1),
    Order(order_type='ask', price=42, volume=1),
    Order(order_type='ask', price=42, volume=1),
    Order(order_type='ask', price=43, volume=1),
    Order(order_type='ask', price=44, volume=1),
    Order(order_type='ask', price=45, volume=1),
]

OrderBook.delete_all_order()
OrderBook.add_list_of_orders(order_list=c)
pprint(OrderBook.get_order_book_snapshot())
