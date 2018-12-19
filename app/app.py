# Depdencies imports
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
import json
import app.utilities as utilities

# Built-in imports
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))
host = os.environ.get('HOST')
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/sort', methods=['POST', 'GET'])
def sort_books():
     result = []
     if request.method == 'POST':
        json_books = request.json
        if json_books.get('rules'):
            rules = utilities.get_rules_from_json(json_books)
            if json_books.get('books'):
                result = utilities.sort_books(json_books, rules)
                res = {'result': result, 'error': ''}
        else:
            res = {'result': result, 'error': 'SortingServiceException'}
     else:
        res = {'result': result, 'error': 'Request must use POST method!'}

     return jsonify(res)


if __name__ == '__main__':
    app.run(host=host)
