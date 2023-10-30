from flask import Flask
from .config import config

#flask application factory function
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])

    from src.app.main.views import main 
    app.register_blueprint(main,url_prefix='/main')
    return app