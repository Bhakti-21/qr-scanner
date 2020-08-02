import os
from src.app import create_app
from src.config import app_config


from flask import Flask
from flask_restful import Resource, request, Api
from src.routes.user import User


app_env = os.environ.get('ENV','development')
app = create_app(app_config[app_env])


if __name__ == '__main__':
	app.run(debug=True)




