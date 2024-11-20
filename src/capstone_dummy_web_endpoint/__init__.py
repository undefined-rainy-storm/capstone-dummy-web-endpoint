from flask import Flask
from flask_restful import Api

from .views.query import Query

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Query, '/query')
    return app
