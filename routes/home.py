from flask import Blueprint
from controllers.home_controller import HomeController
from controllers.user_controller import UserController

bp = Blueprint('home', __name__)

bp.route('/', methods=['GET'])(HomeController.home)
bp.route('/profile/', methods=['GET'])(UserController.get_profile)