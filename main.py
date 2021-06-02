from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
from werkzeug.wrappers import response
import db_config as database

#resourses
from res.badge import Badge
from res.badges import Badges

app = Flask(__name__)
api = Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age': {"$gte": "21"}}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/proyection')
def get_name_and_age():
    response = list(database.db.Badges.find({'age': {"$gte" : "21"}}, {'name':"1", 'age':"1"}))
        
    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/kids')
def get_kids():
    response = list(database.db.Badges.find({'age': {"$gte" : "12"}}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/names')
def get_names():
    response = list(database.db.Badges.find({},{'name': "1"}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)


api.add_resource(Badge, '/new/', '/<string:by>=<string:data>/')
api.add_resource(Badges, '/all/', '/delete/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)


