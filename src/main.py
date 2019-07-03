from src.skyscanner_api import get_quotes_and_places
from src.get_destination import get_destination

def main():
    first_leg = plan_leg("msp")


def plan_leg(start_airport):
    quotes, places = get_quotes_and_places(start_airport)

    # print(places)

    cheap_flights = get_lower_than_price(quotes, 55)

    non_local_cheap_flights = remove_local_destinations(cheap_flights)

    for flight in non_local_cheap_flights:
        pretty_print(flight)



def pretty_print(flight):
  print(flight['MinPrice'], "    ",
        flight['OutboundLeg']['DepartureDate'][5:10],
        get_destination(flight['OutboundLeg']['DestinationId'])['Name'])


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