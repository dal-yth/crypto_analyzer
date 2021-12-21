import time
from datetime import datetime

day_and_hour = 86000 + 3600 # value for including the end date plus an hour

# conversion to unixtime
# if user gives wrong values or format, we simply return the original and let coingecko handle the error
def to_unixtime(dt_string):
    fmts = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S.%f"]
    for fmt in fmts:
        try:
            d = datetime.strptime(dt_string, fmt)
            return int(time.mktime(d.timetuple()))
        except:
            pass
    return dt_string

# conversion from unixtime and split to include only the day
def from_unixtime(unixtime):
    try:
        return datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S.%f').split(" ")[0]
    except:
        return unixtime

# create params according to request args and add the day and hour
def create_params(args):
    params = {
        "vs_currency": args.get('vs_currency') or "eur",
        "from": to_unixtime(args.get('from')),
        "to": to_unixtime(args.get('to'))
    }
    if type(params['to']) == int: # if user gives invalid input can't add to string
        params['to'] = params['to'] + day_and_hour # add day and hour to always get data for end date + hour into the next
    return params

# create url for chosen coin
def create_url(args):
    coin_id = args.get('id') or "bitcoin"
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range"
    return url

# coingecko takes seconds but returns milliseconds
def handle_conversion(data):
    return [[int(item[0] / 1000), item[1]] for item in data] # this should work right?

# check the level of granularity and need to find days time
def check_range(args):
    unix_day = 86000
    start_unix = to_unixtime(args.get('from'))
    end_unix = to_unixtime(args.get('to')) + unix_day
    days = (end_unix - start_unix) / unix_day
    return days

# eww it's ugly but it works, refactor later
def find_days_time(data, args):
    if check_range(args) > 90: # amounts over 90 days work as is without finding days value
        return data
    low_hours = 7166 # 2 hours
    high_hours = 10750 # 3 hours
    unix_day = 86000
    start_day = to_unixtime(args.get('from'))
    days_values = []
    for item in data:
        if item[0] > start_day + low_hours and item[0] < start_day + high_hours:
            days_values.append(item)
            start_day = start_day + unix_day
    return days_values
