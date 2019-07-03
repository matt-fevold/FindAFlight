import json

with open('../resources/destinations.json') as file:
    destination_list = json.load(file)


def get_destination(destination_id):
    for destination in destination_list:
        if destination['PlaceId'] == destination_id:
            return destination

