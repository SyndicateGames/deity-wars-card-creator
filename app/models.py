import uuid

from sqlalchemy import (Column, ForeignKey, Integer, Text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UUID4Mixin(object):
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class IDMixin(object):
    id = Column('id', Integer, primary_key=True)


class ImageMixin(object):
    image = Column(Text)


class DeityWarsSchema(object):
    __table_args__ = {'schema': 'cards'}


class Card(DeityWarsSchema, IDMixin, Base):
    __tablename__ = 'card'
    name = Column(Text)
    image = Column(Text)
    rarity = Column(Text)
    type = Column(Text)


class CardFKMixin(object):
    id = Column('id', Integer, ForeignKey('cards.card.id'), primary_key=True)


class PowerCard(Card, CardFKMixin):
    __tablename__ = 'power_card'
    power = Column(Text)
    value = Column(Integer)


class DeityCard(Card, CardFKMixin):
    __tablename__ = 'deity_card'
    elemental = Column(Integer)
    combat = Column(Integer)
    physical = Column(Integer)
    inherent = Column(Text)


class PowerBoostCard(Card, CardFKMixin):
    __tablename__ = 'power_boost_card'
    power_required = Column(Text)
    value_required = Column(Integer)
    power_boost = Column(Text)
    value_boost = Column(Integer)


class TrainingCard(Card, CardFKMixin):
    __tablename__ = 'training_card'
    power_required_1 = Column(Text)
    value_required_1 = Column(Integer)
    power_boost_1 = Column(Text)
    value_boost_1 = Column(Integer)
    power_required_2 = Column(Text)
    value_required_2 = Column(Integer)
    power_boost_2 = Column(Text)
    value_boost_2 = Column(Integer)


class CooperativeCard(Card, CardFKMixin):
    __tablename__ = 'cooperative_card'
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


class SpecialCard(Card, CardFKMixin):
    __tablename__ = 'special_card'
    deity = Column(UUID, ForeignKey(DeityCard.id))
    special_text = Column(Text)
    special_type = Column(Text)
