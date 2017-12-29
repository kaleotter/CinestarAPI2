# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from flask import Flask, request
from requests import put, get
from flask_restful import Resource, Api, abort, fields, marshal_with, reqparse
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from json import dumps
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser
from flask_jsonpify import jsonify
import bcrypt


#internal modules
import db
import userView

app = Flask(__name__)
api = Api(app)

#engine = create_engine('mysql://dbadmin:student@cr.cinestar-internal.lan/Cinestar', echo =True)
engine = create_engine('mysql://root:student@localhost/cinestar', echo = True)

Session = sessionmaker(bind=engine)

class Movies(Resource):
    def get(self):
        query = conn.execute("SELECT * FROM Movies")
        result = {'data': [dict(zip(tuple (query.keys()),i)) for i in query.cursor]}
        # dict() builds an key data referenced array? Sorta like a pk in a database? See https://docs.python.org/2/tutorial/datastructures.html 5.5)
        # zip() not quite sure I understand this. Ask Typh for help? https://docs.python.org/3.3/library/functions.html#zip
        # tuple() like a list but non dynamic. Can't add or remove without rebuilding it from scratch? http://www.tutorialspoint.com/python/tuple_tuple.htm
        return jsonify(result)
#        return {'movieID':[i[0] for i in query.cursor.fetchall()]}
    
    
class MovieSearchTest (Resource):
    args = {
        'id': fields.Int(
            required =True,
            ),
        }

    @use_kwargs(args)
    
    def get (self, id):
        conn = utils.DbConn.conn().connect()
        query = conn.execute("SELECT * FROM Movies WHERE MovID=%d" %int(id))
        result = {'data': [dict(zip(tuple (query.keys()),i)) for i in query.cursor]}
        # dict() builds an key data referenced array? Sorta like a pk in a database? See https://docs.python.org/2/tutorial/datastructures.html 5.5)
        # zip() not quite sure I understand this. Ask Typh for help? https://docs.python.org/3.3/library/functions.html#zip
        # tuple() like a list but non dynamic. Can't add or remove without rebuilding it from scratch? http://www.tutorialspoint.com/python/tuple_tuple.htm
        return jsonify(result)
    
class MovieId (Resource):
    def get (self,id):
        conn = utils.DbConn.conn().connect()
        query = conn.execute("SELECT * FROM movies WHERE MovID=%d" %int(id))
        result ={'data': [dict(zip(tuple (query.keys()),i)) for i in query.cursor]}
        
        if query != null:               #if the query contains data
            return jsonify(result)
        
        else:
            return jsonify("some kind of error")
            
    
    class MovieReviews(Resource):
        def get(self,MovId):
            
            return jsonify(result)
        



app = Flask(__name__)
api = Api(app)

class Users (Resource):
    def post(self):                #create an acccount
    
        json_data = request.get_json(force=True)
        output = userView.createNewUser(json_data)
        
        return(output)

            
class Login (Resource):
    def post (self):

        json_data = request.get_json(force=True)
        
        response_data = userView.doLogin(json_data)
        
        if response_data == {"message":"Invalid username or password"}:
            print ("we got to an invalid user/pass")

            return (response_data), 403 
        else:
            print ("we got to a valid user/pass")
            return (response_data)

#AAAAAAAH I COMMENTED THIS OUT.     
api.add_resource(Movies, '/Movies')
api.add_resource(MovieId, '/Movies/<movie_ID>')
api.add_resource(MovieSearchTest, '/test', endpoint='test')
api.add_resource(Users, '/users')
api.add_resource(Login, '/users/login')
    
if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')
