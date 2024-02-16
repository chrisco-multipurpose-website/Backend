from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, nullable=False)
    secondname = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.email}>"
    # set hash password
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    # check if password is correct >> login
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    # check if user exists
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    # save user
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete user
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return  f"<Token {self.jti}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class ChurchInfo(db.Model):
    __tablename__ = 'church_info'

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    facebook = db.Column(db.String(255), nullable=True)
    instagram = db.Column(db.String(255), nullable=True)
    youtube = db.Column(db.String(255), nullable=True)
    tiktok = db.Column(db.String(255), nullable=True)
    x_social = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<ChurchInfo {self.contact}>"
    
     # get info by id
    @classmethod
    def get_service_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    # save info
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete info
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) # The name of the service (e.g., Sunday service, Midweek service, Overnight service).
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    service_type = db.Column(db.String(50), nullable=False) # The type of service (e.g., IN-PERSON, ONLINE, IN-PERSON & ONLINE).

    def __repr__(self):
        return f"<Service {self.name}>"
    
    # get service by id
    @classmethod
    def get_service_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    # save service
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete service
    def delete(self):
        db.session.delete(self)
        db.session.commit()













    # member_status = db.Column(db.Boolean, default=True)
    # admin_status = db.Column(db.Boolean, default=False)
    # super_admin_status = db.Column(db.Boolean, default=False)

    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    # personal_info_id = db.Column(db.Integer, db.ForeignKey('personal_info.id'))

    # personal_info = db.relationship('PersonalInfo', backref='user')
    # comments = db.relationship('Comment', backref='user')
    # donations = db.relationship('Donation', backref='user')
    # form_submissions = db.relationship('FormSubmission', backref='user')
    # roles = db.relationship('Role', backref='user')
    # events = db.relationship('Event', backref='user')

# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))

# class PersonalInfo(db.Model):
#     __tablename__ = 'personalinfos'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     full_name = db.Column(db.String(120))
#     address = db.Column(db.String(120))
#     phone_number = db.Column(db.String(120))
#     email = db.Column(db.String(120))

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
# class Comment(db.Model):
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, ondelete='CASCADE')
#     content = db.Column(db.String(120))
#     approved = db.Column(db.Boolean)
#     created_at = db.Column(db.DateTime)

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class Department(db.Model):
#     __tablename__ = 'departments'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String(120))

# class Event(db.Model):
#     __tablename__ = 'events'

#     id = db.Column(db.Integer, primary_key=True)
#     department_id = db.Column(db.Integer)
#     name = db.Column(db.String(120))
#     description = db.Column(db.String(120))
#     date = db.Column(db.DateTime)
#     location = db.Column(db.String(120))
#     organizer_info = db.Column(db.String(120))

#     department_id = db.Column(db.Integer, db.ForeignKey('department.id'))

# class Sermon(db.Model):
#     __tablename__ = 'sermons'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     date = db.Column(db.DateTime)
#     video_url = db.Column(db.String)
#     audio_url = db.Column(db.String)
#     notes = db.Column(db.String)
#     scripture = db.Column(db.String)

# class Donation(db.Model):
#     __tablename__ = 'donations'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     amount = db.Column(db.Float)
#     donation_date = db.Column(db.DateTime)

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class FormSubmission(db.Model):
#     __tablename__ = 'formsubmissions'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer)
#     form_type = db.Column(db.String)
#     content = db.Column(db.String)
#     subitted_at = db.Column(db.DateTime)

#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))