# coding:utf-8
from marshmallow import (fields,
                         pre_load,
                         post_load,
                         Schema)
from model import (Gear,
                   Hero,
                   Item,
                   Squad)


class SquadSchema(Schema):
    id = fields.Integer(dump_only=True)
    label = fields.String(required=True)
    heroes = fields.Nested('HeroSchema', many=True, exclude=('squads', ))

    @pre_load
    def process_hero(self, data):
        """
        Allow hero ids to be passed in instead of a full Hero schema.
        """
        from flask_app import db_session

        heroes = []
        hero_ids = data.get('heroes', [])

        for hid in hero_ids:
            if isinstance(hid, int):
                hero = db_session.query(Hero).get(hid)
                heroes.append(hero)

        if heroes:
            hero_schema = HeroSchema(many=True)
            data['heroes'] = hero_schema.dump(heroes).data

        # import pdb; pdb.set_trace()
        return data

    @post_load
    def make_squad(self, data):
        """
        Call this method after deserializing a Squad JSON object.
        """
        # import pdb; pdb.set_trace()
        return Squad(**data)


class HeroSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    level = fields.Integer(required=True)
    gear = fields.Nested('GearSchema', many=True, exclude=('heroes', ))
    squads = fields.Nested('SquadSchema', many=True, only=('id', 'label'))

    # @pre_load
    # def process_item(self, data):
    #     """
    #     Allow item ids to be passed in instead of a full Item schema.
    #     """
    #     from flask_app import db_session
    #     # import pdb; pdb.set_trace()

    #     items = []
    #     item_ids = data.get('gear', {}).get('items', [])

    #     for iid in item_ids:
    #         if isinstance(iid, int):
    #             item = db_session.query(Item).get(iid)
    #             items.append(item)

    #     if items:
    #         item_schema = ItemSchema(many=True)
    #         data['gear']['items'] = item_schema.dump(items).data

    #     # import pdb; pdb.set_trace()
    #     return data

    @post_load
    def make_hero(self, data):
        """
        Call this method after deserializing a Hero JSON object.
        """
        # import pdb; pdb.set_trace()
        return Hero(**data)


class GearSchema(Schema):
    id = fields.Integer(dump_only=True)
    label = fields.String(required=True)
    heroes = fields.Nested('HeroSchema', many=True)
    items = fields.Nested('ItemSchema', many=True, exclude=('gear', ))

    @post_load
    def make_gear(self, data):
        """
        Call this method after deserializing a Gear JSON object.
        """
        return Gear(**data)


class ItemSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    classification = fields.String(required=True)
    level = fields.Integer(required=True)
    skill_level = fields.Integer(required=True)
    gear = fields.Nested('GearSchema', many=True, only=('id', 'label'))

    @post_load
    def make_item(self, data):
        """
        Call this method after deserializing an Itme JSON object.
        """
        return Item(**data)
