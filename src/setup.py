import json
from src.skyscanner_api import get_quotes_and_places

def write_destination_to_file(destination):
    with open("../resources/destinations.json", "w+") as file:
      json.dump(destination, file)


if __name__ == "__main__":
    quotes, places = get_quotes_and_places("msp")

    write_destination_to_file(places)
