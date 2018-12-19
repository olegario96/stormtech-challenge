# Depdencies imports
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
import json

# Built-in imports
from os import environ

load_dotenv('')
host = environ.get('HOST')
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/sort', methods=['POST', 'GET'])
def sort_books():
    result = []
    if request.method == 'POST':
        json_books = request.json

        res = {'result': result, 'error': ''}
    else:
        res = {'result': result, 'error': 'Request must use POST method!'}

    return jsonify(res)

if __name__ == '__main__':
    app.run(host=host)
