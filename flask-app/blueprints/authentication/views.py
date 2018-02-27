from flask import Blueprint

authentication_bluepring = Blueprint('authentication', __name__, url_prefix='/rest-auth')


@authentication_bluepring.route('/login', methods=['POST'])
def login():
    return "Login"


@authentication_bluepring.route('/logout', methods=['POST'])
def logout():
    pass


@authentication_bluepring.route('/register', methods=['POST'])
def register():
    pass
