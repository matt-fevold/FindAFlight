from skyscanner_api import get_quotes_and_places
from util import pretty_print, remove_local_destinations, add_days_to_date
from get_destination import get_destination
import click

@click.command()
@click.option('--starting-airport', default="msp")
@click.option('--starting-date', default="anytime", help="Format “yyyy-mm-dd”, “yyyy-mm” or “anytime”")
@click.option('--max-days')
def main(starting_airport, starting_date, max_days):
    first_leg = plan_leg(starting_airport, starting_date)
    #
    for flight in first_leg:
        pretty_print(flight,1)

        current_city = get_destination(flight['OutboundLeg']['DestinationId'])['CityName']
        current_airport = get_destination(flight['OutboundLeg']['DestinationId'])['IataCode']
        flight_date = flight['OutboundLeg']['DepartureDate']

        second_leg = plan_leg(current_airport, add_days_to_date(flight_date, 2))
        for l in second_leg:
            if(starting_airport==get_destination(flight['OutboundLeg']['DestinationId'])['IataCode']):
                print("FOUND WAY HOME")
            pretty_print(l, 2)


            # current_city = get_destination(flight['OutboundLeg']['DestinationId'])['CityName']
            # current_airport = get_destination(flight['OutboundLeg']['DestinationId'])['IataCode']
            # flight_date = flight['OutboundLeg']['DepartureDate']
            #
            # third_leg = plan_leg(current_airport, add_days_to_date(flight_date, 2))
            # for t in third_leg:
            #     if(starting_airport==get_destination(flight['OutboundLeg']['DestinationId'])['IataCode']):
            #         print("FOUND WAY HOME")
            #     pretty_print(t, 3)
    #     leg_start_date = flight['OutboundLeg']['DepartureDate']
    #     latest_next_flight_date = add_days_to_date(leg_start_date, 50)
    #
    #     print("searching for flights departing {} from {} to {}".format(current_airport, leg_start_date[0:10], latest_next_flight_date.strftime("%Y-%m-%d")))
    #
    #     # problem, api doesn't let us say explicit start stop search so likely have to implement that
    #     # problem, currently just giving it any flights on specific date not searching the range. will have to do
    #     # month by month and filter out dates that are outside bound
    #     second_leg = plan_leg(current_airport, 1, latest_next_flight_date.strftime("%Y-%m-%d"))


def plan_leg(start_airport, start_date="anytime", leg=0):
    # get all possible flights from start airport on a date
    quotes, places = get_quotes_and_places(start_airport, start_date)

    # filter out any expensive flights
    cheap_flights = remove_quotes_over_max(quotes, 80)

    # remove any local flights from the first result,
    # on other legs okay - bc might be cheaper to fly back to duluth for example
    if(leg==0):
        non_local_cheap_flights = remove_local_destinations(cheap_flights)


    return non_local_cheap_flights


def remove_quotes_over_max(quotes, max_price):
    # print(quotes)
    low_quotes = []
    for quote in quotes:
        quote_price = quote['MinPrice']
        if quote_price < max_price:
            low_quotes.append(quote)

    return low_quotes


if __name__ == "__main__":
    main()
