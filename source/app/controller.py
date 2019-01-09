# coding:utf-8
from .model import (#Gear,
                    Hero,
                    Item,
                    Squad,
                    GearSet)


def add_hero(db_session, hero):
    """
    Store a new hero.
    """
    db_session.add(hero)


def add_heroes_to_squad(db_session, squad, hero_ids):
    """
    Assign heroes to an existing squad.
    """
    if hero_ids:
        for hid in hero_ids:
            hero = get_hero_by_id(db_session, hid)
            squad.heroes.append(hero)
        db_session.add(squad)


def add_item(db_session, item):
    """
    Store a new item.
    """
    db_session.add(item)


def add_items_to_hero(db_session, squad, hero, item_ids):
    """
    Assign items to a hero in an existing squad.
    """
    # import pdb; pdb.set_trace()
    if item_ids:
        for iid in item_ids:
            item = get_item_by_id(db_session, iid)
            squad_hero_item = GearSet(squad_id=squad.id)
            squad_hero_item.item = item
            hero.items.append(squad_hero_item)
        # get item
        # make GearSet
        # assign item to GearSet
        # add GearSet to hero.items
        db_session.add(hero)


def add_squad(db_session, squad):
    """
    Store a new squad.
    """
    db_session.add(squad)


def get_heroes(db_session):
    """
    Get all stored heroes.
    """
    heroes = db_session.query(Hero).all()
    return heroes


def get_hero_by_id(db_session, hid):
    """
    Get an existing hero by it's ID.
    """
    hero = db_session.query(Hero).filter_by(id=hid).one()
    return hero


def get_hero_by_name(db_session, name):
    """
    Get an existing hero by it's name.
    """
    hero = db_session.query(Hero).filter_by(name=name).one()
    return hero


def get_items(db_session):
    """
    Get all stored items.
    """
    items = db_session.query(Item).all()
    return items


def get_item_by_id(db_session, iid):
    """
    Get an existing item by it's ID.
    """
    item = db_session.query(Item).filter_by(id=iid).one()
    return item


def get_item_by_name(db_session, name):
    """
    Get an existing item by it's name.
    """
    item = db_session.query(Item).filter_by(name=name).one()
    return item


def get_squads(db_session):
    """
    Get all stored squads.
    """
    squads = db_session.query(Squad).all()
    return squads


def get_squad_by_id(db_session, sid):
    """
    Get an existing squad by it's ID.
    """
    squad = db_session.query(Squad).filter_by(id=sid).one()
    return squad


def get_squad_by_name(db_session, name):
    """
    Get an existing squad by it's name.
    """
    squad = db_session.query(Squad).filter_by(name=name).one()
    return squad
