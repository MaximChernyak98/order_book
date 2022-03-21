
from order_book.order import Order
from order_book.order_book import OrderBook


c = [
    Order(order_type='bid', price=37, volume=1),
    Order(order_type='bid', price=37, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=38, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='bid', price=39, volume=1),
    Order(order_type='ask', price=40, volume=1),
    Order(order_type='ask', price=40, volume=1),
    Order(order_type='ask', price=40, volume=1),
    Order(order_type='ask', price=41, volume=1),
    Order(order_type='ask', price=42, volume=1),
    Order(order_type='ask', price=43, volume=1),
    Order(order_type='ask', price=44, volume=1),
    Order(order_type='ask', price=45, volume=1),
]


b = OrderBook()
b.add_list_of_orders(order_list=c)
b.get_order_book_snapshot()
