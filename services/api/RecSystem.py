# services/api/RecSystem.py

from flask import Blueprint, request
from flask_restful import Resource, Api
from flask import jsonify
from services.utils.Predictor import Predictor

RecSystem_blueprint = Blueprint('RecSystem', __name__)
api = Api(RecSystem_blueprint)

ctl = Predictor(
    product_csv_path="../assets/products.csv",
    model_pickled_path="../assets/model.pkl"
)


class Status(Resource):
    def get(self):
        response_object = jsonify("OK")
        response_object.status_code = 200
        return response_object


class Recommend(Resource):
    def post(self):
        r = request.json
        recs = ctl.predict(r.get("transaction_history", []))[:30]
        response_object = jsonify({
            'recommended_products': recs
        })
        response_object.status_code = 200
        return response_object


api.add_resource(Recommend, '/recommend')
api.add_resource(Status, '/ready')
