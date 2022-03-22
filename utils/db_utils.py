from order_book.order import Order
import allure
from db_utils.db import db_session
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import Union, List

from db_utils.models import MainTable


class RowInDBNotFoundError(Exception):
    pass


def add_list_of_order_to_db(db_table_model: DeclarativeMeta, order_list: List[Order]):
    table_name = db_table_model.__tablename__
    with allure.step(f'Add order {order_list} to DB {table_name}'):
        with db_session() as session:
            for order in order_list:
                first_bid = MainTable(type=order.order_type,
                                      price=order.price,
                                      volume=order.volume)
                session.add(first_bid)
            session.commit()


def get_unique_row_from_db_by_key(db_table_model: DeclarativeMeta, key_name: str, value: Union[str, int]) -> MainTable:
    table_name = db_table_model.__tablename__
    with allure.step(f'Getting data from DB {table_name} by key ---  {key_name}={value}'):
        try:
            with db_session() as session:
                unique_row = session.query(db_table_model).filter(
                    getattr(db_table_model, key_name) == value).one_or_none()
                if unique_row:
                    return unique_row
                else:
                    raise RowInDBNotFoundError(f'Data not found in table {table_name} '
                                               f'by key {key_name} and value {value}')
        except MultipleResultsFound:
            assert False, f'There are more then one row in table {table_name} by key {key_name} and value {value}'
        except AttributeError as error:
            assert False, f'In DB-table {db_table_model} not found key {key_name}'


def get_all_rows_from_db(db_table_model: DeclarativeMeta) -> MainTable:
    table_name = db_table_model.__tablename__
    with allure.step(f'Getting all data from DB {table_name}'):
        with db_session() as session:
            return session.query(db_table_model).all()


def update_row_from_db_by_key(db_table_model: DeclarativeMeta,
                              key_name: str,
                              value: int,
                              field_to_change: str,
                              field_new_value: int) -> None:
    table_name = db_table_model.__tablename__
    with allure.step(f'Updating row from DB {table_name} by key --- {key_name}={value}, '
                     f'in field {field_to_change}={field_new_value}'):
        try:
            key_field = getattr(db_table_model, key_name)
            field = getattr(db_table_model, field_to_change)

            with db_session() as session:
                session.query(db_table_model).filter(key_field == value).update({field: field_new_value})
                session.commit()
        except MultipleResultsFound:
            assert False, f'There are more then one row in table {table_name} by key {key_name} and value {value}'
        except AttributeError as error:
            assert False, f'In DB-table {db_table_model} not found key {key_name}'


def delete_row_from_db_by_key(db_table_model: DeclarativeMeta, key_name: str, value: Union[str, int]) -> None:
    table_name = db_table_model.__tablename__
    with allure.step(f'Deleting row from DB {table_name} by key ---  {key_name}={value}'):
        try:
            with db_session() as session:
                session.query(db_table_model).filter(getattr(db_table_model, key_name) == value).delete()
                session.commit()
        except AttributeError as error:
            assert False, f'In DB table {db_table_model} not found key {key_name}'


def delete_all_row_from_db(db_table_model: DeclarativeMeta) -> None:
    table_name = db_table_model.__tablename__
    with allure.step(f'Deleting all row from DB {table_name}'):
        with db_session() as session:
            session.query(db_table_model).delete()
            session.commit()


def get_all_rows_from_db_by_key(db_table_model: DeclarativeMeta, key_name: str, value: Union[str, int]) -> MainTable:
    table_name = db_table_model.__tablename__
    with allure.step(f'Getting all rows from DB {table_name} by key ---  {key_name}={value}'):
        try:
            with db_session() as session:
                rows = session.query(db_table_model).filter(
                    getattr(db_table_model, key_name) == value).all()
                return rows
        except AttributeError as error:
            assert False, f'In DB-table {db_table_model} not found key {key_name}'
