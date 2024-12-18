from flask import request, jsonify

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != "Bearer SECRET-TOKEN":
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper