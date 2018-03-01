import binascii
import os

from extensions import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)

    @classmethod
    def find_by(cls, username, password):
        return User.query.filter_by(username=username, password=password).first()

    @classmethod
    def generate_token(cls):
        return binascii.b2a_hex(os.urandom(15)).decode("utf-8")

    def update_token(self):
        self.token = User.generate_token()
        db.session.commit()

    def save(self):
        self.token = User.generate_token()
        db.session.add(self)
        db.session.commit()
