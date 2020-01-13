from peewee import *
from models import BaseModel
from models.user import User

class Hamser(BaseModel):
    name = CharField()
    gender = CharField()
    color = CharField()
    breed = CharField()
    satiety = IntegerField(default=100)
    user_id = ForeignKeyField(User, backref='hamster')
