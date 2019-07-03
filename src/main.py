from src.skyscanner_api import get_quotes_and_places
from src.get_destination import get_destination
from datetime import datetime, timedelta

def main():
    # add_days_to_date("2019-08-27T00:00:00",13)
    # print(datetime.strptime("2019-08-27", "%Y-%m-%d"))
    # print(datetime.today() + timedelta(2))
    first_leg = plan_leg("msp", 0, "anytime")

    for flight in first_leg:
        # current_city = get_destination(flight['OutboundLeg']['DestinationId'])['CityName']
        current_airport = get_destination(flight['OutboundLeg']['DestinationId'])['IataCode']
        leg_start_date = flight['OutboundLeg']['DepartureDate']
        latest_next_flight_date = add_days_to_date(leg_start_date, 50)

        print("searching for flights departing {} from {} to {}".format(current_airport, leg_start_date[0:10], latest_next_flight_date.strftime("%Y-%m-%d")))

        # problem, api doesn't let us say explicit start stop search so likely have to implement that
        # problem, currently just giving it any flights on specific date not searching the range. will have to do
        # month by month and filter out dates that are outside bound
        second_leg = plan_leg(current_airport, 1, latest_next_flight_date.strftime("%Y-%m-%d"))


# Example
# 2019-08-27T00:00:00
def add_days_to_date(date, number_days):
    # strip off 'T00:00:00'
    stripped_date = strip_date(date)

    # turn into datetime object
    datetime_object = datetime.strptime(stripped_date, "%Y-%m-%d")

    # add days to datetimeobject
    future_date = datetime_object + timedelta(number_days)

    return future_date


def days_at_leg(number_of_days):
    pass


def strip_date(date):
    return date[0:10]


def plan_leg(start_airport, leg=0, start_date="anytime"):
    quotes, places = get_quotes_and_places(start_airport, start_date)

    # print(places)

    cheap_flights = get_lower_than_price(quotes, 55)

    non_local_cheap_flights = remove_local_destinations(cheap_flights)

    # for flight in non_local_cheap_flights:
    #     pretty_print(flight, leg)

    return non_local_cheap_flights


def pretty_print(flight, indent_level):
    print("    "*indent_level, flight['MinPrice'], "    ",
          flight['OutboundLeg']['DepartureDate'][0:10],
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