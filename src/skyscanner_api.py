import requests
import json
from datetime import datetime, timedelta


with open('../resources/secrets.json') as secrets:
    secrets = json.load(secrets)

with open('../resources/config.json') as config_file:
    data = json.load(config_file)


def get_quotes_and_places(airport, start_date="anytime"):
    # build search param and headers
    if start_date == "anytime":
        search = airport + "/US/" + start_date
    else:
        search = airport + "/US/" + start_date.strftime("%Y-%m-%d")
    header = {"X-RapidAPI-Host": data['API_HOST'], "X-RapidAPI-Key": secrets['API_KEY']}

    # make call
    response = requests.get(data['BASE_URL'] + search, headers=header)

    # validate response
    if response.status_code != 200:
        print("RESPONSE CODE: ", response.status_code)
        exit(1)

    # parse response into readable format
    quotes = response.json()['Quotes']
    places = response.json()['Places']
    return quotes, places
