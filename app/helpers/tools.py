import time
from datetime import datetime

unix_day = 86000 # unix day in seconds
daily_range = 7826000 # 91 days in seconds

# conversion to unixtime
# if user gives wrong values or format, simply return the original and let coingecko handle the error
def to_unixtime(dt_string):
    fmt = "%Y-%m-%d"
    try:
        d = datetime.strptime(dt_string, fmt)
        return int(time.mktime(d.timetuple()))
    except:
        return dt_string

# conversion from unixtime and split to include only the day
def from_unixtime(unixtime):
    try:
        return datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S.%f').split(" ")[0]
    except:
        return unixtime

# create params according to request args
def create_params(args):
    params = {
        "vs_currency": args.get('vs_currency') or "eur",
        "from": to_unixtime(args.get('from')),
        "to": to_unixtime(args.get('to'))
    }
    # request at least 90 days, it feels hacky, but is much easier than dealing with granularity
    if type(params["to"]) == int and type(params["from"]) == int:
        if params["to"] >= params["from"] and params["to"] - params["from"] < daily_range: # increase the range to 90 days if it's less
            params["to"] = params["from"] + daily_range
    return params

# create url for chosen coin
def create_url(args):
    coin_id = args.get('id') or "bitcoin"
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    return url

# coingecko returns milliseconds, convert to seconds
def convert_s_to_ms(data):
    return [[int(item[0] / 1000), item[1]] for item in data]

# find out the requested range of days out of all days
def find_day_range(data, args):
    start_unix = to_unixtime(args.get('from'))
    end_unix = to_unixtime(args.get('to'))
    if type(start_unix) == int and type(end_unix) == int:
        days = int(((end_unix + unix_day) - start_unix) / unix_day)
        return data[:days]
    else:
        return data
