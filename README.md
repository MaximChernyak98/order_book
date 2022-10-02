# OrderBook 

Interview test - implementation of the Bid/Ask order book and some positive tests for it

### Setup 

1. Clone repository 
2. Create virtual enviroment
3. Install requirements `pip3 install -r requirements.txt`
4. Create DataBase ```python3 init_db.py```

### Run tests
1. run  ```pytest -v -s tests/positive/test_order_book.py --alluredir allure-results```
2. run ```allure serve allure-results```
