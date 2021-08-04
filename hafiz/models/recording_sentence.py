from hafiz.app import db


class RecordingSentence(db.Model):
    __tablename__ = 'recording_sentence'

    id = db.Column(db.Integer, primary_key=True)
    hafiz_id = db.Column(db.Integer, nullable=True)
    audio_clarity = db.Column(db.String())
    background_noise_level = db.Column(db.String())
    with_tajweed = db.Column(db.Boolean)
    number_of_mistakes = db.Column(db.Integer)
    mistakes = db.Column(db.JSON)
    audio_format = db.Column(db.String())
    audio_length_seconds = db.Column(db.BigInteger)

    recording_sentence = db.Column(db.LargeBinary)
    reciter_info_id = db.Column(db.Integer, db.ForeignKey('reciter_info.id'), nullable=False)
    sentence_text_id = db.Column(db.Integer, db.ForeignKey('quran_sentence_text.id'), nullable=False)
