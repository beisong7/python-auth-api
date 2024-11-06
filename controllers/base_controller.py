from flask import jsonify

class BaseController:
    @staticmethod
    def error_response(message="Error handling request", code=500):
        response = {
            "status": "error",
            "error": message
        }
        return jsonify(response), code

    @staticmethod
    def success_response(data={"message": "Completed"}):
        response = {
            "status": "success",
            "data": data
        }
        return jsonify(response)
