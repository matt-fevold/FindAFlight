import json
from src.skyscanner_api import call_api

def write_destination_to_file(destination):
    with open("../resources/destinations.json", "w+") as file:
      json.dump(destination, file)


if __name__ == "__main__":
    quotes, places = call_api()

    write_destination_to_file(places)
