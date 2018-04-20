#!/usr/bin/env python
# coding:utf-8
import json
import unittest2

from model import Gear, Hero
from schema import GearSchema, HeroSchema


class TestHeroSchema(unittest2.TestCase):
    def test_add_hero_json(self):
        hero_dict = dict(
            name="Test Hero",
            level=50
        )
        hero_json = json.dumps(hero_dict)
        result = HeroSchema().loads(hero_json)

        self.assertDictEqual(result.errors, {})
        hero = result.data

        self.assertIsNone(hero.id)
        self.assertEquals(hero.name, hero_dict['name'])
        self.assertEquals(hero.level, hero_dict['level'])
        self.assertListEqual(hero.gear, [])
        self.assertListEqual(hero.squads, [])

    def test_add_hero_dict(self):
        hero_dict = dict(
            name="Test Hero",
            level=50
        )
        result = HeroSchema().load(hero_dict)

        self.assertDictEqual(result.errors, {})
        hero = result.data

        self.assertIsNone(hero.id)
        self.assertEquals(hero.name, hero_dict['name'])
        self.assertEquals(hero.level, hero_dict['level'])
        self.assertListEqual(hero.gear, [])
        self.assertListEqual(hero.squads, [])


class TestGearSchema(unittest2.TestCase):
    def test_add_new_gear_dict(self):
        """
        Test schema loads a python dictionary.
        """
        gear_dict = dict(label="New Gear")
        result = GearSchema().load(gear_dict)

        self.assertDictEqual(result.errors, {})
        gear = result.data

        self.assertIsNone(gear.id)
        self.assertEquals(gear.label, gear_dict['label'])
        self.assertListEqual(gear.items, [])

    def test_add_new_gear_json(self):
        """
        Test schema loads JSON.
        """
        # create json.
        gear_dict = dict(label="New Gear")
        gear_json = json.dumps(gear_dict)
        result = GearSchema().loads(gear_json)

        self.assertDictEqual(result.errors, {})
        gear = result.data

        self.assertIsNone(gear.id)
        self.assertEquals(gear.label, gear_dict['label'])
        self.assertListEqual(gear.items, [])

    def test_load_one_gear_items_empty(self):
        schema = GearSchema()

        gear_dict = dict(
            id=1,
            label="New Gear",
            items=[]
        )
        gear_one = Gear(**gear_dict)

        result = schema.dump(gear_one)

        self.assertDictEqual(result.errors, {})
        gear = result.data

        self.assertEquals(gear['id'], gear_one.id)
        self.assertEquals(gear['label'], gear_one.label)
        self.assertListEqual(gear['items'], gear_one.items)

    def test_load_many_gear_items_empty(self):
        schema = GearSchema(many=True)

        gear_dict = dict(
            id=1,
            label="New Gear",
            items=[]
        )
        gear_dict2 = dict(
            id=2,
            label="New Gear2",
            items=[]
        )
        gear_one = Gear(**gear_dict)
        gear_two = Gear(**gear_dict2)

        result = schema.dump([gear_one, gear_two])

        self.assertDictEqual(result.errors, {})
        gear = result.data

        self.assertEquals(gear[0]['id'], gear_one.id)
        self.assertEquals(gear[0]['label'], gear_one.label)
        self.assertListEqual(gear[0]['items'], gear_one.items)

        self.assertEquals(gear[1]['id'], gear_two.id)
        self.assertEquals(gear[1]['label'], gear_two.label)
        self.assertListEqual(gear[1]['items'], gear_two.items)


@unittest2.skip("Tests are not written yet.")
class TestItemSchema(unittest2.TestCase):
    def test_add_new_item(self):
        # staff = {
        #     "name": "Hellfire Staff",
        #     "classification": "weapon",
        #     "level": 40,
        #     "skill_level": 4
        # }
        pass


if __name__ == '__main__':
    unittest2.main()
