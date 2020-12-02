from flask import current_app as app
from flask import request
from jose import jwt
from app import tools
import json


class Map:
    def __init__(self):
        self.defaults = {
            "id": tools.randID(),
            "name": "",
            "map_active": True,
            "date_created": tools.nowDatetimeUTC(),
            "county": "",
            "co_ordinate_start": {},
            "co_ordinate_end": {},
        }

    def get(self):
        # token_data = jwt.decode(
        #     request.headers.get("AccessToken"), app.config["SECRET_KEY"]
        # )
        print(request)
        print(request.args)
        if "id" in request.args:
            id = request.args["id"]
            map = app.db.maps.find_one("id": id)
            
        else:
            resp = tools.JsonResp({"message": "User not found"}, 404)
        # print(args)
        # print(json.load(id))
        # map = app.db.maps.find_one(
        #     {"name": token_data["name"]}, {"_id": 0, "password": 0}
        # )

        if user:
            resp = tools.JsonResp(map, 200)
        else:
            resp = tools.JsonResp({"message": "User not found"}, 404)

        return resp

    def add(self):
        data = json.loads(request.data)

        expected_data = {
            "name": data["name"],
            "county": data["county"],
            "co_ordinate_start": data["co_ordinate_start"],
            "co_ordinate_end": data["co_ordinate_end"],
        }

        # Merge the posted data with the default user attributes
        self.defaults.update(expected_data)
        map = self.defaults

        # Make sure there isn"t already a map with this name
        existing_map = app.db.maps.find_one({"name": map["name"]})

        if existing_map:
            resp = tools.JsonResp(
                {
                    "message": "There's already an map with this name",
                    "error": "email_exists",
                },
                400,
            )

        else:
            if app.db.maps.save(map):
                resp = tools.JsonResp(
                    {
                        "id": map["id"],
                        "name": map["name"],
                        "county": map["county"],
                        "co_ordinate_start": map["co_ordinate_start"],
                        "co_ordinate_end": map["co_ordinate_end"],
                    },
                    200,
                )

            else:
                resp = tools.JsonResp(
                    {"message": "User could not be added"}, 400)

        return resp
