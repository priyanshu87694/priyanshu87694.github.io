from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SECRET_KEY'] = "8578beb4682fdba76d3bfb6f"
db = SQLAlchemy(app)

from app import routes
from app import models