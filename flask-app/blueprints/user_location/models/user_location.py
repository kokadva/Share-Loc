from extensions import db
from lib.geometry_converter import to_geometry_point
from geoalchemy2 import Geometry


class UserLocation(db.Model):

    __tablename__ = 'user_locations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    location = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=True)

    def __init__(self, user_id, location=None):
        self.user_id = user_id
        self.location = location

    @classmethod
    def find_by_user_id(cls, user_id):
        return UserLocation.query.filter_by(user_id=user_id).first()

    def update_location(self, coordinates):
        point = to_geometry_point(coordinates)
        self.location = point
        db.session.commit()
        return self

    def save(self):
        db.session.add(self)
        db.session.commit()
