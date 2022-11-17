import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)
import control 

search = Flask(__name__)

@search.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'model.html'
        )
    
@search.route('/test', methods=['GET', 'POST'])
def test():
    con=request.form.get('1')
    print(con)
    return render_template(
        'model.html'
        )
    
if __name__ == '__main__':
    search.run(debug=True)
