import allure
from db_utils.db import db_session
from sqlalchemy.orm.exc import MultipleResultsFound


class RowInDBNotFoundError(Exception):
    pass


def get_unique_row_from_db_by_key(db_table_model, key_name, value):
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


def delete_row_from_db_by_key(db_table_model, key_name, value):
    table_name = db_table_model.__tablename__
    with allure.step(f'Deleting row from DB {table_name} by key ---  {key_name}={value}'):
        try:
            with db_session() as session:
                session.query(db_table_model).filter(getattr(db_table_model, key_name) == value).delete()
                session.commit()
        except AttributeError as error:
            assert False, f'In DB table {db_table_model} not found key {key_name}'
