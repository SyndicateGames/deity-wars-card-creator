from flask import Flask, g, render_template

from app.utils import get_db


def create_app(config=None):
    app = Flask(__name__)

#    @app.before_request
#    def before_request():
#        g.db = get_db()

#    @app.teardown_request
#    def teardown(exception=None):
#        g.db.close()

    @app.route('/deity')
    def deity():
        return render_template('deity.html')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()
