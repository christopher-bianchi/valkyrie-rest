#!/usr/bin/env python
# coding:utf-8
import sys
from controller import (add_gear,
                        add_hero,
                        add_item,
                        add_squad,
                        get_gear,
                        get_heroes,
                        get_items,
                        get_squads)
from flask import (Flask,
                   jsonify,
                   request)
from schema import (GearSchema,
                    HeroSchema,
                    ItemSchema,
                    SquadSchema)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


config = {
    'user': 'sandra',
    'password': 'dancer',
    'host': 'db',  # the name of our linked container
    'database': 'valkyrie'
}
engine = create_engine('mysql+mysqlconnector://sandra:dancer@db/valkyrie',
                       isolation_level='REPEATABLE_READ')
db_session = sessionmaker(bind=engine)()
app = Flask('valkyrie-rest')


@app.route('/squads', methods=['GET'])
def get_all_squads():
    """
    Get all squads for display.
    """
    # import pdb; pdb.set_trace()
    schema = SquadSchema(many=True)
    all_squads = get_squads(db_session)
    squads = schema.dump(all_squads)

    return jsonify(squads.data)


@app.route('/squads', methods=['POST'])
def add_new_squad():
    """
    Add a squad.
    """
    # import pdb; pdb.set_trace()
    squad = SquadSchema().load(request.get_json())
    add_squad(db_session, squad.data)

    return '', 204


@app.route('/heroes', methods=['GET'])
def get_all_heroes():
    """
    Get all heroes for display.
    """
    # import pdb; pdb.set_trace()
    schema = HeroSchema(many=True)
    all_heroes = get_heroes(db_session)
    heroes = schema.dump(all_heroes)

    return jsonify(heroes.data)


@app.route('/heroes', methods=['POST'])
def add_new_hero():
    """
    Add a hero.
    """
    # import pdb; pdb.set_trace()
    hero = HeroSchema().load(request.get_json())
    import pdb; pdb.set_trace()
    add_hero(db_session, hero.data)

    return '', 204


@app.route('/items', methods=['GET'])
def get_all_items():
    """
    Get all items for display.
    """
    # import pdb; pdb.set_trace()
    schema = ItemSchema(many=True)
    all_items = get_items(db_session)
    items = schema.dump(all_items)

    return jsonify(items.data)


@app.route('/items', methods=['POST'])
def add_new_item():
    """
    Add an item.
    """
    # import pdb; pdb.set_trace()
    item = ItemSchema().load(request.get_json())
    add_item(db_session, item.data)

    return '', 204


@app.route('/gear', methods=['GET'])
def get_all_gear():
    """
    Get all gear for display.
    """
    # import pdb; pdb.set_trace()
    schema = GearSchema(many=True)
    all_gear = get_gear(db_session)
    gear = schema.dump(all_gear)

    return jsonify(gear.data)


@app.route('/gear', methods=['POST'])
def add_new_gear():
    """
    Add gear.
    """
    # import pdb; pdb.set_trace()
    gear = GearSchema().load(request.get_json())
    add_gear(db_session, gear.data)

    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
