from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://shareloc:shareloc@localhost/shareloc', echo=True)

Base = declarative_base()


class Lake(Base):
    __tablename__ = 'lake'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geometry('POLYGON'))


Lake.__table__.create(engine)
# Lake.__table__.drop(engine)


lake = Lake(name='Majeur', geom='POLYGON((0 0,4 9,11 22,0 0))')
Session = sessionmaker(bind=engine)

session = Session()
session.add(lake)
session.commit()