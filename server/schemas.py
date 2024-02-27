from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.Integer()
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String()

class ProfileDetailSchema(Schema):
    id = fields.Integer()
    phone_number = fields.String()
    address = fields.String()
    bio = fields.String()
    profile_picture = fields.String()

class ServiceSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    start_time = fields.String()
    end_time = fields.String()
    service_type = fields.String()

class ChurchInfoSchema(Schema):
    id = fields.Integer()
    contact = fields.String()
    location = fields.String()
    address = fields.String()
    email = fields.String()
    website = fields.String()
    facebook_url = fields.String()
    instagram_url = fields.String()
    youtube_url = fields.String()
    tiktok_url = fields.String()
    x_url = fields.String()

class EventSchema(Schema):
    id = fields.Integer()
    event_img = fields.String()
    event_category = fields.String()
    title = fields.String()
    description = fields.String()
    theme = fields.String()
    scripture = fields.String()
    location = fields.String()
    date = fields.Date()
    start_time = fields.String()
    end_time = fields.String()
    event_host = fields.String()

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

class BlogSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    blog_img = fields.String()

class SliderImageSchema(Schema):
    id = fields.Integer()
    slider_img = fields.String()

class PrayerRequestSchema(Schema):
    id = fields.Integer()
    request = fields.String()
    timestamp = fields.DateTime()

class CommentSchema(Schema):
    id = fields.Integer()
    content = fields.String()
    timestamp = fields.DateTime()