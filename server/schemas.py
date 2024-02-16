from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Integer()
    firstname = fields.String()
    secondname = fields.String()
    email = fields.String()

class ServiceSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    start_time = fields.Time()
    end_time = fields.Time()
    service_type = fields.String()

class ChurchInfoSchema(Schema):
    id = fields.Intege()
    contact = fields.String()
    location = fields.String()
    facebook = fields.String()
    instagram = fields.String()
    youtube = fields.String()
    tiktok = fields.String()
    x_social = fields.String()