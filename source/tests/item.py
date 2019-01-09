# coding:utf-8
import factory
# import pytest

from app.controller import add_item, get_item_by_name
from app.model import Item


# class HeroFactory(factory.alchemy.SQLAlchemyModelFactory):
class ItemFactory(factory.Factory):
    name = factory.Faker('name')
    classification = 'weapon'
    level = 75 #factory.Faker('level')
    skill_level = 4

    class Meta:
        model = Item
        # sqlalchemy_session = db_session


class TestItem(object):
    def test_add_item(self, db_session):
        """
        Add an item.
        """
        item = ItemFactory.build()
        add_item(db_session, item)
        result = get_item_by_name(db_session, item.name)
        # TODO: Need to revisit this and maybe close session for these tests
        # specifically so the original hero objects aren't updated by the ORM
        # session.

        self._assert_item(result, item)

    def _assert_item(self, actual, expected):
        assert actual.id
        assert actual.name == expected.name
        assert actual.classification == expected.classification
        assert actual.level == expected.level
        assert actual.skill_level == expected.skill_level
