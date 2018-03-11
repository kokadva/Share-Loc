from marshmallow import Schema, post_load
from marshmallow.fields import String, List, Decimal


class GeometryDrawingUploadRequestModel(object):

    token = ""
    coordinates = None

    def __init__(self, token, coordinates):
        self.token = token
        self.coordinates = coordinates


class GeometryDrawingUploadRequestSchema(Schema):

    token = String()
    coordinates = List(List(Decimal()))

    @post_load
    def make_geometry_drawing_model(self, data):
        return GeometryDrawingUploadRequestModel(**data)
