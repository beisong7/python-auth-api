from flask import jsonify, request

class HomeController:
    @staticmethod
    def home():
        return jsonify({"app": "Flask Api Running", "Version": "0"})