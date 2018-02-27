from blueprints.authentication.views import authentication_bluepring
from blueprints.ping.views import ping_bluepring
from extensions import marshmallow, db
from flask_app import app


def init_app():

    app.config.from_object('config.settings')

    init_extensions()
    init_blueprints()


def init_blueprints():
    app.register_blueprint(authentication_bluepring)
    app.register_blueprint(ping_bluepring)


def init_extensions():
    marshmallow.init_app(app)
    db.init_app(app)

if __name__ == '__main__':
    init_app()
    app.run(host='0.0.0.0', port=8000, debug=True)
