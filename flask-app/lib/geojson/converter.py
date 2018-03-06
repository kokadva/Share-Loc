from geoalchemy2.shape import to_shape
from geojson import Feature
from geojson import FeatureCollection
from geojson.geometry import Point


def user_location_to_feature(user_location):
    coordinates = list(to_shape(user_location.location).coords)
    geometry = Point(coordinates=coordinates[0])
    properties = {'id': user_location.user_id}
    return Feature(geometry=geometry, properties=properties)


def to_feature_collection(user_locations):
    user_location_features = list(map(user_location_to_feature, user_locations))
    return FeatureCollection(user_location_features)
