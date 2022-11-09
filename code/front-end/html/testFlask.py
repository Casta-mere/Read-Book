import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)

search = Flask(__name__)

# login/reg--0|info--1
globals.status = 0

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
    
def run():
    search.run(debug=True)

if __name__ == '__main__':
    run()