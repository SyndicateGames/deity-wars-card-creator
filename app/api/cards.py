from flask import jsonify, request
from flask.ext.classy import FlaskView, route

from .serializers.cards import get_card_schema
from app.objects.cards import Cards
from app.utils.exceptions import HTTPError

class CardsView(FlaskView):
    def index(self):
        cards = Cards()
        response = self.build_response('all', cards.get_cards())
        return jsonify(response)

    @route('/<type>/')
    def get_cards(self, type):
        card_type = Cards.get_card_type(type)
        cards = Cards(card_type)
        response = self.build_response(type, cards.get_cards())
        return jsonify(response)

    def post(self):
        json = request.get_json(silent=True)
        if not json:
            raise HTTPError(400, 'Invalid request type')

        if 'type' not in json:
            raise HTTPError(400, 'Must specify card type')

        card_type = Cards.get_card_type(json.get('type'))
        card = Cards(card_type)
        card.add_card(json)
        return jsonify([])

    @route('/edit/<id>', methods=['PUT'])
    def edit_card(self, id):
        json = request.get_json(silent=True)
        if not json:
            raise HTTPError(400, 'Invalid request type')

        card = Cards()
        card.add_card(json, id)
        return jsonify([])

    def delete(self, id):
        card = Cards()
        card.delete_card(id)
        return jsonify([])

    @staticmethod
    def build_response(type, items, include=[]):
        exclude = []
        data = dict()
        if not isinstance(items, list):
            items = [items]
        for _include in include:
            exclude.remove(_include)
        data['cards'] = get_card_schema(type)(
                exclude=exclude
            ).serialize(items)
        return data

