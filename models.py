from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
from datetime import datetime

db = SQLAlchemy()

# define modes
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    confirmed_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
