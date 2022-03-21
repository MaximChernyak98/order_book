import pytest


@pytest.fixture(scope="session")
def ip_manual(request):
    return request.config.getoption('--ip_manual')