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


hero_x_gear = Table('hero_x_gear', Base.metadata,
    Column('hero_id', Integer, ForeignKey('hero.id')),
    Column('gear_id', Integer, ForeignKey('gear.id'))
)


gear_x_item = Table('gear_x_item', Base.metadata,
    Column('gear_id', Integer, ForeignKey('gear.id')),
    Column('item_id', Integer, ForeignKey('item.id'))
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
    gear = relationship(
        "Gear",
        secondary=hero_x_gear,
        back_populates="hero"
    )
    squads = relationship(
        "Squad",
        secondary=squad_x_hero,
        back_populates="heroes"
    )

    # def __init__(self, name, level):
    #     self.name = name
    #     self.level = level


class Gear(Base):
    __tablename__ = 'gear'

    id = Column(Integer, primary_key=True)
    label = Column(String(128), nullable=False)
    hero = relationship(
        "Hero",
        secondary=hero_x_gear,
        back_populates="gear"
    )
    items = relationship(
        "Item",
        secondary=gear_x_item,
        back_populates="gear"
    )


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    classification = Column(String(128), nullable=False)
    level = Column(Integer, nullable=False)
    skill_level = Column(Integer, nullable=False)
    gear = relationship(
        "Gear",
        secondary=gear_x_item,
        back_populates="items"
    )
