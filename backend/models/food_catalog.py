from peewee import *
from models import BaseModel

class FoodCatalog(BaseModel):
    name = CharField()
    recovery_satiety = IntegerField()
    price = IntegerField()
