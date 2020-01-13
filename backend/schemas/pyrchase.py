from marshmallow import Schema, fields

class PurchaseMahageSchema(Schema):
    name = fields.String()
    name = fields.String()
    number_of_purchase = fields.Integer()

    class meta():
        type_ = 'purchase'