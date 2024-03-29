from blueprints.authentication.views import authentication_bluepring
from blueprints.drawing_geometry.views import drawing_geometry
from blueprints.ping.views import ping_bluepring
from blueprints.user_location.views import user_location
from extensions import ma, db, cors
from flask_app import app


def init_app():

    app.config.from_object('config.settings')

    init_extensions()
    init_blueprints()


def init_blueprints():
    app.register_blueprint(authentication_bluepring)
    app.register_blueprint(ping_bluepring)
    app.register_blueprint(user_location)
    app.register_blueprint(drawing_geometry)


def init_extensions():
    ma.init_app(app)
    db.init_app(app)
    cors.init_app(app)

if __name__ == '__main__':
    init_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()
    app.run(host='0.0.0.0', port=8000, debug=True)
