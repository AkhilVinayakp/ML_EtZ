import jwt, os, datetime
from flask import Flask, request
from pymongo import MongoClient

server = Flask(__name__)
mongoclient = MongoClient(os.environ.get("MONGO_URL"))
db = mongoclient[os.environ.get("DATABASE")]
collection = db[os.environ.get("COLLECTION_NAME")]

# creating the first route for login
@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401
    