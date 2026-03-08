from marshmallow import Schema, fields

class ItemSchema(Schema):# only return
    item = fields.Str(required = True)
    price = fields.Int(required = True)

class GetItemSchema(Schema):
    id = fields.Int(dump_only = True)
    item = fields.Nested(ItemSchema)
    
class OptionalGetSchema(Schema):
    id = fields.Int(required = False)

class PostItemSchema(Schema):
    item = fields.Str(required = True)
    price = fields.Int(required = True)

class RequiredIdSchema(Schema):
    id = fields.Int(required = True)

class MessageSchema(Schema):
    message = fields.Str(required = True)

class UserSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)

class UserPostSchema(Schema):
    username = fields.Str(required = True)
    password = fields.Str(required = True)