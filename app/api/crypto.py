from . import api
from flask import jsonify
from .coingecko import req

@api.route("/status", methods=['GET'])
def status():
	return jsonify({'status': 'OK'}), 200

# testing coingecko
# change to POST to get from and to dates
@api.route("/gecko", methods=['GET'])
def test_gecko():
	req.ranged_bt_data()
	return req.json

# implement calendar so user can pick date
# should then call "gecko" route with calendar dates
@api.route("/", methods=['GET'])
def index():
	return "Hello, this is main page"

# these are not working at the moment, placeholders
@api.route("/bearish", methods=['POST'])
def bearish():
	return "VIP bearish"

@api.route("/volume", methods=['POST'])
def volume():
	return "VIP volume"

@api.route("/time_machine", methods=['POST'])
def time_machine():
	return "VIP time"