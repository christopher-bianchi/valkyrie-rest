# coding:utf-8
from app.model import Item
from app.schema import ItemSchema


class TestItemSchema(object):
    def test_add_new_item_as_dict(self):
        """
        Test schema loads python dictionary properly.
        """
        item_dict = dict(
            name="Hellfire Staff",
            classification="weapon",
            level=40,
            skill_level=4
        )
        result = ItemSchema().load(item_dict)
        self._assert_schema(result, item_dict)

    def test_add_new_item_as_json(self, create_and_load_schema_as_json):
        """
        Test schema loads JSON properly.
        """
        item_dict = dict(
            name="Hellfire Staff",
            classification="weapon",
            level=40,
            skill_level=4
        )
        result = create_and_load_schema_as_json(ItemSchema, item_dict)
        self._assert_schema(result, item_dict)

    def _assert_schema(self, result, expected):
        assert result.errors == {}
        actual = result.data

        assert not actual.id
        assert actual.name == expected['name']
        assert actual.classification == expected['classification']
        assert actual.level == expected['level']
        assert actual.skill_level == expected['skill_level']
        assert actual.gear == []
