from get_destination import get_destination
from datetime import datetime, timedelta


def pretty_print(flight, indent_level):
    if get_destination(flight['OutboundLeg']['DestinationId']) is None:
        return
    print("\t "*indent_level, flight['MinPrice'], "\t",
          flight['OutboundLeg']['DepartureDate'][0:10],"\t",
          get_destination(flight['OutboundLeg']['DestinationId'])['IataCode'], "\t",
          get_destination(flight['OutboundLeg']['DestinationId'])['Name'])

def remove_local_destinations(quotes):
    # filter out places i'd never fly to
    # 84790 - theif river falls
    # 47448 - duluth
    local_flights = ["84790", "47448"]
    for i, quote in enumerate(quotes):
      if str(quote['OutboundLeg']['DestinationId']) in local_flights:
        quotes.pop(i)
    return quotes


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
