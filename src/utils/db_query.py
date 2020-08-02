import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from src.app import models
from src.app.models import UserDetails, Base
from src.app import app_config
from sqlalchemy.exc import IntegrityError, InvalidRequestError, SQLAlchemyError

app_env = os.environ.get('ENV', 'development')
config = app_config[app_env]
connection_string = config.CONNECTION_STRING
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


class Query:

    def get_user_details(self, id_number=None):
        try:
            if id_number:

                details = session.query(UserDetails).filter(
                    UserDetails.id_number == id_number).first()
                if details:
                    return details.to_json()

            else:
                user_details = []
                details = session.query(UserDetails).all()
                if details:
                    for cd in details:
                        user_details.append(cd.to_json())

                    return user_details

        except Exception as e:
            raise e

    def store_user_details(self, data):
        try:
            user_details = UserDetails()
            user_details.id_number = data['id_number']

            user_details.first_name = data['first_name']
            user_details.last_name = data['last_name']
            user_details.mobile = data['mobile']
            user_details.image = data['image_url']
            user_details.gender = data['gender']
            session.add(user_details)
            session.flush()
            session.commit()

        except Exception as e:
            session.rollback()
            print(e)
            raise e

    def update_user_details(self, data):

        try:
            user_details = session.query(UserDetails).filter_by(
                id_number=data['id_number']).first()
            print(user_details.__dict__)

            if user_details:

                for column_name, value in data.items():
                    setattr(user_details, column_name, value)
                session.add(user_details)
                session.commit()

        except Exception as e:
            raise e

    def delete_user_details(self, id_number):
        try:
            user_details = session.query(UserDetails).filter(
                UserDetails.id_number == id_number).first()

            if user_details:
                session.delete(user_details)
                session.commit()
                return True
            else:
                return False

        except Exception as e:
            raise e

    def get_login_details(self, token):
        try:
            details = session.query(Login).filter(
                Login.token == token).first()
            if details:
                return details.to_json()
            else:
                return None

        except Exception as e:
            raise e
