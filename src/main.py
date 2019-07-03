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

    print(places)

    write_destination_to_file(places)

    cheap_flights = get_lower_than_price(quotes, 75)

    non_local_cheap_flights = remove_local_destinations(cheap_flights)


    for flight in non_local_cheap_flights:
      print(get_destination(places, flight['OutboundLeg']['DestinationId']))

    # print(len(cheap_flights))


def get_destination(destination_list, destination_id):
    for destination in destination_list:
        if destination['PlaceId'] == destination_id:
            return destination


def get_lower_than_price(quotes, max_price):
    low_quotes = []
    for quote in quotes:
        quote_price = quote['MinPrice']
        if quote_price < max_price:
            low_quotes.append(quote)

    return low_quotes


def remove_local_destinations(quotes):
    # filter out places i'd never fly to
    # 84790 - theif river falls
    local_flights = ["84790"]

    for i, quote in enumerate(quotes):
      if str(quote['OutboundLeg']['DestinationId']) in local_flights:
        quotes.pop(i)

    return quotes


def write_destination_to_file(destination):
  with open("../resources/destinations.json", "w+") as file:
    json.dump(destination, file)


if __name__ == "__main__":
  main()