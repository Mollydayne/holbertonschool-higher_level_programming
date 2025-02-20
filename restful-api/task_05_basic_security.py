#!/usr/bin/python3
"""
Task 5. API Security and Authentication Techniques
"""

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles", "password": generate_password_hash("monsecret")},
    "Molly": {"name": "Molly", "age": 29, "city": "Lormont", "password": generate_password_hash("pastek")},
    "Alex": {"name": "Alex", "age": 93, "city": "Ginko", "password": generate_password_hash("bobbyesttromims")}
}