import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)
from database import Database_conn as db

search = Flask(__name__)

# register--0|login--1|info--2
globals.status = 1
# login error
globals.error = 0
# register error
globals.retry = 0
# user info
globals.User = {"id":"","name":"","pw":"","gender":"","tele":"","brief":""}

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
        status=globals.status,
        error=globals.error,
        retry=globals.retry
        )

@search.route('/register', methods=['GET', 'POST'])
def register():
    globals.status=0
    return render_template(
        "profile.html",
        status=globals.status,
        error=globals.error,
        retry=globals.retry
        )
    
@search.route('/validation', methods=['GET', 'POST'])
def validation():
    if globals.status == 1:
        pw=request.form.get('pw')
        id=request.form.get('id')
        temp=db.get_info(id)
        if temp[4]==pw:
            globals.User={"id":temp[0],"name":temp[1],"gender":temp[2],"tele":temp[3],"pw":temp[4],"brief":temp[5]}
            globals.status = 2
            return render_template(
                "validation.html",
                status=globals.status,
                error=globals.error,
                retry=globals.retry
                )
        else:
            globals.error=1
            return render_template(
                "profile.html",
                status=globals.status,
                error=globals.error,
                retry=globals.retry
                )
    elif globals.status == 0:
        pw=request.form.get('pw')
        pw2=request.form.get('pw2')
        if pw==pw2:
            name=request.form.get("name")
            gender=request.form.get("gender")
            tele=request.form.get("tele")
            brief=request.form.get("brief")
            id=db.new_user(name,gender,tele,pw,brief)
            globals.status=1
            return render_template(
                "profile.html",
                status=globals.status,
                error=globals.error,
                retry=globals.retry
            )
        else:
            globals.retry=1
            return render_template(
                "profile.html",
                status=globals.status,
                error=globals.error,
                retry=globals.retry
            )
    
def run():
    search.run(debug=True)

# if __name__ == '__main__':
#     run()