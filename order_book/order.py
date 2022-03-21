from dataclasses import dataclass


@dataclass
class Order:
    order_id: int = 0
    order_type: str = 'bid'
    price: int = 0
    volume: int = 0
