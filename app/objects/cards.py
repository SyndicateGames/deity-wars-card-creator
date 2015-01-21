from flask import g

from app.models import (
    Card, DeityCard, PowerCard, PowerBoostCard,
    TrainingCard, CooperativeCard,
    SpecialCard)
from app.utils.exceptions import HTTPError

class Cards(object):   
    ALL = 0
    DEITY_CARD = 1
    POWER_CARD = 2
    POWER_BOOST_CARD = 3
    TRAINING_CARD = 4
    COOPERATIVE_CARD = 5
    SPECIAL_CARD = 6

    type_map = {
        ALL: Card,
        DEITY_CARD: DeityCard,
        POWER_CARD: PowerCard,
        POWER_BOOST_CARD: PowerBoostCard,
        TRAINING_CARD: TrainingCard,
        COOPERATIVE_CARD: CooperativeCard,
        SPECIAL_CARD: SpecialCard
    }

    def __init__(self, type=0):
        self.type = type
        self.obj = self.type_map[type]

    @staticmethod
    def get_card_type(string):
        str_type_map = {
            'ALL': 0,
            'DEITY': 1,
            'POWER': 2,
            'POWER_BOOST': 3,
            'TRAINING': 4,
            'COOPERATIVE': 5,
            'SPECIAL': 6
        }
        string = string.upper()
        if string in str_type_map:
            return str_type_map[string]
        else:
            raise HTTPError(400, 'Invalid Card Type')

    def get_cards(self):
        cards = g.db.query(self.obj).all()
        return cards

    def add_card(self, values, id=None):
        card = None
        if id:
            card = g.db.query(self.obj).get(id)
            if not card:
                raise HTTPError(400, 'Cannot find card with id ' + id)
        else:
            if self.type == self.ALL:
                raise HTTPError(400, 'Cannot add a card without a type')
            card = self.obj()
            g.db.add(card)

        for key, value in values.iteritems():
            try:
                setattr(card, key, value)
            except:
                raise HTTPError(400, 'Cannot set attribute: [{}] to value: [{}] for this type of card'.format(key, value))
        g.db.commit()
        return card

    def delete_card(self, id):
        card = g.db.query(self.obj).get(id)
        if card:
            g.db.delete(card)
            g.db.commit()
