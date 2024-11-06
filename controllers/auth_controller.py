from flask import jsonify, request
from models.users import Users
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from controllers.base_controller import BaseController


class AuthController(BaseController):
    @staticmethod
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = Users.oneByEmail(email)

        # if user:
        #     return BaseController.success_response("works well")
        # else:
        #     return BaseController.success_response({"user": user})


        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token), 200
        return jsonify({"msg": "Bad email or password"}), 401