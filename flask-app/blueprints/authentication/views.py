from flask import Blueprint, jsonify
from flask import make_response
from flask import request

from blueprints.authentication.models.user import User
from blueprints.authentication.schemas.user_schema import LoginRequestSchema, LoginResponseSchema

authentication_bluepring = Blueprint('authentication', __name__, url_prefix='/rest-auth')


login_response_schema = LoginResponseSchema()
login_request_schema = LoginRequestSchema()


@authentication_bluepring.route('/login', methods=['POST'])
def login():
    login_request = login_request_schema.load(request.json).data
    user = User.find_by_username(login_request.username)
    if user is None:
        User(login_request.username, login_request.password).save()
        return jsonify(login_response_schema.dump(user).data)
    if user.password != login_request.password:
        return make_response(jsonify({'message': 'Password is incrorrect'}), 401)
    user.update_token()
    return jsonify(login_response_schema.dump(user).data)


@authentication_bluepring.route('/logout', methods=['POST'])
def logout():
    pass


@authentication_bluepring.route('/register', methods=['POST'])
def register():
    pass
