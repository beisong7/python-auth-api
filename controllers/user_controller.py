from flask import jsonify, request
from models.users import Users
from models.main_model import db
from controllers.base_controller import BaseController
from middleware.auth_middleware import jwt_required_middleware

class UserController(BaseController):
    @staticmethod
    def get_users():
        users =  Users.get(paginate=2, route="get_users")
        return BaseController.success_response(users)
        # users = Users.query.all()
        # return jsonify([Users.to_dict(user) for user in users])

    @staticmethod
    def get_user(user_id):
        user = Users.first(user_id)
        if user is None:
            return BaseController.error_response('User not found')
        return BaseController.success_response(user)

    @staticmethod
    def create_user():
        data = request.get_json()
        new_user = Users(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            uid=data.get('uid'),
            state_id=data.get('state_id'),
            phone=data.get('phone'),
            reg_type=data.get('reg_type'),
            email_verified_at=data.get('email_verified_at'),
            password=data.get('password'),
            photo=data.get('photo'),
            device_firebase_token=data.get('device_firebase_token'),
            dob=data.get('dob'),
            is_active=data.get('is_active'),
            is_disabled=data.get('is_disabled'),
            remember_token=data.get('remember_token')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(Users.to_dict(new_user)), 201

    @staticmethod
    def update_user(user_id):
        user = Users.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        data = request.get_json()
        Users.first_name = data.get('first_name', Users.first_name)
        Users.last_name = data.get('last_name', Users.last_name)
        Users.email = data.get('email', Users.email)
        Users.uid = data.get('uid', Users.uid)
        Users.state_id = data.get('state_id', Users.state_id)
        Users.phone = data.get('phone', Users.phone)
        Users.reg_type = data.get('reg_type', Users.reg_type)
        Users.email_verified_at = data.get('email_verified_at', Users.email_verified_at)
        Users.password = data.get('password', Users.password)
        Users.photo = data.get('photo', Users.photo)
        Users.device_firebase_token = data.get('device_firebase_token', Users.device_firebase_token)
        Users.dob = data.get('dob', Users.dob)
        Users.is_active = data.get('is_active', Users.is_active)
        Users.is_disabled = data.get('is_disabled', Users.is_disabled)
        Users.remember_token = data.get('remember_token', Users.remember_token)

        db.session.commit()
        return jsonify(Users.to_dict(user))

    @staticmethod
    def delete_user(user_id):
        user = Users.query.get(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return '', 204
    
    @staticmethod
    @jwt_required_middleware
    def get_profile():
        user = Users.query.get(1)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(Users.to_dict(user))
    

