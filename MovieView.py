from flask import Flask
from flask_restful import abort
from sqlalchemy import create_engine, exists, func
from sqlalchemy.orm import sessionmaker
from json import dumps
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
from flask_jsonpify import jsonify

import db

#engine = create_engine('mysql://dbadmin:student@cr.cinestar-internal.lan/Cinestar', echo =True)
engine = create_engine('mysql://root:student@localhost/cinestar')

Session = sessionmaker(bind=engine)



def movSearch(queryArgs):

    print ("we started movSearch")
    session=Session()
    containsexact=False
    exactmatch={'0'}


    #first, check if anything even similar exists in the db. 

    if session.query(exists().where(func.lower(db.Movies.Title.like(func.lower(queryArgs['movie']))))).scalar():
        print ("we found similar")
        similar = session.query(db.Movies).filter(func.lower([db.Movies.Title.like(func.lower(queryArgs['movie']))]))

        #check for an exact match
        if session.query(exists().where(func.lower(db.Movies.Title)==func.lower(queryArgs['movie']))).scalar():
            containsexact = True
            print ("an exact match was found")
     
            return ({"status":"1"}) 

    else: #we found exactly nothing
        
        return({"status":'0'})

    