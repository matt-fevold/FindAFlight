import requests
import json

with open('../resources/secrets.json') as secrets:
    secrets = json.load(secrets)

with open('../resources/config.json') as config_file:
    data = json.load(config_file)


def main():
    search = "msp/US/anytime?inboundpartialdate=anytime"
    header = {"X-RapidAPI-Host": data['API_HOST'],"X-RapidAPI-Key": secrets['API_KEY']}

    response = requests.get(data['BASE_URL'] + search, headers=header)

    print(response.status_code) # The HTTP status code
    # print(response.content.)
    # print(response.headers) # The HTTP headers
    # print(response.content) # The parsed response
# response.raw_body # The unparsed response


# locations = ["JFK-sky"]

# def build_url(destination):
#   url = data['API_URL']


if __name__ == "__main__":
  main()