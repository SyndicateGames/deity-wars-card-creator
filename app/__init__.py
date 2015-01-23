from flask import Flask, g, render_template

from app.api.cards import CardsView
from app.config import POWER_TYPES, POWER_VALUES
from app.utils.db import get_db


def create_app(config=None):
    app = Flask(
        __name__,
        template_folder='client/templates',
        static_folder='client/static')

    @app.before_request
    def before_request():
        g.db = get_db()

    @app.teardown_request
    def teardown(exception=None):
        g.db.close()

    CardsView.register(app, route_base='/api/cards')

    @app.route('/cooperative')
    def cooperative():
        return render_template(
            'cooperative.html',
            power_types=POWER_TYPES,
            power_values=POWER_VALUES)

    @app.route('/deity')
    def deity():
        return render_template(
            'deity.html',
            power_types=POWER_TYPES,
            power_values=POWER_VALUES)

    @app.route('/power-boost')
    def power_boost():
        return render_template(
            'power-boost.html',
            power_types=POWER_TYPES,
            power_values=POWER_VALUES
        )

    @app.route('/special')
    def special():
        return render_template('special.html')

    @app.route('/training')
    def training():
        return render_template(
            'training.html',
            power_types=POWER_TYPES,
            power_values=POWER_VALUES)

    @app.route('/power')
    def power():
        return render_template(
            'power.html',
            power_types=POWER_TYPES,
            power_values=POWER_VALUES)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()
