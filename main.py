from Flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
import db_config as database

app = Flask(__name__)

all_data = database.db.Badge.find()


if __name__ == '__main__':
    app.run(load_dotenv=True)
