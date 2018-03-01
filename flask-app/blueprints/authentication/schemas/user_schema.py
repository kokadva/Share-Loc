from marshmallow import Schema
from marshmallow import post_load
from marshmallow.fields import String


class LoginRequestModel(object):

    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password


class LoginRequestSchema(Schema):

    username = String()
    password = String()

    @post_load
    def make_user(self, data):
        return LoginRequestModel(**data)


class LoginResponseSchema(Schema):

    token = String()

