# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Imports
from flask import Flask
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from json import dumps
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
from flask_jsonpify import jsonify
import bcrypt

#Local Modules
import db

#engine = create_engine('mysql://dbadmin:student@cr.cinestar-internal.lan/Cinestar', echo =True)
engine = create_engine('mysql://root:student@localhost/cinestar', echo = True)

Session = sessionmaker(bind=engine)

def createNewUser(jsondata):
    session = Session()

        
    user = jsondata['username']
    email = jsondata['email']
    pw =  jsondata['password']
        
    #first check if account with user unique
    if (session.query(exists().where(db.Users.email == email)).scalar()):
        return jsonify({"Message":"An account with this email already exists!"})
        
    #then check to see if username is unique
    if (session.query(exists().where(db.Users.username == user)).scalar()):
        return jsonify({"Message":"An account with this username azlready exists!"})
        
    #we can then prepare to create the account
        
    #first hash the password using bcrypt
    pw_salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw.encode('utf8'),pw_salt)

    new_user = db.Users(username = user, email = email, password = hashed, salt = pw_salt)
    session.add(new_user)
    session.commit()
        
    return jsonify({"Message":"Account created successfully! You Can now Log in"})


def doLogin(json_data):
    session = Session()
    
    user_name=json_data["username"]
    print (user_name)
    password_raw=json_data["password"]
    print (password_raw)
    
    
    #First Work out if the user exists
    if (session.query(exists().where(db.Users.username == user_name)).scalar()):
        
        print ("User Found")
        #We know the user Exists, so now we can check thier password
        for userID, password, salt, in session.query(db.Users).\
                              filter([db.Users.username]== user_name): 

            if bcrypt.checkpw(password_raw,password):
                #password is correct so we can return a user id.
                print ("we won") 
                return {"UserID":userID}
                

            else: 
                print ("pwd was wrong")
                return {"message":"Invalid username or password"}
        
    else:
        print("username was wrong")
        return {"message":"Invalid username or password"}
    
    print ("We dropped out the bottom for some reason")
    
    
    
