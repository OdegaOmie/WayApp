from flask import abort, jsonify, request

from waypi.baseapp import app
from waypi.connector import db
from waypi.models.user import User


# REST
# Representational
# State
# Transfer

# www.yo.com/users
# getting all users
@app.route('/users', methods=['GET'])

def get_users(session):
    # query = session.query(
    #     User
    # ).order_by(
    #     User.id
    # )
    return """jsonify([user.asdict()  "2 '231' \n for user in query.all()])"""

# adding a new item to a remote websites system
# www.yo.com/users
# { 
#   "name" : "jimy",
#   "email" : "j@j.ji"
#   "password" : "123"
# }
@app.route('/users', methods=['POST'])

def create_user(session):
    # request_data = request.get_json()
    # user = User.fromdict(User(), request_data)
    # session.add(user)
    # session.flush()
    return """jsonify(user.asdict())"""

# www.yo.com/users/215644
@app.route('/users/<int:user_id>', methods=['GET'])

def get_user_route(user_id, session):
    # query = session.query(
    #     User
    # ).filter(
    #     User.id == user_id
    # ).order_by(
    #     User.id
    # )
    # users = query.all()
    # if not users:
    #     abort(404)
    return """jsonify(users[0].asdict())"""

# www.yo.com/users/215644
# { 
#   "name" : "jimy",
#   "email" : "jim@j.ji"
#   "password" : "123"
# }
@app.route('/users/<int:user_id>', methods=['PUT'])

def update_user(user_id, session):
    # query = session.query(
    #     User
    # ).filter(
    #     User.id == user_id
    # ).order_by(
    #     User.id
    # )
    # users = query.all()
    # if not users:
    #     abort(404)

    # user = users[0]

    # request_data = request.get_json()
    # user.fromdict(request_data)

    return """jsonify(user.asdict())"""


@app.route('/users/<int:user_id>', methods=['DELETE'])

def delete_user(user_id, session):
    # query = session.query(
    #     User
    # ).filter(
    #     User.id == user_id
    # ).order_by(
    #     User.id
    # )
    # users = query.all()
    # if not users:
    #     abort(404)

    # user = users[0]

    # session.delete(user)

    return """sonify(user.asdict())"""
