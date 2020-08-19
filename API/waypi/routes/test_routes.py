from flask import abort, jsonify, request
from bson import json_util

from waypi.baseapp import app
from waypi.connector import db

import json
from bson import ObjectId




@app.route('/test', methods=['GET'])
def test_get():
    collection = db["users"]
    users = json.loads m ,     ,,zssssssssssss4 (json_util.dumps(collection.find({})))
    return jsonify(users)



@app.route('/test', methods=['POST'])
def test_post():
    users = list()
    return jsonify([user])


