from flask import Blueprint
from flask_restful import Api
from hafiz.views.save import SaveData

save_bp = Blueprint('save_bp', __name__)

save_api = Api(save_bp)
save_api.add_resource(SaveData, '/save')
