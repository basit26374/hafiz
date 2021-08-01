from hafiz.app import db


class QuranWordText(db.Model):
    __table_name__ = 'quran_word_text'

    id = db.Column(db.Integer, primary_key=True)
    word_arabic = db.Column(db.String())