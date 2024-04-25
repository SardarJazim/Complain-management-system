from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)
from Api import app
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User_Details(db.Model):
    # user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),primary_key=True)
    password = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email
        self.password = password


class User_DetailsSchema(ma.Schema):
    class Meta:
        fields = ( 'email', 'password')


class User_Complains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(120))
    text = db.Column(db.String(1000))
    category = db.Column(db.String(120))

    def __init__(self,email,text,category):
        self.email = email
        self.text = text
        self.category=category
    
class User_Complains_Schema(ma.Schema):
    class Meta:
        fields = ('id','email','text','category')




    with app.app_context():
        print("alala")
        db.create_all()
