# services/api/RecSystem.py

from flask import Blueprint, request
from flask_restful import Resource, Api
from flask import jsonify

RecSystem_blueprint = Blueprint('RecSystem', __name__)
api = Api(RecSystem_blueprint)


class Status(Resource):
    def get(self):
        response_object = jsonify("OK")
        response_object.status_code = 200
        return response_object


class Recommend(Resource):
    def post(self):
        post_data = request.get_json()
        response_object = jsonify({
            'recommended_products': 'loh'
        })
        response_object.status_code = 200
        return response_object


api.add_resource(Recommend, '/recommend')
api.add_resource(Status, '/ready')
