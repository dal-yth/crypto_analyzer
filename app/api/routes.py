from . import api
from flask import request, redirect, make_response, render_template
from .api_request import res

@api.route("/status")
def status():
	return make_response("OK", 200)

# catch all route to redirect to documentation
@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
	return redirect("/api/documentation")

# API documentation
@api.route("/api/documentation")
def index():
	return render_template('index.html')

@api.route("/api/downward_trend", methods=['GET'])
def get_downward_trend():
	res.downward_trend(request.args)
	return make_response(res.body, res.status_code)

@api.route("/api/highest_volume", methods=['GET'])
def get_highest_volume():
	res.highest_volume(request.args)
	return make_response(res.body, res.status_code)

@api.route("/api/max_profits", methods=['GET'])
def get_max_profits():
	res.max_profits(request.args)
	return make_response(res.body, res.status_code)
