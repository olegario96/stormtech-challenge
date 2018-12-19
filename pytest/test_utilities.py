import app.utilities as utilities
import json
import pytest
import random

@pytest.fixture(autouse=True)
def random_list():
    random_list = random.sample(range(0, 100), 10)
    random_list.sort()
    return random_list

@pytest.fixture(autouse=True)
def json_books():
    with open('books.json', 'r') as json_file:
        json_books = json.load(json_file)
    return json_books

def test_get_rules_from_json(json_books):
    rules = utilities.get_rules_from_json(json_books)
    assert rules['title'] == False
    assert rules['author'] == False
    assert rules['edition_year'] == True

def test_compare_books_by_one_attribute_ascending(json_books):
    rule = 'title'
    descending = False
    books = json_books.get('books')
    book1, book2 = books[0], books[1]
    assert utilities.compare_books_by_one_attribute(book1, book2, rule, descending) == True

def test_compare_books_by_one_attribute_descending(json_books):
    rule = 'title'
    descending = True
    books = json_books.get('books')
    book1, book2 = books[0], books[1]
    assert utilities.compare_books_by_one_attribute(book1, book2, rule, descending) == False

def test_compare_books(json_books):
    rules = utilities.get_rules_from_json(json_books)
    books = json_books.get('books')
    book1, book2 = books[0], books[1]
    assert utilities.compare_books(book1, book2, rules) == True

def test_binary_search(json_books):
    pass

def test_sort_books(json_books):
    rules = utilities.get_rules_from_json(json_books)
    result = utilities.sort_books(json_books, rules)
    assert result[0]['title'] == 'Head First Design Patterns'
    assert result[1]['title'] == 'Internet & World Wide Web: How to Program'
    assert result[2]['title'] == 'Java How To Program'
    assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'

def test_sort_books_scenario1(json_books):
    rules = {'title': False}
    result = utilities.sort_books(json_books, rules)
    assert result[0]['title'] == 'Head First Design Patterns'
    assert result[1]['title'] == 'Internet & World Wide Web: How to Program'
    assert result[2]['title'] == 'Java How To Program'
    assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'

def test_sort_books_scenario2(json_books):
    rules = {'author': False, 'title': True}
    result = utilities.sort_books(json_books, rules)
    assert result[0]['title'] == 'Java How To Program'
    assert result[1]['title'] == 'Internet & World Wide Web: How to Program'
    assert result[2]['title'] == 'Head First Design Patterns'
    assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'

def test_sort_books_scenario3(json_books):
    rules = {'edition_year': True, 'author': True, 'title': False}
    result = utilities.sort_books(json_books, rules)
    assert result[0]['title'] == 'Internet & World Wide Web: How to Program'
    assert result[1]['title'] == 'Java How To Program'
    assert result[2]['title'] == 'Head First Design Patterns'
    assert result[3]['title'] == 'Patterns of Enterprise Application Architecture'
