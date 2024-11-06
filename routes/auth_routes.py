from flask import Blueprint
from controllers.auth_controller import AuthController

bp = Blueprint('auth_routes', __name__)

bp.route('/login', methods=['POST'])(AuthController.login)