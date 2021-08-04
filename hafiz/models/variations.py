from hafiz.app import db


class Variations(db.Model):
    __tablename__ = 'variations'

    id = db.Column(db.Integer, primary_key=True)
    variation_number = db.Column(db.Integer, nullable=False)
    sentence_ids = db.Column(db.String(), nullable=False)
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=True)
    words = db.relationship('QuranWordText', secondary='variation_words', backref=db.backref('variations'))
