from flask import Flask
from pymongo import MongoClient
from app.tools import JsonResp
# from jose import jwt
# import os


from app.routes.users import user_blueprint


def create_app():

    # Flask Config
    app = Flask(__name__)
    app.config.from_pyfile("config/config.cfg")

    # Database Config
    if app.config["ENVIRONMENT"] == "development":
        mongo = MongoClient(app.config["MONGO_HOSTNAME"], app.config["MONGO_PORT"])
        app.db = mongo[app.config["MONGO_APP_DATABASE"]]
    else:
        mongo = MongoClient("localhost")
        mongo[app.config["MONGO_AUTH_DATABASE"]].authenticate(
            app.config["MONGO_AUTH_USERNAME"], app.config["MONGO_AUTH_PASSWORD"]
        )
        app.db = mongo[app.config["MONGO_APP_DATABASE"]]

    # Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix="/user")

    # Index Route
    @app.route("/")
    def index():
        return JsonResp({"status": "Online"}, 200)

    return app
