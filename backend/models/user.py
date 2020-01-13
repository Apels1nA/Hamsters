from peewee import *
from models import BaseModel


class User(BaseModel):
    email = CharField()
    login = CharField()
    password = CharField()
    balance = IntegerField(default=200)
    user_id = IntegerField()
