# services/__init__.py

import os

from flask import Flask
from services.api.RecSystem import RecSystem_blueprint


def create_app(script_info=None):
    app = Flask(__name__)
    # config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.register_blueprint(RecSystem_blueprint)

    return app
