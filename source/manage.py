#!/usr/bin/env python
# coding:utf-8
from app.model import Base
from app.flask_app import engine


def create_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    # drop_db()
    create_db()
