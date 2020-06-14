from flask import Flask
from api.config import Config
from api.speech.routes import speech

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(speech)
    return app
