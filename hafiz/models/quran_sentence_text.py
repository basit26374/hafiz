from hafiz.app import db


class QuranSentenceText(db.Model):
    __table_name__ = 'quran_sentence_text'

    id = db.Column(db.Integer, primary_key=True)
    ayah_number = db.Column(db.Integer, nullable=False)
    surah_number = db.Column(db.Integer, nullable=False)
    sentence_seq = db.Column(db.Integer, nullable=False)
    sentence_arabic = db.Column(db.LargeBinary, nullable=False)
    sentence_indo_pak = db.Column(db.LargeBinary)
    sentence_uthmani = db.Column(db.LargeBinary)
    english_transliteration = db.Column(db.String())
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=False)
