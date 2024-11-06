from flask import Blueprint
# from routes import user_routes, home
from middleware.main_middleware import register_error_handlers, register_middleware
from middleware.auth_middleware import jwt_required_middleware
import os
import importlib
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt


def bootstrap_services(app):
    # init JWT
    jwt = JWTManager()
    jwt.init_app(app)

    # init bcrypt
    bcrypt = Bcrypt()
    bcrypt.init_app(app)

    # REGISTER ALL ROUTES DYNAMICALLY
    with app.app_context():

        basedir = os.path.abspath(os.path.dirname(__file__))
        # Navigate up to the root directory of your project
        routes_dir = os.path.abspath(os.path.join(basedir, '../routes'))

        for filename in os.listdir(routes_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                print(filename)
                # Import the module
                module_name = f'{filename[:-3]}'
                
                print(module_name)
                module_name = f'routes.{module_name}'
                print(module_name)
                module = importlib.import_module(module_name)

                # Register the blueprint
                for attr in dir(module):
                    blueprint = getattr(module, attr)
                    if isinstance(blueprint, Blueprint):
                        if blueprint.name not in app.blueprints:
                            app.register_blueprint(blueprint)
                        else:
                            print(f"Blueprint {blueprint.name} is already registered.")
                        # app.register_blueprint(blueprint)

    # INIT DATABASE CONNECTIONS
    from models.main_model import db
    db.init_app(app)

    # Register error handlers
    register_error_handlers(app)

    # Register middlewares
    # register_middleware(app)

    # Register auth middleware
