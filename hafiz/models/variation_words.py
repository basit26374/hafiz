from hafiz.app import db


class VariationWords(db.Model):
    __tablename__ = 'variation_words'

    id = db.Column(db.Integer, primary_key=True)
    variation_id = db.Column(db.Integer, db.ForeignKey('variations.id'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('quran_word_text.id'), nullable=False)