import time
from queue import Empty
from telnetlib import STATUS
from flask import (
    Flask, render_template, request, redirect, url_for, globals)
import control 
import json

search = Flask(__name__)

@search.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'model.html'
        )
    
@search.route('/test', methods=['GET', 'POST'])
def test():
    con=json.loads(request.get_data(as_text=True))
    print(con["choice"][0])
    return render_template(
        'model.html'
        )
    
if __name__ == '__main__':
    search.run(debug=True)
    
    
