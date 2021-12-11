import requests

# make parsers for this, maybe utils.py?
base_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=1577836800&to=1609376400"

# should maybe change this to just be parsing and create another class for request
class CoinGeckoRequest:
	
	def to_unixtime(from_time, to_time):
		pass

	def create_request_url():
		pass

	def choose_crypto():
		pass

	def create_payload():
		pass

	def highest_volume(self):
		volumes = [x[1] for x in self.json.get('total_volumes')]
		self.highest = {'highest_volume': max(volumes, default=0)}

	# not a fan of this but it works, rework later
	def downward_trend(self):
		max_bearish = 0
		counter = 0
		prices = [x[1] for x in self.json.get('prices')]
		for idx, val in enumerate(prices):
			if idx == 0:
				continue
			if val > prices[idx-1]:
				counter += 1
			else:
				if counter > max_bearish:
					max_bearish = counter
				counter = 0
		self.bearish = {"max_bearish": max_bearish}

	def time_machine(self):
		pass

	# just for checking out values
	def get_volumes(self):
		self.volumes = {'total_volumes': self.json.get('total_volumes')}

	# change the requests url to be modifiable to insert unix timestamps
	def ranged_bt_data(self):
		self.res = requests.get(base_url)
		self.json = self.res.json()

req = CoinGeckoRequest()