from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

# Define association table for many-to-many relationship between users and roles
# user_roles = db.Table('user_roles',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#     db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True)
# )

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True, nullable=False)
    lastname = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String, nullable=True)

    # roles = db.relationship('Role', secondary=user_roles, backref=db.backref('users', lazy='dynamic'))
    personal_details = db.relationship('ProfileDetail', uselist=False, back_populates='user')
    comments = db.relationship('Comment', backref='user', lazy=True)
    prayer_requests = db.relationship('PrayerRequest', backref='user', lazy=True)

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

# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String, unique=True, nullable=False)

#     def __repr__(self):
#         return f"<Role {self.name}>"

class ProfileDetail(db.Model):
    __tablename__ = 'profile_details'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    phone_number = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)

    user = db.relationship('User', back_populates='personal_details')

    def __repr__(self):
        return f"<ProfileDetails {self.user_id}>"
    
    # save profile
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete profile
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
    address = db.Column(db.String)
    email = db.Column(db.String)
    website = db.Column(db.String)
    facebook_url = db.Column(db.String(255), nullable=True)
    instagram_url = db.Column(db.String(255), nullable=True)
    youtube_url = db.Column(db.String(255), nullable=True)
    tiktok_url= db.Column(db.String(255), nullable=True)
    x_url = db.Column(db.String(255), nullable=True)

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
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
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


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_img = db.Column(db.String)
    event_category = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    theme = db.Column(db.String)
    scripture = db.Column(db.String)
    location = db.Column(db.String)
    date = db.Column(db.Date)
    start_time = db.Column(db.String)
    end_time = db.Column(db.String)
    event_host = db.Column(db.String)
    
    def __repr__(self):
        return f"<Event {self.title}>"
    
    # get event by id
    @classmethod
    def get_service_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    # save event
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete event
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class AboutUs(db.Model):
    __tablename__ = 'about_us'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    about_img = db.Column(db.String)
    mission = db.Column(db.String)
    vision = db.Column(db.String)
    faith = db.Column(db.String)
    faith_img = db.Column(db.String)
    word = db.Column(db.String)
    word_img = db.Column(db.String)
    trinity = db.Column(db.String)
    trinity_img = db.Column(db.String)
    baptism = db.Column(db.String)
    baptism_img = db.Column(db.String)
    church_slogan = db.Column(db.String)
    purpose= db.Column(db.String)
    history_desc = db.Column(db.String)

    def __repr__(self):
        return f"<About {self.title}>"

    # save about
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete about
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    department_img = db.Column(db.String)

    def __repr__(self):
        return f"<Department {self.title}>"

    # save department
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete department
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    blog_img = db.Column(db.String)
    comments = db.relationship('Comment', backref='blog', lazy=True)

    def __repr__(self):
        return f"<Blog {self.title}>"

    # save department
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete department
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class SliderImage(db.Model):
    __tablename__ = "sliderimages"

    id = db.Column(db.Integer, primary_key=True)
    slider_img = db.Column(db.String)

    def __repr__(self):
        return f"<SliderImage {self.id}>"
    
class PrayerRequest(db.Model):
    __tablename__ = 'prayer_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    request = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # # Define a relationship with the User model
    # user = db.relationship('User', backref=db.backref('prayer_requests', lazy=True))

    def __repr__(self):
        return f"<PrayerRequest {self.id}>"
    
    # save request
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete request
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=True)
    comment = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<Comment {self.id}>"
    
    # save comment
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete comment
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<Subcriber {self.email}>"
    
    # save subscriber
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete subscriber
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Inquiry(db.Model):
    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    inquiry = db.Column(db.String, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return f"<Inquiry {self.email}>"
    
    # save inquiry
    def save(self):
        db.session.add(self)
        db.session.commit()

    # delete inquiry
    def delete(self):
        db.session.delete(self)
        db.session.commit()

