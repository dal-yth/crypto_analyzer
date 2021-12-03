import requests

# make parsers for this, maybe utils.py?
base_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=1577836800&to=1609376400"

class CoinGeckoRequest:
	
	def to_unixtime(from_time, to_time):
		pass

	def create_request_url():
		pass

	def choose_crypto():
		pass

	def create_payload():
		pass

	# change the requests url to be modifiable to insert unix timestamps
	def ranged_bt_data(self):
		self.res = requests.get(base_url)
		self.json = self.res.json()

req = CoinGeckoRequest()