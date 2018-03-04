import binascii
import os

from extensions import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = self.generate_token()

    @classmethod
    def find_by_username(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def find_by_tolen(cls, token):
        return User.query.filter_by(token=token).first()

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
        return self
