# coding:utf-8
from app.model import Gear
from app.schema import GearSchema


class TestGearSchema(object):
    def test_add_new_gear_as_dict(self):
        """
        Test schema loads python dictionary properly.
        """
        gear_dict = dict(label="New Gear")
        result = GearSchema().load(gear_dict)
        self._assert_schema(result, gear_dict)

    def test_add_new_gear_as_json(self, create_and_load_schema_as_json):
        """
        Test schema loads JSON properly.
        """
        gear_dict = dict(label="New Gear")
        result = create_and_load_schema_as_json(GearSchema, gear_dict)
        self._assert_schema(result, gear_dict)

    def _assert_schema(self, result, expected):
        assert result.errors == {}
        actual = result.data

        assert not actual.id
        assert actual.label == expected['label']
        assert actual.items == []

    # def test_load_one_gear_items_empty(self):
    #     schema = GearSchema()

    #     gear_dict = dict(
    #         id=1,
    #         label="New Gear",
    #         items=[]
    #     )
    #     gear_one = Gear(**gear_dict)

    #     result = schema.dump(gear_one)

    #     self.assertDictEqual(result.errors, {})
    #     gear = result.data

    #     self.assertEquals(gear['id'], gear_one.id)
    #     self.assertEquals(gear['label'], gear_one.label)
    #     self.assertListEqual(gear['items'], gear_one.items)

    # def test_load_many_gear_items_empty(self):
    #     schema = GearSchema(many=True)

    #     gear_dict = dict(
    #         id=1,
    #         label="New Gear",
    #         items=[]
    #     )
    #     gear_dict2 = dict(
    #         id=2,
    #         label="New Gear2",
    #         items=[]
    #     )
    #     gear_one = Gear(**gear_dict)
    #     gear_two = Gear(**gear_dict2)

    #     result = schema.dump([gear_one, gear_two])

    #     self.assertDictEqual(result.errors, {})
    #     gear = result.data

    #     self.assertEquals(gear[0]['id'], gear_one.id)
    #     self.assertEquals(gear[0]['label'], gear_one.label)
    #     self.assertListEqual(gear[0]['items'], gear_one.items)

    #     self.assertEquals(gear[1]['id'], gear_two.id)
    #     self.assertEquals(gear[1]['label'], gear_two.label)
    #     self.assertListEqual(gear[1]['items'], gear_two.items)
