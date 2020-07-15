from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
import pandas as pd

Base = declarative_base()

from app.extensions import db
from app.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


association_table = Table('association', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('vocab_id', Integer, ForeignKey('nocab.id'))
    )


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    connection = db.relationship('Nocab', secondary=association_table, 
        backref=db.backref('following_users', lazy='dynamic'))


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Nocab(db.Model):
    __tablename__ = 'nocab'
    id = Column(Integer, primary_key=True)
    words_es = db.Column(db.String(128))
    form = db.Column(db.Integer)
    def_es = db.Column(db.String(1000))
    frequency = db.Column(db.Integer)


