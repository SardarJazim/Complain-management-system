import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Configure Flask-SQLAlchemy for local database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Example URI for SQLite database (relative path)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'


from Api import models
from Api import views
