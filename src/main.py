import requests
import json

with open('../resources/secrets.json') as secrets:
    secrets = json.load(secrets)

with open('../resources/config.json') as config_file:
    data = json.load(config_file)


def main():
    # build search param and headers
    search = "msp/US/anytime?inboundpartialdate=2019-12-01"
    header = {"X-RapidAPI-Host": data['API_HOST'],"X-RapidAPI-Key": secrets['API_KEY']}

    # make call
    response = requests.get(data['BASE_URL'] + search, headers=header)

    # validate response
    print("RESPONSE CODE: ", response.status_code)

    # parse response into readable format
    quotes = response.json()['Quotes']
    places = response.json()['Places']

    # print(quotes[0])
    print(places)
    cheap_flights = get_lowest_price(quotes, 130)



    for flight in cheap_flights:
      print(get_destination(places, flight['OutboundLeg']['DestinationId'])['Name'])

    print(len(cheap_flights))


def get_destination(destination_list, destination_id):
    for destination in destination_list:
        if destination['PlaceId'] == destination_id:
            return destination


def get_lowest_price(quotes, max_price):
    low_quotes = []
    for quote in quotes:
        quote_price = quote['MinPrice']
        if quote_price < max_price:
            low_quotes.append(quote)

    return low_quotes

def remove_local_destinations(quotes):
    # filter out places i'd never fly to
    local_flights = []
    # for quote in quotes:
    #   if quote['']
    pass

if __name__ == "__main__":
  main()