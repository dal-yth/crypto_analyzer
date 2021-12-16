from . import api
from flask import request, jsonify
from .coingecko import req

@api.route("/status")
def status():
	return jsonify({'status': 'OK'}), 200

# implement calendar so user can pick date
# should then call "gecko" route with calendar dates
@api.route("/")
def index():
	return "Hello, this is main page. It will hold simple API documentation."

# make sure these return coingecko errors properly when user gives wrong inputs
@api.route("/bearish", methods=['GET'])
def get_downward_trend():
	req.downward_trend(request.args)
	return jsonify({"max_bearish": req.response}), 200

@api.route("/volume", methods=['GET'])
def get_highest_volume():
	req.highest_volume(request.args)
	return jsonify({'highest_volume': req.response}), 200

@api.route("/time_machine", methods=['GET'])
def get_max_profits():
	req.max_profits(request.args)
	return jsonify({'max_profit': req.response}), 200
