#!/usr/bin/python3
"""
Task 4. Develop a Simple API using Python with Flask
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
