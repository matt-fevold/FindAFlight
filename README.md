# FindAFlight

## setup env

- python3
- setup venv
        - https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv
- requirements.txt has dependencies
- change `secrets-template.json` to `secrets.json`
- create a key on `https://rapidapi.com` and replace it


### what it does
currently, given an airport code (msp, lax, jfk...) it will search for one way flights
under 80$ to a city and flights 2 days later.
I plan to make those number configurable, but for now... 
```
> findaflight --starting-airport=msp
         38.0   2020-04-14      ATL     Atlanta Hartsfield-Jackson
                 39.0   2020-04-16      AUS     Austin-Bergstrom
                 69.0   2020-04-16      BNA     Nashville
                 41.0   2020-04-16      BOS     Boston Logan International
                 39.0   2020-04-16      BWI     Baltimore Washington International
                 57.0   2020-04-16      CLE     Cleveland Hopkins International
                 71.0   2020-04-16      CLT     Charlotte Douglas
                 74.0   2020-04-16      DEN     Denver International
                 38.0   2020-04-16      DFW     Dallas Fort Worth International
                 38.0   2020-04-16      DTW     Detroit Wayne County
                 38.0   2020-04-16      EWR     New York Newark
                 33.0   2020-04-16      FLL     Fort Lauderdale International
                 38.0   2020-04-16      IAH     Houston George Bush Intercntl.
                 38.0   2020-04-16      MCO     Orlando International
                 39.0   2020-04-16      MIA     Miami International
                 75.0   2020-04-16      MKL     Jackson
                 38.0   2020-04-16      MSP     Minneapolis St Paul
                 38.0   2020-04-16      ORD     Chicago O'Hare International
                 57.0   2020-04-16      PHL     Philadelphia International
                 77.0   2020-04-16      PIT     Pittsburgh International
                 29.0   2020-04-16      RDU     Raleigh / Durham
                 69.0   2020-04-16      SLC     Salt Lake City
                 37.0   2020-04-16      TPA     Tampa International
         61.0   2020-04-01      AUS     Austin-Bergstrom
                 68.0   2020-04-03      ATL     Atlanta Hartsfield-Jackson
                 62.0   2020-04-03      BNA     Nashville
                 79.0   2020-04-03      BOS     Boston Logan International
                 63.0   2020-04-03      BWI     Baltimore Washington International
                 66.0   2020-04-03      CVG     Cincinnati Northern Kentucky
                 62.0   2020-04-03      DEN     Denver International
                 62.0   2020-04-03      DTW     Detroit Wayne County
                 70.0   2020-04-03      FLL     Fort Lauderdale International
                 77.0   2020-04-03      LAS     Las Vegas Mccarran
                 63.0   2020-04-03      LAX     Los Angeles International
                 63.0   2020-04-03      MCO     Orlando International
                 57.0   2020-04-03      MSY     New Orleans Louis Armstrong
                 53.0   2020-04-03      PIT     Pittsburgh International
                 79.0   2020-04-03      SAN     San Diego International
                 69.0   2020-04-03      SFO     San Francisco International
                 49.0   2020-04-03      SLC     Salt Lake City
```
