import flask
from flask import *
import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
