import json
from sqlalchemy import Column, Integer, BOOLEAN, JSON, DateTime, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Login(Base):
    __tablename__ = 'login'
    phone_no = Column(String, primary_key=True)
    token = Column(String)
    password = Column(String)

    def to_json(self):
        return {
            "phone_no": self.phone_no,
            "token": self.token,
            "password": self.password
        }


class UserDetails(Base):
    __tablename__ = 'user_details'
    id_number = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    image = Column(String)
    mobile = Column(String)
    user_active = Column(String, default="no")

    def to_json(self):
        return {
            "id_number": self.id_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "image": self.image,
            "mobile": self.mobile,
            "user_active": self.user_active
        }
