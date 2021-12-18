import time
from datetime import datetime

# conversion to unixtime
# if user gives wrong values or format, we simply return the original and let coingecko handle the error
def to_unixtime(timestring):
    try:
        d = datetime.strptime(timestring, "%Y-%m-%d")
    except:
        return timestring
    unixtime = int(time.mktime(d.timetuple()))
    return unixtime

def from_unixtime(timestring):
    return timestring

# create params according to request args
def create_params(args):
    params = {
        "vs_currency": args.get('vs_currency') or "eur",
        "from": to_unixtime(args.get('from')),
        "to": to_unixtime(args.get('to')) # need to add 3600 to this
    }
    return params

# create url for chosen coin
def create_url(args):
    coin_id = args.get('id') or "bitcoin"
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    return url
