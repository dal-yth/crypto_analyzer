import requests
from app.helpers.tools import to_unixtime

# should maybe change this to just be parsing and create another class for request
class CoinGeckoRequest:

	# create params according to request args
	def create_params(self, args):
		self.params = {
			"vs_currency": args['vs_currency'] if args.get('vs_currency') else "eur",
			"from": to_unixtime(args.get('from')),
			"to": to_unixtime(args.get('to'))
		}
	
	def create_url(self, args):
		coin_id = args['id'] if args.get('id') else "bitcoin"
		self.url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"

	# create params and request the data
	def ranged_bt_data(self, args):
		self.create_params(args)
		self.create_url(args)
		res = requests.get(self.url, params=self.params)
		self.json = res.json()

	# get volumes from list of volumes and fetch highest one
	def highest_volume(self, args):
		self.ranged_bt_data(args)
		#just testing it out, but really dumb, find better way
		if "error" in self.json.keys():
			self.response = self.json.get("error")
			return
		volumes = [x[1] for x in self.json.get('total_volumes')]
		self.response = max(volumes, default=0)

	# not a fan of this but it works, rework later
	# counts days where trend goes downward and keeps track of highest value
	# should be noted that technically downwards trend could also have a plateau where price remains the same before going down again
	# above point is outside of the scope of project
	def downward_trend(self, args):
		self.ranged_bt_data(args)
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
		self.response = max_bearish

	#  in progress
	def max_profits(self, args):
		self.response = "testing"

req = CoinGeckoRequest()