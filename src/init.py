from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv
# Modules from this project
from generate_key import generate_key_if_not_exist

# Initialize Flask app
app = Flask(__name__)
generate_key_if_not_exist('.env')
load_dotenv()
app.secret_key = getenv('SECRET_KEY')
# Initialize db
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
db = SQLAlchemy(app)
