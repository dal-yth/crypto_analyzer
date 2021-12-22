from . import api
from flask import request, make_response
from .api_request import req

# maybe also check if coingecko is down?
@api.route("/status")
def status():
	return make_response("OK", 200)

# This index route should have simple API documentation, or make apidoc route?
@api.route("/")
def index():
	return make_response("Hello, this is main page. You should head over to /api/highest_volume, /api/downward_trend and /api/time_machine", 200)

@api.route("/api/downward_trend", methods=['GET'])
def get_downward_trend():
	req.downward_trend(request.args)
	return make_response(req.response, req.status_code)

@api.route("/api/highest_volume", methods=['GET'])
def get_highest_volume():
	req.highest_volume(request.args)
	return make_response(req.response, req.status_code)

@api.route("/api/time_machine", methods=['GET'])
def get_max_profits():
	req.max_profits(request.args)
	return make_response(req.response, req.status_code)

# add apidoc route and catchall route that leads to apidoc
#api.route("/apidoc")