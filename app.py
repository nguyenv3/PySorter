import json
import http.client

from flask import Flask, request, jsonify, render_template, send_file
from schematics.exceptions import DataError

from .request_models import NumberPOSTRequest, StringPOSTRequest
app = Flask(__name__)


@app.errorhandler(DataError)
def data_error_handler(error):
    error_message = json.dumps({
        'error': {
            # Find a better way to change an error to a
            # JSON serializable.
            'validation': json.loads(str(error))
        }
    })
    return error_message, http.client.UNPROCESSABLE_ENTITY


@app.route('/')
def home():
    """
    Return a 200.
    """
    return render_template('homepage.html')


@app.route('/numbers', methods=['POST'])
def post_numbers():
    """
    Endpoint to handle sorting numbers.
    """
    request_model = NumberPOSTRequest(request.get_json())
    request_model.validate()
    sorted_list = sorted(request_model.numbers, key=int,
                         reverse=request_model.descending)
    return jsonify(sorted_list)


@app.route('/strings', methods=['POST'])
def post_strings():
    """
    Endpoint to handle sorting text.
    """
    request_model = StringPOSTRequest(request.get_json())
    request_model.validate()
    sorted_list = sorted(request_model.strings,
                         reverse=request_model.descending)
    return jsonify(sorted_list)


@app.route('/haha', methods=['GET'])
def get_webclient():
    """
    Endpoint to get the javascript.
    """
    return send_file('webclient.js')