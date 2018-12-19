# stormtech-challenge

This repo contains all the source code used to solve the problem for the
[Stormtech challenge](http://site.stormtech.com.br/).

## Solution

To solve the proposed problem, a microservice in Flask was built. Basically,
you have to send a `POST` request to the route `/sort` and passing the books
as body. A example of the JSON file can be checked in the `books.json` file.

### Dependencies

This project was built in a Ubuntu 16.04 machine. To run this project on your
computer you must have `Python3, pip, virtualenv`. Install all this tools with:

```
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip -y
$ sudo pip3 install virtualenv
$ virtualenv .venv && source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

### Run

To run this project, inside the `.venv`, just type:

```
(.venv) $ flask run
```

### Tests

To run all tests, inside the `.venv`, just type:

```
(.venv) $ python -m pytest
```
