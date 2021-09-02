import datetime
import logging
from flask import request, jsonify
from flask_restful import Resource
from flask_restful.utils import cors
from marshmallow import fields, Schema, validate
from hafiz.models.reciter_info import ReciterInfo
from hafiz.models.recording_sentence import RecordingSentence

from hafiz.app import db


class ReciterData(Resource):

    @cors.crossdomain(methods={"HEAD", "OPTIONS", "POST"},
                      origin='*')
    def post(self):
        logging.info('------------------------------')
        logging.info(request.json)
        logging.info(request.files)
        print(request.files)
        print(request.args.get('hafiz_id'))

        # Add Recitor Info
        recitor_info = ReciterInfo(
            age=request.json('age'),
            location=request.json('location'),
            gender=request.json('gender')
        )
        db.session.add(recitor_info)
        db.session.commit()

        #Add Variation Info
        # for variation in request.json('variations'):
        #     variation = RecordingSentence(
        #         hafiz_id=
        #         audio_clarity=
        #         background_noise_level=
        #         with_tajweed=
        #         number_of_mistakes=
        #         mistakes=
        #         audio_format=
        #         recording_sentence=
        #         reciter_info_id=
        #         sentence_text_id=
        #     )

        output = {
            'message': 'Object created successfully.',
            'resource_id': 1,
            'status_code': 201
        }
        return output, 201