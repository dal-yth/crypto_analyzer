import requests
from app.helpers.tools import create_params, create_url, find_day_range, from_unixtime, convert_s_to_ms


class APIRequest:

	# check for failed status codes
	def request_failed(self):
		if self.status_code > 399:
			self.body = self.json # coingecko error becomes the response
			return True
		return False

	# request the data from coingecko
	def get_ranged_coin_data(self, args):
		try:
			res = requests.get(url=create_url(args), params=create_params(args))
			self.status_code = res.status_code
			self.json = res.json()
		except: # in case something goes wrong with request such as 50 request limit
			self.status_code = 404
			self.json = {"error": "page not found"}

	# calls funcs to do the request, check for failure and process the data for routes
	def fetch_and_process_data(self, args, data_key):
		self.get_ranged_coin_data(args)
		if self.request_failed():
			return False
		ranged_data = find_day_range(self.json.get(data_key), args)
		self.data = convert_s_to_ms(ranged_data)
		return True

	# get volumes from list of volumes and fetch highest one
	def highest_volume(self, args):
		if not self.fetch_and_process_data(args, "total_volumes"):
			return
		volumes = [x[1] for x in self.data]
		self.body = {'highest_volume': max(volumes, default=0)}

	# counts days where trend goes downward and keeps track of highest value
	def downward_trend(self, args):
		if not self.fetch_and_process_data(args, "prices"):
			return
		max_bearish = 0
		counter = 0
		for idx, val in enumerate(self.data):
			if idx == 0:
				continue
			if val[1] < self.data[idx-1][1]:
				counter += 1
			else:
				if counter > max_bearish: # counted more bearish days
					max_bearish = counter
				counter = 0
		if counter > max_bearish: # in case last day was bearish
			max_bearish = counter
		self.body = {'downward_trend': max_bearish}

	# find max difference in bitcoin value
	def max_profits(self, args):
		if not self.fetch_and_process_data(args, "prices"):
			return
		min = self.data[0] if self.data else 0 # get price of first entry
		diff = 0
		buy_date = None
		sell_date = None
		for price in self.data:
			if (price[1] < min[1]): # found new minimum price
				min = price
			elif (price[1] - min[1] > diff): # found greater profit
				diff = price[1] - min[1]
				buy_date = min[0]
				sell_date = price[0]
		self.body = {"buy_date": from_unixtime(buy_date), "sell_date": from_unixtime(sell_date)}

res = APIRequest()