from peewee import *
from models import BaseModel

class HamsterCatalog(BaseModel):
    breed = CharField()
    price = IntegerField()
