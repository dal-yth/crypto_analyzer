from flask import Flask, jsonify
import requests

# just for testing
base_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=1577836800&to=1609376400"

app = Flask(__name__)

# create date to unix timestamp conversion!
def to_unixtime(time):
	pass

# change the requests url to be modifiable to insert unix timestamps
def ranged_bt_data():
	res = requests.get(base_url)
	return res.json()

@app.route("/status", methods=['GET'])
def status():
	return jsonify({'status': 'OK'}), 200

# testing coingecko
# change to POST to get from and to dates
@app.route("/gecko", methods=['GET'])
def test_gecko():
	return ranged_bt_data()

# implement calendar so user can pick date
# should then call "gecko" route with calendar dates
@app.route("/", methods=['GET'])
def index():
	return "Hello, this is main page"

