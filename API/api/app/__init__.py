from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from app.tools import JsonResp
# from jose import jwt
import os
import logging, sys

from app.routes.users import user_blueprint

class SingleLevelFilter(logging.Filter):
    def __init__(self, passlevel, reject):
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel)



def create_app():

    h1 = logging.StreamHandler(sys.stdout)
    f1 = SingleLevelFilter(logging.INFO, True)
    h1.addFilter(f1)
    rootLogger = logging.getLogger()
    rootLogger.addHandler(h1)
    rootLogger = logging.getLogger()

    logger = logging.getLogger("my.logger")
    logger.setLevel(logging.DEBUG)
    # logger.debug("A DEBUG message")
    # logger.info("An INFO message")
    # logger.warning("A WARNING message")
    # logger.error("An ERROR message")
    # logger.critical("A CRITICAL message")



    # Flask Config
    app = Flask(__name__)
    app.config.from_pyfile("config/config.cfg")

    # Database Config
    if app.config["ENVIRONMENT"] == "development":
        print("Development")
        # mongo = MongoClient(app.config["MONGO_HOSTNAME"], app.config["MONGO_PORT"])
        mongo = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
        logger.debug(os.environ['DB_PORT_27017_TCP_ADDR'])
        logger.debug(mongo.database_names())
        # mongo = MongoClient("mongodb://db:27017")
        
        
        app.db = mongo[app.config["MONGO_APP_DATABASE"]]
        logger.debug(app.db)
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
