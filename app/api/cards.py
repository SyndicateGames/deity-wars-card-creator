from flask import g, jsonify
from flask.ext.classy import FlaskView

from app.models import Card

class CardsView(FlaskView):
    def index(self):
        cards = g.query(Card).all()
        return jsonify({'cards': cards})
