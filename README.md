# bt_analyzer
Technical assignment for Vincit Rising Star program. Analyzes bitcoin market value for a given date range.

## Pre-requisites

Python > 3.7 \
Docker > 20.10

## Installation

### Virtual environment:

For development create and activate virtual environent:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements to venv:
```bash
pip install -r requirements.txt
```

Set env variables in .env:
```bash
FLASK_APP=main.py
FLASK_ENV=development/testing/production
```

Run the project:
```bash
flask run
```

### Docker:

Building the docker image:
```bash
docker build -t bt_analyzer .
```

Running the image:
```bash
docker run -d -p 5000:5000 --name bt_analyzer bt_analyzer
```

## Usage

Head over to http://localhost:5000/ for the app landing page. It will have a simple description of the api endpoints.
This will also be deployed to Heroku, address for that is coming later.

### API

/api/bearish\
Returns the longest downward trend for given daterange. 

/api/volume\
Returns the highest volume for given daterange.

/api/time_machine\
Returns buy_date and sell_date for given range. Returns null as days if there are no days where money could be made or if the range is less than 2 days.

All endpoints take following parameters:
id: (string) Id of the chosen coin (bitcoint etc.). Defaults to bitcoin.\
vs_currency: (string) Target currency of market data (usd, eur, jpy, etc.). Defaults to eur.\
from*: (string) Starting date for daterange.\
to*: (string) Ending date for daterange.

*required field


### Example usage:

Basic request that defaults to bitcoin and eur:

/time_machine?to=2021-01-19&from=2021-05-20

with other currency:

/volume?vs_currency=jpy&to=2021-01-19&from=2021-05-20

with other coin:

/bearish?id=ethereum&vs_currency=usd&to=2021-01-19&from=2021-05-20