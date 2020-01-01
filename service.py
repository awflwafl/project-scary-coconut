# standard library
import json

# third-party
from flask import Flask, jsonify, request
from flask_cors import CORS


service = Flask(__name__)

CORS(service)


@service.route('/ping', methods=['GET'])
def ping():
    return jsonify({ 'message': 'PONG' }), 200

if __name__ == '__main__':
    service.debug = True
    service.run(host='0.0.0.0', port=80)
