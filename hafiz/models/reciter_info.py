from hafiz.app import db


class ReciterInfo(db.Model):
    __table_name__ = 'reciter_info'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    location = db.Column(db.String())
    gender = db.Column(db.String())
