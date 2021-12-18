import requests
from app.helpers.tools import create_params, create_url


class APIRequest:

	# check for failed status codes
	def request_failed(self):
		if self.status_code > 399:
			self.response = self.json # coingecko error becomes the response
			return True
		return False

	# request the data
	def ranged_coin_data(self, args):
		res = requests.get(url=create_url(args), params=create_params(args))
		self.status_code = res.status_code
		self.json = res.json()

	# get volumes from list of volumes and fetch highest one
	def highest_volume(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
		volumes = [x[1] for x in self.json.get('total_volumes')]
		self.response = {'highest_volume': max(volumes, default=0)}

	# not a fan of this but it works
	# counts days where trend goes downward and keeps track of highest value
	def downward_trend(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
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
		self.response = {'max_bearish': max_bearish}

	# find max difference in bitcoin value
	def max_profits(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
		prices = list(self.json.get('prices'))
		min = prices[0] if prices else 0 # get price of first entry
		diff = 0
		buy_date = None
		sell_date = None
		for price in prices:
			if (price[1] < min[1]): # we find new minimum price
				min = price
			elif (price[1] - min[1] > diff): # we find greater profit
				diff = price[1] - min[1]
				buy_date = min[0]
				sell_date = price[0]
		self.response = {"buy_date": buy_date, "sell_date": sell_date}

req = APIRequest()