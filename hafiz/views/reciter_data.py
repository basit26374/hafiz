import datetime
from flask import request, jsonify
from flask_restful import Resource
from marshmallow import fields, Schema, validate

from hafiz.app import db


class ReciterData(Resource):

    def post(self):
        print(request.files)

        output = {
            'message': 'Object created successfully.',
            'resource_id': 1,
            'status_code': 201
        }
        return output, 201