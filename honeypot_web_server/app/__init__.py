from flask import Flask, render_template
from config.config import Config
from config.secrets import SECRET_KEY
from logging_system.loggers.logger import honeypot_web_logger
from honeypot_web_server.app.routes import honeypot_routes

def create_app():
    app = Flask(__name__, template_folder="../templates")  
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(honeypot_routes)
    honeypot_web_logger()
    return app
