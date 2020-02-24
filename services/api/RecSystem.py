# services/api/RecSystem.py

from flask import Blueprint, request
from flask_restful import Resource, Api
from flask import jsonify
from services.utils.Predictor import Predictor
from services.utils import parse_data

RecSystem_blueprint = Blueprint('RecSystem', __name__)
api = Api(RecSystem_blueprint)

ctl = Predictor(
    model_pickled_path="./assets/model.pkl",
    dict_pickled_path="./assets/x5_dic.pkl"
)

# baseline
baseline = {
    "recommended_products": [
        "4009f09b04",
        "15ccaa8685",
        "bf07df54e1",
        "3e038662c0",
        "4dcf79043e",
        "f4599ca21a",
        "5cb93c9bc5",
        "4a29330c8d",
        "439498bce2",
        "343e841aaa",
        "0a46068efc",
        "dc2001d036",
        "31dcf71bbd",
        "5645789fdf",
        "113e3ace79",
        "f098ee2a85",
        "53fc95e177",
        "080ace8748",
        "4c07cb5835",
        "ea27d5dc75",
        "cbe1cd3bb3",
        "1c257c1a1b",
        "f5e18af323",
        "5186e12ff4",
        "6d0f84a0ac",
        "f95785964a",
        "ad865591c6",
        "ac81544ebc",
        "de25bccdaf",
        "f43c12d228",
    ]
}


class Status(Resource):
    def get(self):
        response_object = jsonify("OK")
        response_object.status_code = 200
        return response_object


class Recommend(Resource):
    def post(self):
        try:
            data = request.json
            user_id, user_frame = parse_data(data)
            products = user_frame["product_id"].to_list()
            if not products:
                return jsonify(baseline)
            else:
                predictions = [pred for pred in ctl.predict(products)]
                predictions = predictions + [
                    base_task
                    for base_task in baseline["recommended_products"]
                    if base_task not in predictions
                ]
                return jsonify({"recommended_products": predictions[:30]})
        except Exception as e:
            return jsonify(baseline)


api.add_resource(Recommend, '/recommend')
api.add_resource(Status, '/ready')
