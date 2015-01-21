from marshmallow import fields

from .base import BaseSchema

class CardSchema(BaseSchema):
    id = fields.Integer(attribute='id')
    name = fields.String(attribute='name')
    image = fields.String(attribute='image')
    rarity = fields.String(attribute='rarity')
    type = fields.String(attribute='string')

class PowerSchema(CardSchema):
    power = fields.String(attribute='power')
    value = fields.String(attribute='value')

class DeitySchema(CardSchema):
    elemental = fields.Integer(attribute='elemental')
    combat = fields.Integer(attribute='combat')
    physical = fields.Integer(attribute='physical')
    inherent = fields.String(attribute='inherent')

class PowerBoostSchema(CardSchema):
    powerRequired = fields.String(attribute='power_required')
    valueRequired = fields.Integer(attribute='value_required')
    powerBoost = fields.String(attribute='power_boost')
    valueBoost = fields.Integer(attribute='value_boost')

class TrainingSchema(CardSchema):
    powerRequired1 = fields.String(attribute='power_required_1')
    valueRequired1 = fields.Integer(attribute='value_required_1')
    powerBoost1 = fields.String(attribute='power_boost_1')
    valueBoost1 = fields.Integer(attribute='value_boost_1')
    powerRequired2 = fields.String(attribute='power_required_1')
    valueRequired2 = fields.Integer(attribute='value_required_1')
    powerBoost2 = fields.String(attribute='power_boost_1')
    valueBoost2 = fields.Integer(attribute='value_boost_1')

class CooperativeSchema(CardSchema):
    powerRequired = fields.String(attribute='power_required')
    valueRequired = fields.Integer(attribute='value_required')
    powerAttack = fields.String(attribute='power_attack')
    valueAttack = fields.Integer(attribute='value_attack')
    firstPowerBoost1 = fields.String(attribute='first_power_boost_1')
    firstValueBoost1 = fields.Integer(attribute='first_value_boost_1')
    secondPowerBoost1 = fields.String(attribute='second_power_boost_1')
    secondValueBoost1 = fields.Integer(attribute='second_value_boost_1')
    firstPowerBoost2 = fields.String(attribute='first_power_boost_2')
    firstValueBoost2 = fields.Integer(attribute='first_value_boost_2')
    secondPowerBoost2 = fields.String(attribute='second_power_boost_2')
    secondValueBoost2 = fields.Integer(attribute='second_value_boost_2')

class SpecialSchema(CardSchema):
    deity = fields.Integer(attribute='deity')
    specialText = fields.String(attribute='special_text')
    specialType = fields.String(attribute='special_type')

def get_card_schema(type):
    obj_map = {
        'ALL': CardSchema,
        'DEITY': DeitySchema,
        'POWER': PowerSchema,
        'POWER_BOOST': PowerBoostSchema,
        'TRAINING': TrainingSchema,
        'COOPERATIVE': CooperativeSchema,
        'SPECIAL': SpecialSchema
    }
    type = type.upper()
    if type in obj_map:
        return obj_map[type]
