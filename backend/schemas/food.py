from marshmallow import Schema, fields

class FoodPublickSchema(Schema):
    name = fields.String()
    recovery_satiety = fields.Integer()