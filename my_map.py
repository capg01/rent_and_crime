from geopy.geocoders import Nominatim
import folium
import csv
import numpy as np
import pandas as pd
import base64
from io import BytesIO
import cache as ch

def map_crime(crime_total, m):
    nom = Nominatim()

    for suburb in crime_total:

        if (ch.suburb_lat_lng_db(suburb)) == False:
            address = suburb + ',' + ' ' + 'NSW'
            n = nom.geocode(address, timeout=None)
            ch.insert_into_db(suburb, n.latitude, n.longitude)

        elif (ch.suburb_lat_lng_db(suburb)) == True:

            if (crime_total[suburb] > 5000 and crime_total[suburb] <= 10000):
                lat, lng = ch.retrieve_coordinates(suburb)
                folium.CircleMarker(location=[lat, lng],radius=10, color = '#90EE90', fill = True).add_to(m)
            elif (crime_total[suburb] > 10000 and crime_total[suburb] <= 20000):
                lat, lng = ch.retrieve_coordinates(suburb)
                folium.CircleMarker(location=[lat, lng],radius=20, color = '#FFFF00', fill = True).add_to(m)
            elif crime_total[suburb] > 20000 and crime_total[suburb] <= 30000:
                lat, lng = ch.retrieve_coordinates(suburb)
                folium.CircleMarker(location=[lat, lng],radius=30, color = '#FFA07A', fill = True).add_to(m)
            elif crime_total[suburb] > 30000:
                lat, lng = ch.retrieve_coordinates(suburb)
                folium.CircleMarker(location=[lat, lnge],radius=40, color = '#FF0000', fill = True).add_to(m)

    m.save(outfile='map.html')

def map_it(m):

    with open('rent_details.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            lat = float(line['LATITUDE'])
            lng = float(line['LONGITUDE'])
            rental_address = line['ADDRESS']
            price = line['PRICE']
            carspace = line['CARSPACE']
            popup_info = price + ':' + carspace + ':'  + rental_address

            folium.Marker(location=[lat, lng], popup = popup_info).add_to(m)

    m.save(outfile='map.html')

def station_info(suburb_crime):

    filename = 'StationEntrances2018.csv'

    m = folium.Map(location=[-33.868820, 151.209290],tiles='Openstreetmap' , zoom_start=10)

    with open('station_coordinates.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            lat = float(line['LAT'])
            lng = float(line['LONG'])
            pop_info = line['Train_Station']

            marker = folium.Marker(location=[lat, lng], icon=folium.Icon(color='lightgray',icon='info-sign'), popup=pop_info)
            marker.add_to(m)


    m.save(outfile='map.html')
    map_crime(suburb_crime, m)
    map_it(m)

