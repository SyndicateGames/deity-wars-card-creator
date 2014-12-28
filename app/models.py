import uuid

from sqlalchemy import (Boolean, Column, ForeignKey, Integer, Text)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UUID4Mixin(object):
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)


class ImageMixin(object):
    image = Column(Text)


class DeityWarsSchema(object):
    __table_args__ = {'schema': 'deitywars'}


class PowerCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'power_card'
    power = Column(Text)
    value = Column(Integer)

    def __init__(self, power='', value='', image=''):
        self.power = power
        self.value = value
        self.image = image

    def serialize(self):
        return dict(
            power=self.power,
            value=self.value,
            image=self.image,
        )


class DeityCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'character_card'
    name = Column(Text)
    elemental = Column(Integer)
    combat = Column(Integer)
    physical = Column(Integer)
    inherent = Column(Text)

    def __init__(self, name='', image='', elemental='', combat='', physical='', inherent=''):
        self.name = name
        self.image = image
        self.elemental = elemental
        self.combat = combat
        self.physical = physical
        self.inherent = inherent

    def serialize(self):
        return dict(
            image=self.image,
            name=self.name,
            elemental=self.elemental,
            combat=self.combat,
            inherent=self.inherent
        )


class PowerBoostCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'power_boost_card'
    name = Column(Text)
    power_required = Column(Text)
    value_required = Column(Integer)
    power_boost = Column(Text)
    value_boost = Column(Integer)

    def __init__(self, name='', image='', power_required='', value_required='', power_boost='', value_boost=''):
        self.name = name
        self.image = image
        self.power_required = power_required
        self.value_required = value_required
        self.power_boost = power_boost
        self.value_boost = value_boost

    def serialize(self):
        return dict(
            image=self.image,
            name=self.name,
            powerRequired=self.power_required,
            valueRequired=self.value_required,
            powerBoost=self.power_boost,
            valueBoost=self.value_boost
        )


class TrainingCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'training_card'
    name = Column(Text)
    power_required_1 = Column(Text)
    value_required_1 = Column(Integer)
    power_boost_1 = Column(Text)
    value_boost_1 = Column(Integer)
    power_required_2 = Column(Text)
    value_required_2 = Column(Integer)
    power_boost_2 = Column(Text)
    value_boost_2 = Column(Integer)

    def __init__(self, name='', image='', power_required_1='', value_required_1='', power_boost_1='', value_boost_1='',
                 power_required_2, value_required_2, power_boost_2, value_boost_2):
        self.name = name
        self.image = image
        self.power_required_1 = power_required_1,
        self.value_required_1 = value_required_1,
        self.power_boost_1 = power_boost_1,
        self.value_boost_1 = value_boost_1
        self.power_required_2 = power_required_2,
        self.value_required_2 = value_required_2,
        self.power_boost_2 = power_boost_2,
        self.value_boost_2 = value_boost_2

    def serialize(self):
        return dict(
            image=self.image,
            name=self.name,
            powerRequired1=self.power_required_1,
            valueRequired1=self.value_required_1,
            powerBoost1=self.power_boost_1,
            valueBoost1=self.value_boost_1,
            powerRequired2=self.power_required_2,
            valueRequired2=self.value_required_2,
            powerBoost2=self.power_boost_2,
            valueBoost2=self.value_boost_2
        )


class CooperativeCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'cooperative_card'
    name = Column(Text)
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

    def __init__(self, image, name, power_required, value_required, power_attack, value_attack,
                 first_power_boost_1, first_power_value_1, second_power_boost_1, second_power_value_1,
                 first_power_boost_2, first_power_value_2, second_power_boost_2, second_power_value_2):
        self.image = image
        self.name = name
        self.power_required = power_required
        self.value_required = value_required
        self.power_attack = power_attack
        self.value_attack = value_attack
        self.first_power_boost_1 = first_power_boost_1
        self.first_power_value_1 = first_power_value_1
        self.second_power_boost_1 = second_power_boost_1
        self.second_power_value_1 = second_power_value_1
        self.first_power_boost_2 = first_power_boost_2
        self.first_power_value_2 = first_power_value_2
        self.second_power_boost_2 = second_power_boost_2
        self.second_power_value_2 = second_power_value_2

    def serialize(self):
        return dict(
            image=self.image,
            name=self.name,
            powerRequired=self.power_required,
            valueRequired=self.value_required,
            powerAttack=self.power_attack,
            valueAttack=self.value_attack,
            firstPowerBoost1=self.first_power_boost_1,
            firstPowerValue1=self.first_power_value_1,
            secondPowerBoost1=self.second_power_boost_1,
            secondPowerValue1=self.second_power_value_1,
            firstPowerBoost2=self.first_power_boost_2,
            firstPowerValue2=self.first_power_value_2,
            secondPowerBoost2=self.second_power_boost_2,
            secondPowerValue2=seld.second_power_value_2
        )


class SpecialCard(DeityWarsSchema, UUID4Mixin, ImageMixin, Base):
    __tablename__ = 'special_card'
    name = Column(Text)
    deity = Column(UUID, ForeignKey(DeityCard.id))
    special_text = Column(Text)
    special_type = Column(Text)

    def __init__(self, image, name, deity, special_text, special_type):
        self.name = name,
        self.deity = deity,
        self.special_text = special_text,
        self.special_type = special_type
