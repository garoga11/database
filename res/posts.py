from flask import Flask, json, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
from werkzeug.wrappers import response
import db_config as database

class Posts(Resource):
    """handeling post behavior """

    def get(self, _id):
        response = self.abort_if_not_exist(_id)
        response ['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self, _id):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id)}, {"$push":{
            "posts":{
                "id": request.json["id"],
                "name": request.json["name"],
                "img": request.json["img"],
                "date": request.json["date"]
            }
        }})
        return jsonify({"message": f"The post {request.json['id']} was successfully created"})


    def put(self, _id, uuid):
        response= self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id":ObjectId(_id), "posts.id": uuid},
        {"$set":{
            "posts.$.name":request.json["name"],
            "posts.$.img":request.json["img"],
            "posts.$.date":request.json["date"]
        }}
        )

        return jsonify(request.json)

    def delete (self, _id, uuid):
        response = self.abort_if_not_exist(_id)

        database.db.Badges.update_one({"_id":ObjectId(_id)},
        {"$pull":{
            "posts":{"id":uuid}
        }})
        
        return jsonify({"message": f"The post with uuid {uuid} was successfully deleted."})

    def abort_if_not_exist(self, _id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {"name":1, "posts":1})

        if response:
            return response
        else:
            abort(jsonify({"status":404, "_id": f"{_id} not found"}))