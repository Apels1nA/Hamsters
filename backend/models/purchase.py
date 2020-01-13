from peewee import *
from models import BaseModel

class Purchase(BaseModel):
    product_type = CharField()
    number_of_purchase = IntegerField()