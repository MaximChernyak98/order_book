from order_book.order import Order


positive_order = [
    Order(order_type='bid', price=33, volume=1),
    Order(order_type='ask', price=33, volume=1),
]


typical_order_book = [
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
