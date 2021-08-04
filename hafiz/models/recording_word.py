from hafiz.app import db


class RecordingWord(db.Model):
    __tablename__ = 'recording_word'

    id = db.Column(db.Integer, primary_key=True)
    hafiz_id = db.Column(db.Integer, nullable=True)
    is_correct = db.Column(db.Boolean)
    recording_word = db.Column(db.LargeBinary, nullable=True)
    reciter_info_id = db.Column(db.Integer, db.ForeignKey('reciter_info.id'), nullable=False)
    word_text_id = db.Column(db.Integer, db.ForeignKey('quran_word_text.id'), nullable=False)
    recording_sentence_id = db.Column(db.Integer, db.ForeignKey('recording_sentence.id'), nullable=False)
