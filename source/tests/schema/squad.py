# coding:utf-8
from app.model import Squad
from app.schema import SquadSchema


class TestSquadSchema(object):
    def test_add_new_squad_as_dict(self):
        """
        Test schema loads python dictionary properly.
        """
        squad_dict = dict(label="Arena")
        result = SquadSchema().load(squad_dict)
        self._assert_schema(result, squad_dict)

    def test_add_new_squad_as_json(self, create_and_load_schema_as_json):
        """
        Test schema loads JSON properly.
        """
        squad_dict = dict(label="Arena")
        result = create_and_load_schema_as_json(SquadSchema, squad_dict)
        self._assert_schema(result, squad_dict)

    def _assert_schema(self, result, expected):
        assert result.errors == {}
        actual = result.data

        assert not actual.id
        assert actual.label == expected['label']
        assert actual.heroes == []
