"""
    The problem proposed is solved by using a Flask web application. As the
    problem hadn't give no restriction for the application, a web application
    was choosed, since the candidate has experience with it. Also, the Flask
    was choosed, because it is designed to be a small framework to work with
    microservices, that is exactly what this application is. The API has only
    one route, /sort, that receives the books in JSON format and returns
    all the books ordered using as criteria the author, title or edition
    year.
"""

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
    """
        The index just indicates the file where the user
        can found more information about the service.
    """
    return 'To more info, check the README.md file!'

@app.route('/sort', methods=['POST', 'GET'])
def sort_books():
    """
        This route receives the books in json format using POST as HTTP method.
        The JSON must containg at least one rule to order the books, or an
        exception will be sent to the client. This is a requisite. After
        sort the books, the server will respond with the books ordered by
        the criteria(s) in JSON format too.
    """
    result = []
    if request.method == 'POST':
        json_books = request.json
        rules = utilities.get_rules_from_json(json_books)
        if rules:
            if json_books.get('books'):
                result = utilities.sort_books(json_books, rules)
            res = {'result': result, 'error': ''}
        else:
            res = {'result': result, 'error': 'SortingServiceException'}
    else:
        res = {'result': result, 'error': 'Request must use POST method!'}

    return jsonify(res)


if __name__ == '__main__':
    """
        Main method to just start the application.
    """
    app.run(host=host)
