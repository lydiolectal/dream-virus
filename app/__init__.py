from flask import Flask
from dotenv import load_dotenv
# import firebase_admin

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# firebase = firebase_admin.initialize_app()

from app import routes
