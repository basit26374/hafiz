from hafiz.app import db


class QuranWordText(db.Model):
    __table_name__ = 'quran_word_text'

    id = db.Column(db.Integer, primary_key=True)
    word_seq = db.Column(db.Integer, nullable=False)
    surah_number = db.Column(db.Integer, nullable=False)
    ayah_number = db.Column(db.Integer, nullable=False)
    word_arabic = db.Column(db.LargeBinary, nullable=False)
    word_english = db.Column(db.String())
    ayah_text_id = db.Column(db.Integer, db.ForeignKey('quran_ayah_text.id'), nullable=False)
    english_translation = db.Column(db.String())
