from flask import request
from flask_restful import Resource
from flask_restful.utils import cors
import json
import math

from hafiz.app import db
from hafiz.models.quran_ayah_text import QuranAyahText
from hafiz.models.variations import Variations
from hafiz.models.quran_word_text import QuranWordText
from hafiz.models.variation_words import VariationWords
from hafiz.utils.serializers import ayah_serializer, variation_serializer, words_serializer


class SurahNumber(Resource):

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

        ayaah = ayaah.filter(QuranAyahText.surah_number==surah_number)

        total_rec = ayaah.count()
        if not limit:
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)
        else:
            total_pages = math.ceil(total_rec / limit)
            page = int((offset / limit) + 1) if offset else 1
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)

        results = [ayah_serializer(ayah) for ayah in ayaah.items]

        return {
            'count': total_rec,
            'num_results': len(results),
            'objects': results,
            'page': page,
            'total_pages': total_pages
        }


class SurahName(Resource):

    @cors.crossdomain(methods={"HEAD", "OPTIONS", "GET"},
                      origin='*')
    def get(self, surah_name):
        limit, offset, page, total_pages = None, 0, 1, 1
        params = request.args.get('q')
        ayaah = QuranAyahText.query

        if params:
            params = json.loads(params)
            limit = params.get('limit')
            offset = params.get('offset')

        ayaah = ayaah.filter(QuranAyahText.surah_name==surah_name)

        total_rec = ayaah.count()
        if not limit:
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)
        else:
            total_pages = math.ceil(total_rec / limit)
            page = int((offset / limit) + 1) if offset else 1
            ayaah = ayaah.paginate(page=page, per_page=limit, error_out=False)

        results = [ayah_serializer(ayah) for ayah in ayaah.items]

        return {
            'count': total_rec,
            'num_results': len(results),
            'objects': results,
            'page': page,
            'total_pages': total_pages
        }


class AyahVariation(Resource):

    @cors.crossdomain(methods={"HEAD", "OPTIONS", "GET"},
                      origin='*')
    def get(self, ayah_id):
        variations = Variations.query.filter(Variations.ayah_text_id==ayah_id)
        
        results = [variation_serializer(variation) for variation in variations]

        return {
            'num_results': len(results),
            "objects": results,
            "status_code": 200
        }


class WordsVariation(Resource):

    @cors.crossdomain(methods={"HEAD", "OPTIONS", "GET"},
                      origin='*')
    def get(self, variation_id):

        # variation_record = Variations.query.filter(Variations.id == variation_id).first()

        # words = QuranWordText.query.join(
        #     VariationWords, QuranWordText.id == VariationWords.word_id).join(
        #     Variations, VariationWords.variation_id == Variations.id).add_columns(
        #         QuranWordText.id, QuranWordText.word_arabic).filter(
        #             Variations.id == variation_id).all()

        word_object = db.session.execute(f'select qwt.id, qwt.word_arabic from variations v join variation_words vw on vw.variation_id = v.id join quran_word_text qwt on qwt.id = vw.word_id where v.id = {variation_id}')

        results = [words_serializer(word) for word in word_object]

        return {
            'num_results': len(results),
            "objects": results,
            "status_code": 200
        }
