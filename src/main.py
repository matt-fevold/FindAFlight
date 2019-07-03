from src.skyscanner_api import get_quotes_and_places
from src.get_destination import get_destination

def main():
    quotes, places = get_quotes_and_places("msp")

    # print(places)

    cheap_flights = get_lower_than_price(quotes, 75)

    non_local_cheap_flights = remove_local_destinations(cheap_flights)

    for flight in non_local_cheap_flights:
        print(get_destination(flight['OutboundLeg']['DestinationId']))


def plan_trip(start_airport):
    pass


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




if __name__ == "__main__":
    main()