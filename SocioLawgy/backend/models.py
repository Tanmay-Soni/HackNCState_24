from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Lawyer(db.Model):
    __tablename__ = 'lawyers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    speciality = db.Column(db.String, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    personal_website = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, nullable=False, default=False)

    cases = db.relationship('Case', backref=db.backref('lawyers'))

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    cases = db.relationship('Case', backref=db.backref('clients'))

class Case(db.Model):
    __tablename__ = 'cases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    case_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyers.id'), nullable=True)