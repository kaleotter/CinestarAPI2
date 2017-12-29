from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.types import DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import *

#engine = create_engine('mysql://accessusr:Student@192.168.0.64/CineStarMain', echo = True)
engine = create_engine('mysql://root:student@localhost/cinestar', echo = True)

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    
    userID = Column(Integer, primary_key = True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(BLOB)
    salt = Column(BLOB)
    
    
    def __repr__(self):
        return "<Users( userID = '%s',username='%s', email='%s', password='%s', salt=%s)>" % (
                        self.userID,
                        self.username, 
                        self.email, 
                        self.password,
                        self.salt)
    


    
class Movies (Base):
    __tablename__ ='Movies'
    
    MovieID = Column(Integer, primary_key=True)
    Title = Column(String) 
    Year = Column(YEAR(4))
    Certification = Column(String(45))
    Release_date = Column(DATETIME)
    Runtime = Column(String())
    Genres = Column(String(1000)) 
    Directors = Column(String(1000)) 
    Writers = Column(String(1000)) 
    Actors = Column(String(1000)) 
    Synopsis = Column(String(5000)) 
    languages = Column(String(500)) 
    Country = Column(String(70)) 
    Awards = Column(String(500)) 
    Poster_URL = Column(String(1000)) 
    IMDBRating = Column (DECIMAL(1,0)) 
    MetaScore =Column(DECIMAL(1,0)) 
    Type = Column(String(50)) 
    DVD =Column(DATE)
    Website = Column(String(500))
    
    def  __repr__(self):
        return "<Movies (Title='%s',Year='%s',Certification='%s',Release_date='%s',Runtime='%s',Genres='%s',Directors='%s',Writers='%s', Actors='%s', Synopsis='%s', languages='%s', Country='%s',Awards='%s',Poster_URL='%s',IMDBRating='%s', MetaScore='%s',Type='%s',DVD='%s',Website='%s')>" % (
                self.Title,
                self.Year,
                self.Certification,
                self.Release_date,
                self.Runtime,
                self.Genres,
                self.Directors,
                self.Writers,
                self.Actors,
                self.Synopsis,
                self.languages,
                self.Country,
                self.Awards,
                self.Poster_URL,
                self.IMDBRating,
                self.MetaScore,
                self.Type,
                Self.DVD,
                Self.Website
                )