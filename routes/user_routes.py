from flask import Blueprint
from controllers.user_controller import UserController

bp = Blueprint('users', __name__, url_prefix='/users')

bp.route('/', methods=['GET'])(UserController.get_users)
bp.route('/<int:user_id>', methods=['GET'])(UserController.get_user)
bp.route('/', methods=['POST'])(UserController.create_user)
bp.route('/<int:user_id>', methods=['PUT'])(UserController.update_user)
bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete_user)
