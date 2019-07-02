import requests
import json

with open('../resources/secrets.json') as secrets:
    secrets = json.load(secrets)

with open('../resources/config.json') as config_file:
    data = json.load(config_file)


def main():
    search = "msp/US/inboundpartialdate=2019-12-01"
    header = {"X-RapidAPI-Host": data['API_HOST'],"X-RapidAPI-Key": secrets['API_KEY']}

    response = requests.get(data['BASE_URL'] + search, headers=header)

    quotes = response.json()['Quotes']
    places = response.json()['Places']

    print(response.status_code)

    print(len(quotes))
    print(len(places))


if __name__ == "__main__":
  main()