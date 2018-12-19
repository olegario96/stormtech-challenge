from app import app
import pytest

import json
import os

@pytest.fixture(scope='session')
def client():
    app.app.config['TESTING'] = True
    testing_client = app.app.test_client()
    ctx = app.app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

def test_sort_books_scenario4(client):
    res = client.post('/sort', json={})
    error = json.loads(res.data.decode('utf-8')).get('error')
    assert error == 'SortingServiceException'

def test_sort_books_scenario5(client):
    rules = {}
    json_books = {
        "books": [],
        "sorting_title": "",
        "sorting_author": "",
        "sorting_edition_year": ""
    }
    res = client.post('/sort', json=json_books)
    result = json.loads(res.data.decode('utf-8')).get('result')
    assert len(result) == 0
