from flask import Blueprint
from flask_restful import Api
from hafiz.views.save import SaveData
from hafiz.views.surah import SurahData

save_bp = Blueprint('save_bp', __name__)
surah_bp = Blueprint('surah_bp', __name__)

save_api = Api(save_bp)
save_api.add_resource(SaveData, '/save')

surah_api = Api(surah_bp)
surah_api.add_resource(SurahData, '/surah/<surah_number>')