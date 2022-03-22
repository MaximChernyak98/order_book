import pytest

pytest_plugins = ['fixtures.api_request', 'fixtures.parser', 'fixtures.setups_teardowns']


def pytest_addoption(parser):
    parser.addoption(
        '--ip_manual',
        action='store',
        default='www.111.ru')
