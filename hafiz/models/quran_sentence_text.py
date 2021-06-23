from hafiz.app import db


class QuranSentenceText(db.Model):
    __table_name__ = 'quran_sentence_text'

    id = db.Column(db.Integer, primary_key=True)
    ayah_number = db.Column(db.Integer, nullable=False)
    surah_number = db.Column(db.Integer, nullable=False)
    sentence_seq = db.Column(db.Integer, nullable=False)
    sentence_arabic = db.Column(db.LargeBinary, nullable=False)
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=False)
