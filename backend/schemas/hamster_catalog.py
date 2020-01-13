from marshmallow import Schema, fields

class HamsterCatalogPublickSchema(Schema):
    breed = fields.String()
    price = fields.Integer()

    class meta():
        type_ = 'hamser_catalog'