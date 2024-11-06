from datetime import datetime
from models.main_model import db
from models.model import BaseModel
from flask_bcrypt import generate_password_hash, check_password_hash

class Users(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    uid = db.Column(db.String(120), unique=True, nullable=False)
    state_id = db.Column(db.Integer, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    reg_type = db.Column(db.String(20), nullable=True)
    email_verified_at = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=True)
    device_firebase_token = db.Column(db.String(255), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    is_disabled = db.Column(db.Boolean, default=False)
    remember_token = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'uid': self.uid,
            'state_id': self.state_id,
            'phone': self.phone,
            'reg_type': self.reg_type,
            'email_verified_at': self.email_verified_at.isoformat() if self.email_verified_at else None,
            'password': self.password,
            'photo': self.photo,
            'device_firebase_token': self.device_firebase_token,
            'dob': self.dob,
            'is_active': self.is_active,
            'is_disabled': self.is_disabled,
            'remember_token': self.remember_token,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
