from flask import Blueprint
from flask import request

from blueprints.authentication.models.user import User

from blueprints.user_location.models.user_location import UserLocation
from blueprints.user_location.schemas.location_schema import UpdateLocationRequestSchema

user_location = Blueprint('user_location', __name__, url_prefix='/rest/location')

update_location_request_schema = UpdateLocationRequestSchema()


@user_location.route('/update', methods=['POST'])
def update_location():
    user_location_update_request = update_location_request_schema.load(request.json).data
    user = User.find_by_tolen(user_location_update_request.token)
    UserLocation.find_by_user_id(user.id).update_location(user_location_update_request.coordinates)
    return "Updated Successfully"
