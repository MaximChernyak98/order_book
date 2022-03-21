
from order_book.order import Order
from order_book.order_book import OrderBook


a = Order(order_type='bid', price=123, volume=1)
c = [Order(order_type='ask', price=123, volume=1),
     Order(order_type='bid', price=23, volume=2)]


# b = OrderBook()
# b.add_list_of_orders(order_list=a)
# b.add_list_of_orders(order_list=c)
b = OrderBook()
print(b.update_order_volume(order_id=1, new_volume=22222))
