
from order_book.order import Order
from order_book.order_book import OrderBook


# a = Order(order_type='bid', price=123, volume=1)
# c = [Order(order_type='ask', price=123, volume=1),
#      Order(order_type='bid', price=23, volume=2)]


# b = OrderBook()
# b.add_order(order_list=a)
# b.add_order(order_list=c)
b = OrderBook()
b.delete_order_by_id(order_id=5)
