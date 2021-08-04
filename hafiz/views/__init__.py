from flask import Blueprint
from flask_restful import Api
from hafiz.views.reciter_data import ReciterData
from hafiz.views.surah import SurahNumber
from hafiz.views.surah import SurahName
from hafiz.views.surah import AyahVariation
from hafiz.views.surah import WordsVariation

reciter_data_bp = Blueprint('reciter_data_bp', __name__)
surah_number_bp = Blueprint('surah_number_bp', __name__)
surah_name_bp = Blueprint('surah_name_bp', __name__)
ayah_variation_bp = Blueprint('ayah_variation_bp', __name__)
word_variation_bp = Blueprint('word_variation_bp', __name__)

reciter_data_api = Api(reciter_data_bp)
reciter_data_api.add_resource(ReciterData, '/reciter_data')

surah_number_api = Api(surah_number_bp)
surah_number_api.add_resource(SurahNumber, '/surah_number/<surah_number>')

surah_name_api = Api(surah_name_bp)
surah_name_api.add_resource(SurahName, '/surah_name/<surah_name>')

ayah_variation_api = Api(ayah_variation_bp)
ayah_variation_api.add_resource(AyahVariation, '/ayah/<ayah_id>')

word_variation_api = Api(word_variation_bp)
word_variation_api.add_resource(WordsVariation, '/word/<variation_id>')