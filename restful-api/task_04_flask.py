#!/usr/bin/python3
"""
Task 4. Develop a Simple API using Python with Flask
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)

username = {
        "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
        "Molly": {"name": "Molly", "age": 29, "city": "Lormont"},
        "Alex": {"name": "Alex", "age": 93, "city": "Ginko"}
}

@app.route('/')

def home():
    return 'Welcome to the Flask API!'

@app.route('/data')

def getUsers():
    return jsonify(username)

@app.route('/status')

def status():
    return 'OK'

@app.route('/users/<username>')

def usersFullObject(username):
    users = users.get(username)
    if username:
        return jsonify(username)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user')

def status():
    return 'OK'

if __name__ == '__main__':
    app.run()
