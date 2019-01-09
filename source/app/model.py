# coding:utf-8
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


squad_x_hero = Table('squad_x_hero', Base.metadata,
    Column('squad_id', Integer, ForeignKey('squad.id')),
    Column('hero_id', Integer, ForeignKey('hero.id'))
)


class Squad(Base):
    __tablename__ = 'squad'

    id = Column(Integer, primary_key=True)
    label = Column(String(128), nullable=False)
    heroes = relationship(
        "Hero",
        secondary=squad_x_hero,
        back_populates="squads"
    )

    # def __init__(self, label):
    #     self.label = label


class Hero(Base):
    __tablename__ = 'hero'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    level = Column(Integer, nullable=False)

    squads = relationship(
        "Squad",
        secondary=squad_x_hero,
        back_populates="heroes"
    )
    gear_set = relationship('GearSet', back_populates='hero')

    # TODO: rework model and session context.
    # def __init__(self, db_session):
    #     self._session = db_session

    # def add(db_session, hero):
    #     """
    #     Store a new hero.
    #     """
    #     db_session.add(hero)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    classification = Column(String(128), nullable=False)
    level = Column(Integer, nullable=False)
    skill_level = Column(Integer, nullable=False)

    heroes = relationship('GearSet', back_populates='item')


class GearSet(Base):
    __tablename__ = 'gear_set'

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey(Hero.id))
    item_id = Column(Integer, ForeignKey(Item.id))
    squad_id = Column(Integer, ForeignKey(Squad.id), nullable=False)

    hero = relationship('Hero', back_populates='gear_set')
    item = relationship('Item', back_populates='heroes')
