from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, current_user, get_jwt_identity
from models import User, TokenBlocklist

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    user = User.get_user_by_email(email=data.get('email' ))

    if user is not None:
        return jsonify({"error": "User already exists"}), 403
    
    new_user = User(
        firstname = data.get('firstname'),
        lastname = data.get('lastname'),
        email = data.get('email')
    )
    new_user.set_password(password=data.get("password"))

    new_user.save()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
     data = request.get_json()

     user = User.get_user_by_email(email=data.get('email'))

     if user and (user.check_password(password=data.get('password'))):
         access_token = create_access_token(identity=user.email)
         refresh_token = create_refresh_token(identity=user.email)

         return jsonify(
             {
                 "message":"Logged In",
                 "tokens": {
                     "access": access_token,
                     "refresh": refresh_token
                 }
             }
         ), 200
     
     return jsonify({"error": "Invalid email or password"}), 400

@auth_bp.route('/whoami', methods=['GET'])
@jwt_required()
def whoami():
    return jsonify(
        {
            "user_details" : {
                "username": current_user.username,
                "email": current_user.email
            }
        }
    )

@auth_bp.route('/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refresh_access():
    identity = get_jwt_identity()
    new_access_token = create_access_token(identity=identity)

    return jsonify({"access_token": new_access_token})

@auth_bp.route('/logout', methods=['GET'])
@jwt_required(verify_type=False)
def logout_user():
    jwt = get_jwt()

    jti = jwt['jti']
    token_type = jwt['type']

    token_b = TokenBlocklist(jti = jti)
    token_b.save()

    return jsonify({"message": f"{token_type} token revoked successfully"}), 200

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()

    email = data.get('email')
    new_password = data.get('new_password')

    user = User.get_user_by_email(email=email)

    if user is None:
        return jsonify({"error": "User does not exist"}), 404

    # Update the password for the user
    user.set_password(password=new_password)
    user.save()

    return jsonify({"message": "Password reset successfully"}), 200