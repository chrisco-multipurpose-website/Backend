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
    id = fields.Integer()
    contact = fields.String()
    location = fields.String()
    facebook = fields.String()
    instagram = fields.String()
    youtube = fields.String()
    tiktok = fields.String()
    x_social = fields.String()

class EventSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()

class AboutUsSChema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    about_img = fields.String()
    mission = fields.String()
    vision = fields.String()
    faith = fields.String()
    faith_img = fields.String()
    word= fields.String()
    word_img = fields.String()
    trinity = fields.String()
    trinity_img = fields.String()
    baptism = fields.String()
    baptism_img = fields.String()
    church_slogan = fields.String()
    purpose = fields.String()
    history_desc = fields.String()

class DepartmentSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    department_img = fields.String()