from sqlalchemy import (Column, ForeignKey, Integer, Text)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeityWarsSchema(object):
    __table_args__ = {'schema': 'cards'}


class Card(DeityWarsSchema, Base):
    __tablename__ = 'card'
    id = Column('id', Integer, primary_key=True)
    name = Column(Text)
    image = Column(Text)
    rarity = Column(Text)
    type = Column(Text)
    __mapper_args__ = {
        'polymorphic_identity': 'Card',
        'polymorphic_on': type
    }


class PowerCard(Card):
    __tablename__ = 'power_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    power = Column(Text)
    value = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity': 'power'
    }


class DeityCard(Card):
    __tablename__ = 'deity_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    elemental = Column(Integer)
    combat = Column(Integer)
    physical = Column(Integer)
    inherent = Column(Text)
    __mapper_args__ = {
        'polymorphic_identity': 'deity'
    }


class PowerBoostCard(Card):
    __tablename__ = 'power_boost_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    power_required = Column(Text)
    value_required = Column(Integer)
    power_boost = Column(Text)
    value_boost = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity': 'power_boost'
    }


class TrainingCard(Card):
    __tablename__ = 'training_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    power_required_1 = Column(Text)
    value_required_1 = Column(Integer)
    power_boost_1 = Column(Text)
    value_boost_1 = Column(Integer)
    power_required_2 = Column(Text)
    value_required_2 = Column(Integer)
    power_boost_2 = Column(Text)
    value_boost_2 = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity': 'training'
    }


class CooperativeCard(Card):
    __tablename__ = 'cooperative_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    power_required = Column(Text)
    value_required = Column(Integer)
    power_attack = Column(Text)
    value_attack = Column(Integer)
    first_power_boost_1 = Column(Text)
    first_power_value_1 = Column(Integer)
    second_power_boost_1 = Column(Text)
    second_power_value_1 = Column(Integer)
    first_power_boost_2 = Column(Text)
    first_power_value_2 = Column(Integer)
    second_power_boost_2 = Column(Text)
    second_power_value_2 = Column(Integer)
    __mapper_args__ = {
        'polymorphic_identity': 'cooperative'
    }


class SpecialCard(Card):
    __tablename__ = 'special_card'
    id = Column(Integer, ForeignKey('cards.card.id'), primary_key=True)
    deity = Column(Integer, ForeignKey(DeityCard.id))
    special_text = Column(Text)
    special_type = Column(Text)
    __mapper_args__ = {
        'polymorphic_identity': 'special'
    }
