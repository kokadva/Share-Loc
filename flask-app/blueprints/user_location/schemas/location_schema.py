from marshmallow import Schema, post_load
from marshmallow.fields import String, List, Decimal


class UserLocationUpdateRequestModel(object):

    token = ""
    coordinates = None

    def __init__(self, token, coordinates):
        self.token = token
        self.coordinates = coordinates


class UpdateLocationRequestSchema(Schema):

    token = String()
    coordinates = List(Decimal())

    @post_load
    def make_user_location(self, data):
        return UserLocationUpdateRequestModel(**data)
