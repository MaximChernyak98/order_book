from typing import Union, List
from db_utils.models import MainTable
from sqlalchemy.orm.decl_api import DeclarativeMeta
from db_utils.db import db_session
import allure


def check_value_in_db_row(row_in_db: MainTable, key_name: str, value: Union[str, int]) -> None:
    with allure.step(f'Check field in DB ---  {key_name}={value}'):
        try:
            actual_value = getattr(row_in_db, key_name)
        except AttributeError:
            assert False, f'In row {row_in_db} not found key {key_name}'
        assert actual_value == value, \
            f'Do not match value in DB {row_in_db} by key {key_name}\n'\
            f'Expected value - {value} / Actual value - {actual_value}'


def check_field_in_db_row_not_none(row_in_db: MainTable, key_name: str) -> None:
    with allure.step(f'Check field {key_name} in DB is not None'):
        try:
            actual_value = getattr(row_in_db, key_name)
        except AttributeError:
            assert False, f'In row {row_in_db} not found key {key_name}'
        assert actual_value != None, \
            f'Value in DB {row_in_db} by key {key_name} is None (expected not None)'


def check_db_is_empty(db_table_model: DeclarativeMeta) -> None:
    with allure.step(f'Check DB is empty'):
        with db_session() as session:
            rows = session.query(db_table_model).all()

            assert rows == [], f'DB is not empty (expected empty DB)'
