from marshmallow import Schema, fields

class FoodCatalogPublickSchema(Schema):
    name = fields.String()
    recovery_satiety = fields.Integer()
    price = fields.Integer()

    class meta():
        type_ = 'food_catalog'
