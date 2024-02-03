from flask_sqlalchemy import SQLAlchemy
import uuid
import datetime

db = SQLAlchemy()
def generated_uuid():
    import string, random
    charecters = string.ascii_letters + string.digits
    short_uuid = ''.join(random.choice(charecters) for _ in range(10))
    return short_uuid

class User(db.Model):
    __tablename__ = 'users'
    # id
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    affiliate_id = db.Column(db.String(10), unique=True, default=generated_uuid())
    address = db.Column(db.Text())
    password = db.Column(db.String(500), nullable=False)
    verify = db.Column(db.DateTime(), default=datetime.datetime.now())
    verify_by_admin = db.Column(db.DateTime())
