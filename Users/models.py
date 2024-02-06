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


class Status(Enum):
    pending = "Pending"
    delivering = "Delivering"
    devliverd = "Delivered"


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
    sample = relationship('Sample', backref='laboratory')


class LabBranch(db.Model):
    __tablename__ = 'laboratory_branch'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    laboratory_id = db.Column(db.String(36), db.ForeignKey('laboratory.id', name='fk_laboratory_branch_to_laboratory'), \
                              nullable=False)
    branch_name = db.Column(db.String(256))
    manager = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    services = db.Column(db.Text)
    address = relationship('LabAddress', backref='lab_branch', uselist=False)


class LabAddress(db.Model):
    __tablename__ = 'laboratory_address'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    lab_branch_id = db.Column(db.String, db.ForeignKey('laboratory_branch.id', name='fk_address_to_laboratory_branch') \
                              , nullable=False, unique=True)
    address = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(256), nullable=True)


class UserAddress(db.Model):
    __tablename__ = 'user_address'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', name='fk_UserAddress_to_user'), nullable=False)
    address = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(256), nullable=True)


class Delivery(db.Model):
    __tablename__ = 'delivery'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(256), nullable=False)
    address = db.Column(db.Text)
    slug = db.Column(db.String(256))


class SampleType(db.Model):
    __tablename__ = 'sample_type'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    type = db.Column(db.Text)
    sample = relationship('Sample', backref='sample_type')


class Sample(db.Model):
    __tablename__ = 'sample'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id', name='fk_sample_to_user'), nullable=False)
    laboratory_id = db.Column(db.String(36), db.ForeignKey('laboratory.id', name='fk_sample_to_laboratory'))
    sample_type_id = db.Column(db.String(36), db.ForeignKey('sample_type.id', name='fk_sample_to_sampletype'))
    dr_id = db.Column(db.String(36), db.ForeignKey('users.id', name='fk_sample_to_user_docter'))
    status = db.Column(db.Enum(Status), default=Status.pending)
    traking_code = db.Column(db.String(1000))
    result = db.Column(db.Text)
    program = relationship('Program', backref='program')


class Program(db.Model):
    __tablename__ = 'program'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    dr_program_id = db.Column(db.String(36), db.ForeignKey('dr_program.id', name='fk_program_to_doctorProgram'))
    sample_id = db.Column(db.String(36), db.ForeignKey('sample.id', name='fk_program_to_sample'))
    ai_text = db.Column(db.Text)
    dr_text = db.Column(db.Text)
    status = db.Column(db.Boolean, default=False)


class DrProgram(db.Model):
    __tablename__ = 'dr_program'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    dr_id = db.Column(db.String(36), db.ForeignKey('users.id', name='fk_drprogam_to_doctor'))
    analize = db.Column(db.Text)
    # to_do = relationship('ToDo', backref='dr')


class ToDo(db.Model):
    __tablename__ = 'to_do'


