from marshmallow import Schema, fields

#отдаю
class UserPublickSchema(Schema):
    email = fields.String()
    login = fields.String()
    balance = fields.Integer()
    
    class meta():
        type_ = 'user'


#приходит
class UserManageSchema(Schema):
    email = fields.String(load_only=True)
    login = fields.String(load_only=True)
    password = fields.String(load_only=True)

    class meta():
        type_ = 'user'