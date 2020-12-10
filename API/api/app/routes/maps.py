from flask import Blueprint
# from flask import current_app as app

from app.auth import token_required
from app.models.map import Map

map_blueprint = Blueprint("map", __name__)


@map_blueprint.route("/", methods=["GET"])

def get():
    return Map().get()



@map_blueprint.route("/", methods=["POST"])
@token_required
def add():
    return Map().add()
