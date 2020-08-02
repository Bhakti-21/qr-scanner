import jwt
import json
from flask_restful import Resource


class Token:
    '''
    This class will generate the tokens for qr code
    '''

    def post(self, data):
        try:
            # data = {'username' : 'demo'}
            key = 'secret_qr'
            encoded = jwt.encode(data, key, algorithm='HS256')
            resp = {'key': encoded}
            return json.dumps(resp), 200

        except Exception as e:
            print(e)
            raise e
