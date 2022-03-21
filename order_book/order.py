from dataclasses import dataclass


@dataclass
class Order:
    order_id: int = 0
    order_type: str = 'bid'
    price: int = 0
    volume: int = 0

    def __repr__(self):
        return f'Order with id={self.order_id}, type={self.order_type}, price={self.price}, volume={self.volume}'
