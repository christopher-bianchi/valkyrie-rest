# coding:utf-8
from model import (Gear,
                   Hero,
                   Item,
                   Squad)


def get_squads(db_sess):
    """
    Get all stored squads.
    """
    squads = db_sess.query(Squad).all()
    return squads


def add_squad(db_sess, squad):
    """
    Store a new squad.
    """
    # import pdb; pdb.set_trace()
    db_sess.add(squad)
    db_sess.commit()
    db_sess.close()


def get_heroes(db_sess):
    """
    Get all stored heroes.
    """
    heroes = db_sess.query(Hero).all()
    return heroes


def add_hero(db_sess, hero):
    """
    Store a new hero.
    """
    # import pdb; pdb.set_trace()
    db_sess.add(hero)
    db_sess.commit()
    db_sess.close()


def get_items(db_sess):
    """
    Get all stored items.
    """
    items = db_sess.query(Item).all()
    return items


def add_item(db_sess, item):
    """
    Store a new item.
    """
    # import pdb; pdb.set_trace()
    db_sess.add(item)
    db_sess.commit()
    db_sess.close()


def get_gear(db_sess):
    """
    Get all stored gear.
    """
    gear = db_sess.query(Gear).all()
    return gear


def add_gear(db_sess, gear):
    """
    Store new gear.
    """
    # import pdb; pdb.set_trace()
    db_sess.add(gear)
    db_sess.commit()
    db_sess.close()
