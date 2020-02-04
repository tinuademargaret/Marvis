from flask import Flask
# from src.config.constants import Config
# from src.config.cors import *
from flask_socketio import SocketIO, emit

import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app)
# app.config.from_object(Config)

# APP_URL = "https://inventedu.herokuapp.com/"
# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# from src.app.services import database_service
