from hafiz.app import db


class QuranSentenceText(db.Model):
    __table_name__ = 'quran_sentence_text'

    id = db.Column(db.Integer, primary_key=True)
    sentence_seq = db.Column(db.Integer, nullable=False)
    sentence_arabic = db.Column(db.JSON, nullable=False)
    sentence_indo_pak = db.Column(db.JSON)
    sentence_uthmani = db.Column(db.JSON)
    english_transliteration = db.Column(db.String())
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=False)
