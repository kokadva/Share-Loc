from flask import Blueprint

ping_bluepring = Blueprint('ping_bluepring', __name__)


@ping_bluepring.route('/ping', methods=['GET'])
def ping():
    return "Share-Loc", 200
