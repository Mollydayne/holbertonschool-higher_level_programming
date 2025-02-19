#!/usr/bin/python3
"""
Task 4. Develop a Simple API using Python with Flask
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {
        "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
        "Molly": {"name": "Molly", "age": 29, "city": "Lormont"},
        "Alex": {"name": "Alex", "age": 93, "city": "Ginko"}
}

@app.route('/')

def home():
    return 'Welcome to the Flask API!'

@app.route('/data')

def getUsers():
    return jsonify(users)

@app.route('/status')

def status():
    return 'OK'

@app.route('/users/<username>')

def usersFullObject(username):
    users = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    username = data["username"]

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "Yeah, u added someone else !", "user": users[username]}), 201  # ✅ JSON structuré

if __name__ == '__main__':
    app.run()
