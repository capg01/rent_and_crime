import sanitise_data as sd
import crime_nsw as crime
import my_map
import json
import ast
import requests
from pprint import pprint

def request_token(username, password):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    data = {
      'grant_type': 'client_credentials',
      'scope': 'api_listings_read api_agencies_read'
      }

    response = requests.post('https://auth.domain.com.au/v1/connect/token', headers=headers, data=data, auth=(username, password))

    access_token = response.text
    token = ast.literal_eval(access_token)

    return access(token)

def access(token):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer' + ' ' + token['access_token']
    }

    data = '{"listingType":"Rent", "propertyTypes":[ "apartmentUnitFlat" ], "minBedrooms":1, "maxBathrooms": 1, "minBathrooms":1,"maxBathrooms": 1, "minCarspaces":0,"maxCarspaces": 1, "minPrice": 400, "maxPrice": 600,"locations":[ { "state":"NSW", "region":"", "area":"", "suburb":"Westmead", "postCode":"", "includeSurroundingSuburbs":false } ]}'

    response = requests.post('https://api.domain.com.au/v1/listings/residential/_search', headers=headers, data=data)

    return response.text

client_id = 'client_05473c1556774ae7a0136ff55c2b2f67'
client_secret = 'secret_bfa61195d913f25d3710386a13bf5713'

json_response = request_token(client_id, client_secret)

json_data = json.loads(json_response)

sd.extract_data(json_data)
suburb_crime = crime.crime_total('Crime_NSW.csv')
my_map.station_info(suburb_crime)
