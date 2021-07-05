from flask import request
from flask_restful import Resource
from flask_restful.utils import cors
import json
import math

from hafiz.app import db
from hafiz.models.quran_ayah_text import QuranAyahText
from hafiz.utils.serializers import ayah_serializer


class SurahData(Resource):

    @cors.crossdomain(methods={"HEAD", "OPTIONS", "GET"},
                      origin='*')
    def get(self, surah_number):
        limit, offset, page, total_pages = None, 0, 1, 1
        params = request.args.get('q')
        ayaah = QuranAyahText.query

        if params:
            params = json.loads(params)
            limit = params.get('limit')
            offset = params.get('offset')

        total_rec = ayaah.count()
        if not limit:
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)
        else:
            total_pages = math.ceil(total_rec / limit)
            page = int((offset / limit) + 1) if offset else 1
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)

        results = [ayah_serializer(ayah) for ayah in ayaah.items]

        # quran_ayaah = QuranAyahText.query.filter_by(
        #     surah_number=surah_number
        # ).all()

        return {
            'count': total_rec,
            'num_results': len(results),
            'objects': results,
            'page': page,
            'total_pages': total_pages
        }

        # return {"msg": "zappa app deployed",
        #         "status_code": 200
        #         }