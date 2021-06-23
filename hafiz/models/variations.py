from hafiz.app import db


class Variations(db.Model):
    __table_name__ = 'variations'

    id = db.Column(db.Integer, primary_key=True)
    is_variation = db.Column(db.Boolean, nullable=False)
    ayaah_variations = db.Column(db.JSON, nullable=True)
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=True)
