# coding:utf-8
from app.model import Hero
from app.schema import HeroSchema


class TestHeroSchema(object):
    def test_add_hero_as_dict(self):
        """
        Test schema loads python dictionary properly.
        """
        hero_dict = dict(
            name="Test Hero",
            level=50
        )
        result = HeroSchema().load(hero_dict)
        self._assert_schema(result, hero_dict)

    def test_add_hero_as_json(self, create_and_load_schema_as_json):
        """
        Test schema loads JSON properly.
        """
        hero_dict = dict(
            name="Test Hero",
            level=50
        )
        result = create_and_load_schema_as_json(HeroSchema, hero_dict)
        self._assert_schema(result, hero_dict)

    def _assert_schema(self, result, expected):
        assert result.errors == {}
        actual = result.data

        assert not actual.id
        assert actual.name == expected['name']
        assert actual.level == expected['level']
        assert actual.gear == []
        assert actual.squads == []
