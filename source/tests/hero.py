# coding:utf-8
import factory
# import pytest

from app.controller import add_hero, get_hero_by_name
from app.model import Hero


# class HeroFactory(factory.alchemy.SQLAlchemyModelFactory):
class HeroFactory(factory.Factory):
    name = factory.Faker('name')
    level = 75 #factory.Faker('level')

    class Meta:
        model = Hero
        # sqlalchemy_session = db_session


# @pytest.mark.usefixtures('db_session')
class TestHero(object):
    def test_add_hero(self, db_session):
        """
        Add a hero.
        """
        hero = HeroFactory.build()
        add_hero(db_session, hero)
        result = get_hero_by_name(db_session, hero.name)
        # TODO: Need to revisit this and maybe close session for these tests
        # specifically so the original hero objects aren't updated by the ORM
        # session.

        self._assert_hero(result, hero)

    def _assert_hero(self, actual, expected):
        assert actual.id
        assert actual.name == expected.name
        assert actual.level == expected.level
        assert actual.squads == []
