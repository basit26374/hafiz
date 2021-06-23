from hafiz.app import db


class QuranAyahText(db.Model):
    __tablename__ = 'quran_ayah_text'

    id = db.Column(db.Integer, primary_key=True)
    surah_name = db.Column(db.String(), nullable=False)
    surah_number = db.Column(db.Integer, nullable=False)
    ayah = db.Column(db.LargeBinary, nullable=False)
    ayah_number = db.Column(db.Integer, nullable=False)
    no_of_sentences = db.Column(db.Integer)
    no_of_words = db.Column(db.Integer)
    no_of_stops = db.Column(db.Integer)
    no_of_variations = db.Column(db.Integer)
