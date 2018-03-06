import json

from flask import Blueprint
from flask import request

from blueprints.authentication.models.user import User

from blueprints.user_location.models.user_location import UserLocation
from blueprints.user_location.schemas.location_schema import UpdateLocationRequestSchema
from lib.geojson.converter import to_feature_collection

user_location = Blueprint('user_location', __name__, url_prefix='/rest/location')

update_location_request_schema = UpdateLocationRequestSchema()


@user_location.route('/update', methods=['POST'])
def update_location():
    user_location_update_request = update_location_request_schema.load(request.json).data
    user = User.find_by_tolen(user_location_update_request.token)
    UserLocation.find_by_user_id(user.id).update_location(user_location_update_request.coordinates)
    return "Updated Successfully"


@user_location.route('/get/all', methods=['GET'])
def get_user_locations():
    user_locations = UserLocation.query.filter(UserLocation.location != None).all()
    feature_collection = to_feature_collection(user_locations)
    return json.dumps(feature_collection)
