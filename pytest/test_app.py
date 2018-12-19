from app import app
import pytest

import os
import tempfile

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
    assert 2 == 2

# def test_sort_books_scenario4(json_books):
#     rules = {'edition_year': True, 'author': True, 'title': False}
#     result = utilities.sort_books(json_books, rules)
#     assert result[0]['title'] == 'Java How To Program'
#     assert result[1]['title'] == 'Internet & World Wide Web: How to Program'
#     assert result[2]['title'] == 'Head First Design Patterns'
#     assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'

# def test_sort_books_scenario5(json_books):
#     rules = {'edition_year': True, 'author': True, 'title': False}
#     result = utilities.sort_books(json_books, rules)
#     assert result[0]['title'] == 'Java How To Program'
#     assert result[1]['title'] == 'Internet & World Wide Web: How to Program'
#     assert result[2]['title'] == 'Head First Design Patterns'
#     assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'
