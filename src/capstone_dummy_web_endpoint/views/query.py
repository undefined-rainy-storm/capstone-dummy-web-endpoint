from flask import request
from flask_restful import Resource
from datetime import datetime

from ..models.enums.emotion import Emotions

from random import choice

class Query(Resource):
    def get(self):
        return { 'status': 'ok', 'timestamp': datetime.now().isoformat() }
    
    def post(self):
        req = request.get_json()
        if 'image' in req:
            return {
                'status': 'ok',
                'timestamp': datetime.now().isoformat(),
                'result': choice(list(Emotions)).value
            }, 200
        else:
            return {
                'status': 'error',
                'timestamp': datetime.now().isoformat(),
                'message': 'Image not found'
            }, 400
