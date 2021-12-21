import requests
from app.helpers.tools import create_params, create_url, find_days_time, from_unixtime, handle_conversion


class APIRequest:

	# check for failed status codes
	def request_failed(self):
		if self.status_code > 399:
			self.response = self.json # coingecko error becomes the response
			return True
		return False

	# request the data
	# test the error cases!
	def ranged_coin_data(self, args):
		res = requests.get(url=create_url(args), params=create_params(args))
		self.status_code = res.status_code
		self.json = res.json()

	# get volumes from list of volumes and fetch highest one
	def highest_volume(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
		data = handle_conversion(self.json.get('total_volumes'))
		print("converted data:")
		for item in data:
			print(f"{from_unixtime(item[0])}:{item[1]}")
		cumu = 0
		for item in data:
			cumu += item[1]
		print(f"average volume: {cumu / len(data)}, cumu: {cumu}, len:{len(data)}")
		print("")
		days_time = find_days_time(data, args)
		print("day by day data:")
		for item in days_time:
			print(f"{from_unixtime(item[0])}:{item[1]}")
		volumes = [x[1] for x in days_time]
		self.response = {'highest_volume': max(volumes, default=0)}

	# not a fan of this but it works, need to refactor and split
	# counts days where trend goes downward and keeps track of highest value
	def downward_trend(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
		data = handle_conversion(self.json.get('prices'))
		print("converted data:")
		for item in data:
			print(f"{from_unixtime(item[0])}:{item[1]}")
		print("")
		prices = find_days_time(data, args)
		print("day by day data:")
		for item in prices:
			print(f"{from_unixtime(item[0])}:{item[1]}")
		max_bearish = 0
		counter = 0
		for idx, val in enumerate(prices):
			if idx == 0:
				continue
			if val[1] < prices[idx-1][1]:
				counter += 1
			else:
				if counter > max_bearish: # counted more bearish days
					max_bearish = counter
				counter = 0
		if counter > max_bearish: # in case last day was bearish
			max_bearish = counter
		self.response = {'max_bearish': max_bearish}

	# find max difference in bitcoin value
	# really need to refactor this
	def max_profits(self, args):
		self.ranged_coin_data(args)
		if self.request_failed():
			return
		data = handle_conversion(self.json.get('prices'))
		print("converted data:")
		for item in data:
			print(f"{from_unixtime(item[0])}:{item[1]}")
		print("")
		prices = find_days_time(data, args)
		print("day by day data:")
		for item in prices:
			print(f"{from_unixtime(item[0])}:{item[1]}")
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
		self.response = {"buy_date": from_unixtime(buy_date), "sell_date": from_unixtime(sell_date)}

req = APIRequest()