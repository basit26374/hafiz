from hafiz.app import db


class Variations(db.Model):
    __table_name__ = 'variations'

    id = db.Column(db.Integer, primary_key=True)
    variation_number = db.Column(db.Integer, nullable=False)
    sentence_ids = db.Column(db.String(), nullable=False)
    word_ids = db.Column(db.ARRAY(db.Integer), nullable=False)
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=True)
