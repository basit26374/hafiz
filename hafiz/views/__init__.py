from flask import Blueprint
from flask_restful import Api
from hafiz.views.reciter_data import ReciterData
from hafiz.views.surah import SurahData
from hafiz.views.surah import AyahVariation
from hafiz.views.surah import WordsVariation

reciter_data_bp = Blueprint('reciter_data_bp', __name__)
surah_bp = Blueprint('surah_bp', __name__)
ayah_variation_bp = Blueprint('ayah_variation_bp', __name__)
word_variation_bp = Blueprint('word_variation_bp', __name__)

reciter_data_api = Api(reciter_data_bp)
reciter_data_api.add_resource(ReciterData, '/reciter_data')

surah_api = Api(surah_bp)
surah_api.add_resource(SurahData, '/surah/<surah_number>')

ayah_variation_api = Api(ayah_variation_bp)
ayah_variation_api.add_resource(AyahVariation, '/ayah/<ayah_id>')

word_variation_api = Api(word_variation_bp)
word_variation_api.add_resource(WordsVariation, '/word/<variation_id>')