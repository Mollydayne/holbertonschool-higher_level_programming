#!/usr/bin/python3
"""
Task 5. API Security and Authentication Techniques
"""

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token, JWTManager, jwt_required, get_jwt_identity
)
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config["SECRET_KEY"] = "SuperMegaUltraSecretKey"
app.config["JWT_SECRET_KEY"] = "SuperSecretUltraMegaJWTKey"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"},
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    return username if user and check_password_hash(user["password"], password) else None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

@app.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token), 200

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
def handle_jwt_errors(err):
    return jsonify({"error": "Invalid or expired token"}), 401

if __name__ == "__main__":
    app.run(debug=True)
