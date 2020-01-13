from peewee import *
from models import BaseModel
from models.user import User

class Food(BaseModel):
    name = CharField()
    recovery_satiety = IntegerField()
    user_id = ForeignKeyField(User, backref='food')
