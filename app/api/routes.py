from . import api
from flask import request, jsonify
from .api_request import req

# maybe also check if coingecko is down?
@api.route("/status")
def status():
	return jsonify({'status': 'OK'}), 200

# This index route should have simple API documentation
@api.route("/")
def index():
	return "Hello, this is main page. It will hold simple API documentation.", 200

# make sure these return coingecko errors properly when user gives wrong inputs
@api.route("/bearish", methods=['GET'])
def get_downward_trend():
	req.downward_trend(request.args)
	return req.response, req.status_code

@api.route("/volume", methods=['GET'])
def get_highest_volume():
	req.highest_volume(request.args)
	return req.response, req.status_code

@api.route("/time_machine", methods=['GET'])
def get_max_profits():
	req.max_profits(request.args)
	return req.response, req.status_code
