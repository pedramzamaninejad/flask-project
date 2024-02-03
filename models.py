import uuid
import datetime
from enum import Enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def generated_uuid():
    import string, random
    charecters = string.ascii_letters + string.digits
    short_uuid = ''.join(random.choice(charecters) for _ in range(10))
    return short_uuid


class BloodType(Enum):
    Not_given = 'NG'
    A_positive = 'A+'
    A_negative = 'A-'
    B_positive = 'B+'
    B_negative = 'B-'
    O_positive = 'O+'
    O_negative = 'O-'
    AB_positive = 'AB+'
    AB_negative = 'AB-'


class Type(Enum):
    normal = 'N'
    doctor = 'D'


class User(db.Model):
    __tablename__ = 'users'
    # id
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    affiliate_id = db.Column(db.String(10), unique=True, default=generated_uuid())
    affiliated_by = db.Column(db.String(10), nullable=True)
    location = db.Column(db.Text(), nullable=True)
    address = db.Column(db.Text(), nullable=True)
    password = db.Column(db.String(500), nullable=False)
    verify = db.Column(db.DateTime(), default=datetime.datetime.now())
    verify_by_admin = db.Column(db.Boolean(), default=False)
    blood_type = db.Column(db.Enum(BloodType), default=BloodType.Not_given)
    type = db.Column(db.Enum(Type), default=Type.normal)
