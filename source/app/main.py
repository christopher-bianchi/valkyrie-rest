# coding:utf-8
import http.client
import os
import sys

from contextlib import contextmanager
from flask import (Flask,
                   jsonify,
                   request)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .controller import (add_hero,
                         add_heroes_to_squad,
                         add_item,
                         add_items_to_hero,
                         add_squad,
                         get_heroes,
                         get_hero_by_id,
                         get_items,
                         get_squads,
                         get_squad_by_id)
from .schema import (HeroSchema,
                     ItemSchema,
                     SquadSchema)


app = Flask('valkyrie-rest')


def _configure_app(app):
    config_dict = {}
    for key, value in os.environ.items():
        if 'VALK_' in key:
            config_dict[key] = value
    app.config.update(config_dict)


_configure_app(app)
connection_string = ('mysql+mysqlconnector://'
                     '{user}:{password}@{db_host}/{db}').format(
    user=app.config['VALK_DB_USER'],
    password=app.config['VALK_DB_PASSWORD'],
    db_host=app.config['VALK_DB_HOST'],
    db=app.config['VALK_DB']
)
engine = create_engine(connection_string,
                       isolation_level='REPEATABLE_READ')
db_session = sessionmaker(bind=engine)()


@contextmanager
def session_scope():
    """
    Provide a standardized transactional scope around a series of db
    operations.
    """
    try:
        yield db_session
        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()


@app.route('/squad', methods=['GET'])
def get_all_squads():
    """
    Get all squads for display.
    """
    schema = SquadSchema(many=True)
    with session_scope() as session:
        all_squads = get_squads(session)
        squads = schema.dump(all_squads)

    return jsonify(squads.data)


@app.route('/squad/<int:squad_id>', methods=['GET'])
def squad_by_id(squad_id):
    """
    Get an existing squad by it's ID.
    """
    schema = SquadSchema()
    with session_scope() as session:
        s = get_squad_by_id(session, squad_id)
        squad = schema.dump(s)

    return jsonify(squad.data)


@app.route('/squad', methods=['POST'])
def add_new_squad():
    """
    Add a squad.
    """
    squad = SquadSchema().load(request.get_json())
    with session_scope() as session:
        add_squad(session, squad.data)

    return '', http.client.CREATED


@app.route('/squad/<int:squad_id>', methods=['PUT'])
def update_squad(squad_id):
    """
    Add heroes to an existing squad.
    """
    hero_ids = request.get_json().get('heroes', [])
    with session_scope() as session:
        squad = get_squad_by_id(session, squad_id)
        add_heroes_to_squad(session, squad, hero_ids)

    return '', http.client.NO_CONTENT


@app.route('/squad/<int:squad_id>/hero/<int:hero_id>/set', methods=['PUT'])
def update_gear_set(squad_id, hero_id):
    """
    Assign items to a hero in an existing squad.
    """
    item_ids = request.get_json().get('items', [])
    with session_scope() as session:
        squad = get_squad_by_id(session, squad_id)
        hero = get_hero_by_id(session, hero_id)
        add_items_to_hero(session, squad, hero, item_ids)

    return '', http.client.NO_CONTENT


@app.route('/hero', methods=['GET'])
def get_all_heroes():
    """
    Get all heroes for display.
    """
    schema = HeroSchema(many=True)
    with session_scope() as session:
        all_heroes = get_heroes(session)
        heroes = schema.dump(all_heroes)

    return jsonify(heroes.data)


@app.route('/hero/<int:hero_id>', methods=['GET'])
def hero_by_id(hero_id):
    """
    Get an existing hero by it's ID.
    """
    schema = HeroSchema()
    with session_scope() as session:
        h = get_hero_by_id(session, hero_id)
        hero = schema.dump(h)

    return jsonify(hero.data)


@app.route('/hero', methods=['POST'])
def add_new_hero():
    """
    Add a hero.
    """
    hero = HeroSchema().load(request.get_json())
    with session_scope() as session:
        add_hero(session, hero.data)

    return '', http.client.CREATED


@app.route('/item', methods=['GET'])
def get_all_items():
    """
    Get all items for display.
    """
    schema = ItemSchema(many=True)
    with session_scope() as session:
        all_items = get_items(session)
        items = schema.dump(all_items)

    return jsonify(items.data)


@app.route('/item', methods=['POST'])
def add_new_item():
    """
    Add an item.
    """
    item = ItemSchema().load(request.get_json())
    with session_scope() as session:
        add_item(session, item.data)

    return '', http.client.CREATED
