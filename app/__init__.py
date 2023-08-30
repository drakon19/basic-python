from flask import Flask
from flask.views import MethodView
from flask_migrate import Migrate

from .Users.resources import users_blueprint
from .Database import db

class HelloWorld(MethodView):
    def get(self):
        return {'message': 'Hey there! Hello world :)'}
    





migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('../settings.py')

    db.init_app(app)
    hello_world = HelloWorld.as_view("hello_world")

    app.add_url_rule('/', view_func=hello_world)
    app.add_url_rule('/api/', view_func=hello_world)
    
    app.register_blueprint(users_blueprint)

    return app