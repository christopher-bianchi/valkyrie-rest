# coding:utf-8
import factory
# import pytest

from app.controller import add_squad, get_squad_by_name
from app.model import Squad


# class HeroFactory(factory.alchemy.SQLAlchemyModelFactory):
class SquadFactory(factory.Factory):
    label = 'Arena'

    class Meta:
        model = Squad
        # sqlalchemy_session = db_session


class TestSquad(object):
    def test_add_squad(self, db_session):
        """
        Add a squad.
        """
        squad = SquadFactory.build()
        add_squad(db_session, squad)
        result = get_squad_by_name(db_session, squad.name)
        # TODO: Need to revisit this and maybe close session for these tests
        # specifically so the original hero objects aren't updated by the ORM
        # session.

        self._assert_squad(result, squad)

    def test_add_hero_to_squad(self, db_session):
        """
        Add a hero to an existing squad.
        """
        squad = SquadFactory.create()
        add_squad(db_session, squad)
        result = get_squad_by_name(db_session, squad.name)
        # TODO: Need to revisit this and maybe close session for these tests
        # specifically so the original hero objects aren't updated by the ORM
        # session.

        self._assert_squad(result, squad)

    def _assert_squad(self, actual, expected):
        assert actual.id
        assert actual.label == expected.label
        assert actual.heroes == []
