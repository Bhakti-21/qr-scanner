import json
import jwt
import requests
from flask import request
from src.utils import db_query

qud = db_query.Query()


def authentication(f):
    def wrapper(*args, **kwargs):
        try:
            key = 'secret_qr'
            token = request.headers.get("Authorization")
            if token:
                details = qud.get_login_details(token)
                if details:
                    token_details = jwt.decode(
                        token, key, algorithms=['HS256'])
                    if details['password'] != token_details['username']:
                        return {"response": "Unauthorized"}, 401
                else:
                    return {"response": "Unauthorized"}, 401
            else:
                return {"response": "Unauthorized"}, 401

        except Exception as e:
            return {"response": "Unauthorized"}, 401

        return f(*args, **kwargs)

    return wrapper
