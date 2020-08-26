from flask import abort, jsonify, request
from bson import json_util

from waypi.baseapp import app
from waypi.connector import db

import json

@app.route("/test", methods=["GET"])
def test_get():
    collection = db["users"]
    users = json.loads(json_util.dumps(collection.find({})))
    return jsonify(users)


@app.route("/test", methods=["POST"])
def test_post():
    users = list()
    return jsonify([users])
