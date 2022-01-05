from flask import Flask
# from flask import request, session, redirect
# from flask_sqlalchemy import SQLAlchemy
import os
from . import config

def create_app():
    from . import models, fitbit
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    os.makedirs(config.SQLITE_DATABASE_LOCATION, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(config.SQLITE_DATABASE_LOCATION, config.SQLITE_DATABASE_NAME))

    models.init_app(app)
    fitbit.init_app(app)
    # services.init_app(app)
    return app

# app = create_app()