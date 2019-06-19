from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

from numpy import genfromtxt

import os

#basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config.from_object(Config)
#app.comfig['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C/Users/icprbadmin/Documents/Python_Scripts/Workflow_py/test.db'

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


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

file_name = "data/Reservoir_intake_retweaked.csv"
data = Load_Data(file_name)

#this needs to be adapted to flask-migrate structure
for i in data:
    record = Data(**{
        'year': i[1],
        'month': i[2],
        'res': i[3],
        'solids': i[4],
        'NTU': i[5],
        'org_ml': i[6],
        'MPN_100ml': i[7],
        'MPN_100ml_1': i[8],
        'LosR': i[9],
        'Silica': i[10],
        'Ca': i[11],
        'Mg': i[12],
        'Ca_Mg': i[13],
        'NO3': i[14],
        'NO3_USGS': i[15],
        'Cl2': i[16],
        'Na': i[17],
        'SO4': i[18],
        'K': i[19],
        'pH': i[20],
        'Alk': i[21],
        'Hard': i[22],
        'Nhard': i[23],
        'C_USGSTemp': i[24],
        'F_USGS': i[25],
        'Temp': i[26],
        'MD_Precip_inch_mon': i[27],
        'MD_Temp_F': i[28]
    })

#print(record)