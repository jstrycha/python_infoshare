# https://flask-restx.readthedocs.io/en/latest/index.html

from functools import wraps

import namespace
from flask import Flask, request
from flask_restx import Resource, Api, abort, Namespace

API_KEY = 'TAjNY_API_KI_Itowdodatkubardzodlugi'

HEADER_SECURE_NAME = 'X-API-KEY'

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': HEADER_SECURE_NAME
    }
}

app = Flask(__name__)
api = Api(app, authorizations=authorizations)


api_hello = Namespace('hello', description='Witam')
api_bye = Namespace('bye', description='DoWidzenia')

api.add_namespace(api_hello)
api.add_namespace(api_bye)


def secure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get(HEADER_SECURE_NAME)
        print('wywołano metodę post')
        if api_key != API_KEY:
            abort(401, 'Bad API Key')
        return func(*args, **kwargs)
    return wrapper


@api_hello.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    @secure
    @api.doc(security='apikey')
    def post(self):
        return {'hello': 'world'}

@api_bye.route('/bye')
class Bye(Resource):
    def get(self):
        return {'bye': 'world'}

if __name__ == '__main__':
    app.run(debug=True)