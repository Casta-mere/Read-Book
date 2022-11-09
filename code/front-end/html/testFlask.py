import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)

search = Flask(__name__)

# register--0|login--1|info--2
globals.status = 1

@search.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html',
        status=globals.status
        )
    
@search.route('/books', methods=['GET', 'POST'])
def books():
    return render_template(
        'books.html',
        status=globals.status
        )

@search.route('/test', methods=['GET', 'POST'])
def test():
    return render_template(
        'test.html',
        status=globals.status
        )
    
@search.route('/statistics', methods=['GET', 'POST'])
def statistics():
    return render_template(
        'statistics.html',
        status=globals.status
        )
    
@search.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template(
        'profile.html',
        status=globals.status
        )
    
@search.route('/login', methods=['GET', 'POST'])
def login():
    globals.status = 1
    return render_template(
        'profile.html',
        status=globals.status
        )

@search.route('/register', methods=['GET', 'POST'])
def register():
    globals.status=0
    return render_template(
        "profile.html",
        status=globals.status
        )
    
@search.route('/validation', methods=['GET', 'POST'])
def validation():
    globals.status = 2
    return render_template(
        "validation.html",
        status=globals.status
        )
    
def run():
    search.run(debug=True)

if __name__ == '__main__':
    run()