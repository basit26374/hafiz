from hafiz.app import db


class QuranAyahText(db.Model):
    __tablename__ = 'quran_ayah_text'

    id = db.Column(db.Integer, primary_key=True)
    surah_name = db.Column(db.String(), nullable=False)
    surah_number = db.Column(db.Integer, nullable=False)
    ayah_arabic = db.Column(db.LargeBinary, nullable=False)
    ayah_indo_pak = db.Column(db.LargeBinary)
    ayah_uthmani = db.Column(db.LargeBinary)
    ayah_number = db.Column(db.Integer, nullable=False)
