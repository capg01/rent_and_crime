import csv
import re

def extract_data(json_data):

    with open('rent_details.csv','w') as f:
        fieldnames = ['PRICE', 'ADDRESS', 'LATITUDE', 'LONGITUDE','CARSPACE']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

    for i, listing in enumerate(json_data):
        apt_price = json_data[i]['listing']['priceDetails']['displayPrice']

        try:
            apt_price = clean_apt_price(apt_price)
        except AttributeError:
            print('display price not formatted correctly on website')

        try:
            carspace = json_data[i]['listing']['propertyDetails']['carspaces']
        except KeyError:
            carspace = 0

        address = json_data[i]['listing']['propertyDetails']['displayableAddress']
        latitude = json_data[i]['listing']['propertyDetails']['latitude']
        longitude = json_data[i]['listing']['propertyDetails']['longitude']

        write_to_file = [apt_price, carspace, address, latitude, longitude]

        with open('rent_details.csv','a') as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
            csv_writer.writerow({
                'PRICE' : write_to_file[0], 'ADDRESS' : write_to_file[2], 'LATITUDE':write_to_file[3],
                'LONGITUDE':write_to_file[4], 'CARSPACE':write_to_file[1]
                })

def clean_apt_price(price):

    clean_price = re.search(r'(\$\d\d\d)', price)
    return clean_price.group(0)

