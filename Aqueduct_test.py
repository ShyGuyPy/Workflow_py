from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()



class Data(Base):
    __tablename__ = 'Aqueduct_test'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    year = Column(Integer)
    month = Column(Integer)
    res = Column(Float)
    solids = Column(Integer)#Bool
    NTU = Column(Integer)#Bool
    org_ml = Column(Integer)#Bool
    MPN_100ml = Column(Integer)#Bool
    MPN_100ml_1 = Column(Integer)#Bool
    LosR = Column(Float)
    Silica = Column(Float)
    Ca = Column(Float)
    Mg = Column(Float)
    Ca_Mg = Column(Float)
    NO3 = Column(Float)
    NO3_USGS = Column(Float)
    Cl2 = Column(Float)
    Na = Column(Float)
    SO4 = Column(Float)
    K = Column(Float)
    pH = Column(Float)
    Alk = Column(Float)
    Hard = Column(Float)
    Nhard = Column(Float)
    C_USGSTemp = Column(Float)
    F_USGS = Column(Float)
    Temp = Column(Float)
    MD_Precip_inch_mon = Column(Float)
    MD_Temp_F = Column(Float)

if __name__ == "__main__":
    t = time()

    engine = create_engine('sqlite:///data/Aqueduct_test.db')
    Base.metadata.create_all(engine)

    session = sessionmaker()
    session.configure(bind=engine)
    s = session()


try:

    file_name = "data/Reservoir_intake_retweaked.csv"
    data = Load_Data(file_name)

    print(data)


    for i in data:
        record = Data(**{
            'year' : i[1],
            'month' : i[2],
            'res' : i[3],
            'solids' : i[4],
            'NTU' : i[5],
            'org_ml' : i[6],
            'MPN_100ml' : i[7],
            'MPN_100ml_1' : i[8],
            'LosR' : i[9],
            'Silica' : i[10],
            'Ca' : i[11],
            'Mg' : i[12],
            'Ca_Mg' : i[13],
            'NO3' : i[14],
            'NO3_USGS' : i[15],
            'Cl2' : i[16],
            'Na' : i[17],
            'SO4' : i[18],
            'K' : i[19],
            'pH' : i[20],
            'Alk' : i[21],
            'Hard' : i[22],
            'Nhard' : i[23],
            'C_USGSTemp' : i[24],
            'F_USGS' : i[25],
            'Temp' : i[26],
            'MD_Precip_inch_mon' : i[27],
            'MD_Temp_F' : i[28]
        })
        s.add(record)

    s.commit()
    print("success")
except:
    s.rollback()
    print("no good")
finally:
    s.close()
    print("connection closed")
print("Time elapsed: " + str(time() - t) + " s.")
