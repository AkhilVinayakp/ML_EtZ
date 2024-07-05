import jwt
import datetime
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
# from werkzeug.security import check_password_hash

server = Flask(__name__)
server.debug = True

# MongoDB configuration
mongo_url = os.environ.get("MONGO_URL")
client = MongoClient(mongo_url)
db = client[os.environ.get("DATABASE")]
users_collection = db[os.environ.get("COLLECTION_NAME")]

@server.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hi welcome to ZZebra"})


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    # what we got from auth.
    print("auth received :", auth)
    if not auth:
        return "missing credentials", 401

    # Check database for username
    user = users_collection.find_one({"name": auth.username})

    if user:
        uname = user['name']
        password = user['password']  # Assuming password is hashed

        # Verify password
        if auth.username != uname or auth.password != password:
            return "invalid credentials", 401
        else:
            token = createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
            return jsonify({"token": token}), 200
    else:
        return "invalid credentials", 401

@server.route("/validate", methods=["POST"])
def validate():
    # should be a bearer token,
    encoded_jwt = request.headers.get("Authorization")

    if not encoded_jwt:
        return "missing credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            encoded_jwt, os.environ.get("JWT_SECRET"), algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return "expired token", 403
    except jwt.InvalidTokenError:
        return "not authorized", 403

    return jsonify(decoded), 200

def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
