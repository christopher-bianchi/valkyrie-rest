# coding:utf-8
import pytest

from sqlalchemy.orm import sessionmaker

from app.main import engine


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope='function')
def db_session(connection):
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
