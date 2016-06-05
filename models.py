from server import db

from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'hackathon'

    id = db.Column(db.Integer, primary_key=True)
    block = db.Column(db.Integer)
    lot = db.Column(db.Integer)
    address = db.Column(db.String())
    sc_rcvd = db.Column(db.String())
    screenFormRec = 
    OptEvalRec
    OptEvalComp
    InOut
    Tier
    Status
