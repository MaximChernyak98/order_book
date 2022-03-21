import pytest

pytest_plugins = ['fixtures.api_request', 'fixtures.parser']


def pytest_addoption(parser):
    parser.addoption(
        '--ip_manual',
        action='store',
        default='www.111.ru')
