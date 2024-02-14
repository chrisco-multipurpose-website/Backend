from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    member_status = db.Column(db.Boolean, default=True)
    admin_status = db.Column(db.Boolean, default=False)
    super_admin_status = db.Column(db.Boolean, default=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    personal_info_id = db.Column(db.Integer, db.ForeignKey('personal_info.id'))

    personal_info = db.relationship('PersonalInfo', backref='user')
    comments = db.relationship('Comment', backref='user')
    donations = db.relationship('Donation', backref='user')
    form_submissions = db.relationship('FormSubmission', backref='user')
    roles = db.relationship('Role', backref='user')
    events = db.relationship('Event', backref='user')

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

class PersonalInfo(db.Model):
    __tablename__ = 'personalinfos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    full_name = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))
    email = db.Column(db.String(120))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ondelete='CASCADE')
    content = db.Column(db.String(120))
    approved = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(120))

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer)
    name = db.Column(db.String(120))
    description = db.Column(db.String(120))
    date = db.Column(db.DateTime)
    location = db.Column(db.String(120))
    organizer_info = db.Column(db.String(120))

    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

class Sermon(db.Model):
    __tablename__ = 'sermons'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    date = db.Column(db.DateTime)
    video_url = db.Column(db.String)
    audio_url = db.Column(db.String)
    notes = db.Column(db.String)
    scripture = db.Column(db.String)

class Donation(db.Model):
    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    donation_date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class FormSubmission(db.Model):
    __tablename__ = 'formsubmissions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    form_type = db.Column(db.String)
    content = db.Column(db.String)
    subitted_at = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))