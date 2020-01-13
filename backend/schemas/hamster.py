from marshmallow import Schema, fields

class HamsterPublickSchema(Schema):
    name = fields.String()
    gender = fields.String()
    color = fields.String()
    breed = fields.String()

    class meta():
        type_ = 'hamster'
