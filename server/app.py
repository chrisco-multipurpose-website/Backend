from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db, User, TokenBlocklist
from blueprints.auth import auth_bp
from blueprints.users import user_bp
from blueprints.services import service_bp
from blueprints.churchinfo import churchinfo_bp
from blueprints.events import event_bp
from blueprints.about_us import about_bp
from blueprints.departments import department_bp
from blueprints.swagger import swaggerui_bp
from blueprints.youtube import youtube_bp
from blueprints.spotify import spotify_bp
from blueprints.sliders import slider_bp
from blueprints.blogs import blog_bp
from blueprints.profile import profile_bp
from blueprints.prayer_request import prayer_request_bp
from blueprints.comments import comment_bp
from blueprints.inquiry import inquiry_bp
from blueprints.subscription import subscription_bp
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = '5f8e5e934051cdfb322c0619'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///church.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Connecting with react
CORS(app)

# Initialize app with db, migrate
migrate = Migrate(app, db)
jwt = JWTManager(app)
db.init_app(app)

# register blueprints
app.register_blueprint(swaggerui_bp, url_prefix="/swagger")
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(service_bp, url_prefix='/services')
app.register_blueprint(churchinfo_bp, url_prefix='/churchinfo')
app.register_blueprint(event_bp, url_prefix='/events')
app.register_blueprint(about_bp, url_prefix='/about')
app.register_blueprint(department_bp, url_prefix='/departments')
app.register_blueprint(youtube_bp, url_prefix='/youtube')
app.register_blueprint(spotify_bp, url_prefix='/spotify')
app.register_blueprint(slider_bp, url_prefix='/sliders')
app.register_blueprint(blog_bp, url_prefix='/blogs')
app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(prayer_request_bp, url_prefix='/requests')
app.register_blueprint(comment_bp, url_prefix='/comments')
app.register_blueprint(inquiry_bp, url_prefix='/inquiries')
app.register_blueprint(subscription_bp, url_prefix='/subscriptions')

# load user
@jwt.user_lookup_loader
def user_looup_callback(jwt_header, jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(email=identity).one_or_none()


# jwt error handlers
# expired token handler
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify(
        {
            "message": "Token has expired",
            "error": "token_expired"
        }
    ), 401

# invalid token loader
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(
        {
            "message": "Signature verification failed",
            "error": "invalid_token"
        }
    ), 401

# unauthorized token loader (when token is not provided)
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify(
        {
            "message": "Request doesn't contain a valid token",
            "error": "authorization_header"
        }
    ), 401


# revoking tokens >> logout
@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
    jti = jwt_data['jti']
    
    token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

    return token is not None



if __name__== '__main__':
    app.run(port=5555, debug=True)