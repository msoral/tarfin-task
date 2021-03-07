from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DatabaseConfig as dbConfig

# Create globally accessible libraries
db = SQLAlchemy()


def init_app():
    # Create Flask Instance
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{dbConfig.dialect}+{dbConfig.driver}://{dbConfig.user}:" \
                                            f"{dbConfig.password}@{dbConfig.host}:{dbConfig.port}/{dbConfig.db}"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Initilize
    db.init_app(app)
    with app.app_context():
        # Include our resources
        from . import routes
        from . import models

        db.create_all()

        # Register Blueprints
        app.register_blueprint(routes.bp)

        return app

