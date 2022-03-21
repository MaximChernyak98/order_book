import pytest


pytest.fixture(scope='function', autouse=True)
def api_request(request):
    class Dummy():
        def __init__(self) -> None:
            self.headers = {
                "Content-Type": "application/json",
            }

    res = Dummy()
    yield res
