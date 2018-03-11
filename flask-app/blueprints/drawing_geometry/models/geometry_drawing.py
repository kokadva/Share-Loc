from extensions import db
from geoalchemy2 import Geometry


class GeometryDrawing(db.Model):

    __tablename__ = 'geometry_drawings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    geometry = db.Column(Geometry(geometry_type='POLYGON', srid=4326), nullable=True)

    def __init__(self, user_id, geometry=None):
        self.user_id = user_id
        self.geometry = geometry

    @classmethod
    def find_by_user_id(cls, user_id):
        return GeometryDrawing.query.filter_by(user_id=user_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
