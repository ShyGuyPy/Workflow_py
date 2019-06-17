from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

import os

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config.from_object(Config)

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')

#SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)


#models

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    res = db.Column(db.Integer)
    solids = db.Column(db.Integer)#Bool
    NTU = db.Column(db.Integer)#Bool
    org_mal = db.Column(db.Integer)#Bool
    MPN_100ml = db.Column(db.Integer)#Bool
    MPN_100ml_1 = db.Column(db.Integer)#Bool
    LosR = db.Column(db.Float)
    Silica = db.Column(db.Float)
    Ca = db.Column(db.Float)
    Mg = db.Column(db.Float)
    Ca_Mg = db.Column(db.Float)
    NO3 = db.Column(db.Float)
    NO3_USGS = db.Column(db.Float)
    Cl2 = db.Column(db.Float)
    Na = db.Column(db.Float)
    SO4 = db.Column(db.Float)
    K = db.Column(db.Float)
    pH = db.Column(db.Float)
    Alk = db.Column(db.Float)
    Hard = db.Column(db.Float)
    Nhard = db.Column(db.Float)
    C_USGSTemp = db.Column(db.Float)
    F_USGS = db.Column(db.Float)
    Temp = db.Column(db.Float)
    MD_Precip_inch_mon = db.Column(db.Float)
    MD_Temp_F = db.Column(db.Float)
