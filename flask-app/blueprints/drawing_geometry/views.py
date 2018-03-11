from flask import Blueprint
from flask import request

from blueprints.authentication.models.user import User
from blueprints.drawing_geometry.models.geometry_drawing import GeometryDrawing
from blueprints.drawing_geometry.schemas.geometry_drawing_schema import GeometryDrawingUploadRequestSchema

from lib.geometry_converter import to_geometry_polygon

drawing_geometry = Blueprint('drawing_geometry', __name__, url_prefix='/rest/drawing')

geometry_drawing_upload_request_schema = GeometryDrawingUploadRequestSchema()


@drawing_geometry.route('/upload', methods=['POST'])
def update_location():
    new_polygon_create_schema = geometry_drawing_upload_request_schema.load(request.json).data
    geometry = to_geometry_polygon(new_polygon_create_schema.coordinates)
    user = User.find_by_tolen(new_polygon_create_schema.token)
    GeometryDrawing(user.id, geometry).save()
    return "Upload Successfully"
