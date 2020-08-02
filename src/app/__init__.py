import os
from flask import Flask, json
from flask_cors import CORS
from flask_restful import Api
from src.config import app_config
from src.routes.user import User, Hello, ScanQr, MediaDownload
from src.routes.token import Token


app = Flask(__name__)
api = Api(app)


def create_app(config):
    app.config.from_object(config)
    CORS(app)

    # api.add_resource(Token, '/token', methods=['POST'], endpoint='token')
    api.add_resource(Hello, '/', methods=['GET'], endpoint='hello')
    api.add_resource(ScanQr, '/scan', methods=['GET'], endpoint='scan')
    api.add_resource(User, '/get/<id_number>',
                     methods=['GET'], endpoint='user')
    api.add_resource(User, '/create/userdetails',
                     methods=['POST'], endpoint='user_details')
    api.add_resource(User, '/update/<id_number>',
                     methods=['PUT'], endpoint='user_details_update')
    api.add_resource(User, '/delete/<id_number>',
                     methods=['DELETE'], endpoint='user_details_delete')
    api.add_resource(MediaDownload, '/media/<id_number>',
                     methods=['GET'], endpoint='media')
    return app
