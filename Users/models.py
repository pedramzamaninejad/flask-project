import datetime
import uuid
from enum import Enum

from flask_sqlalchemy import SQLAlchemy
from shortuuid import ShortUUID
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class BloodType(Enum):
    Not_given = 'Not Given'
    A_positive = 'A+'
    A_negative = 'A-'
    B_positive = 'B+'
    B_negative = 'B-'
    O_positive = 'O+'
    O_negative = 'O-'
    AB_positive = 'AB+'
    AB_negative = 'AB-'


class UserType(Enum):
    normal = 'Normal'
    doctor = 'Doctor'


class Sex(Enum):
    not_given = "Not Given"
    male = "Male"
    female = "Female"
    non_binary = 'Non Binary'


class User(db.Model):
    __tablename__ = 'users'
    # id
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    sex = db.Column(db.Enum(Sex), default=Sex.not_given)
    weight = db.Column(db.Float, nullable=True)
    affiliate_id = db.Column(db.String(10), unique=True, default=lambda: ShortUUID().random(length=10))
    affiliated_by = db.Column(db.String(10), nullable=True)
    address = relationship('UserAddress', backref='user', uselist=True)
    password = db.Column(db.String(500), nullable=False)
    verify = db.Column(db.DateTime, default=datetime.datetime.now())
    verify_by_admin = db.Column(db.Boolean, default=False)
    blood_type = db.Column(db.Enum(BloodType), default=BloodType.Not_given)
    user_type = db.Column(db.Enum(UserType), default=UserType.normal)


class Laboratory(db.Model):
    __tablename__ = 'laboratory'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(256), nullable=False)
    employee = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(256), nullable=False)
    year_founded = db.Column(db.Date, nullable=False)
    branches = relationship('LabBranch', backref='laboratory')


class LabBranch(db.Model):
    __tablename__ = 'laboratory_branch'

    id = db.Column(db.Integer, primary_key=True)
    laboratory_id = db.Column(db.String(36), db.ForeignKey('laboratory.id', name='fk_laboratory_branch_to_laboratory'), \
                              nullable=False)
    branch_name = db.Column(db.String(256))
    manager = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    services = db.Column(db.Text)
    address = relationship('LabAddress', backref='lab_branch', uselist=False)


class LabAddress(db.Model):
    __tablename__ = 'laboratory_address'

    id = db.Column(db.Integer, primary_key=True)
    lab_branch_id = db.Column(db.String, db.ForeignKey('laboratory_branch.id', name='fk_address_to_laboratory_branch') \
                              , nullable=False, unique=True)
    address = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(256), nullable=True)


class UserAddress(db.Model):
    __tablename__ = 'user_address'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', name='fk_UserAddress_to_user'), nullable=False)
    address = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(256), nullable=True)
