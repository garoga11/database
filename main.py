from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
import db_config as database

app = Flask(__name__)
api = Api(app)

#all_data = database.db.Badge.find()


class Test(Resource):
    def get(self):
        pass


class Badge(Resource):

    def post(self):
        database.db.dbExample.insert_one(
            {
                'header_img_url': request.json['header_img_url'],
                'profile_picture_url': request.json['profile_picture_url'],
                'age': request.json['age'],
                'city': request.json['city'],
                'followers': request.json['followers'],
                'likes': request.json['likes'],
                'post': request.json['post'],
            }
        )


class AllBadge(Resource):
    """Get all badges"""

    def get(self):
        pass


api.add_resource(Badge, '/new')

if __name__ == '__main__':
    app.run(load_dotenv=True)
