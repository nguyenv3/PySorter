import json

from flask import Flask, request, jsonify
from schematics.exceptions import DataError

from .request_models import NumberPOSTRequest
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
    return error_message, 422


@app.route('/')
def home():
    """
    Return a 200.
    """
    return 'Haha xd'


@app.route('/numbers', methods=['POST'])
def post_numbers():
    """
    Endpoint to handle sorting numbers.
    """
    request_model = NumberPOSTRequest(request.get_json())
    request_model.validate()
    sorted_list = sorted(request_model.numbers, key=int)
    return jsonify(sorted_list)