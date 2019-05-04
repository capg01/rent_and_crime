import psycopg2

def suburb_lat_lng_db(suburb):

    '''This function checks if we have an entry for the suburb and returns
    True, False or None (if something is wrong with the data)'''

    conn = psycopg2.connect(
            host = 'localhost',
            database='suren',
            user='postgres'
            )

    c = conn.cursor()

    #c.execute(""" CREATE TABLE suburb_lat_lng (
    #              suburb text,
    #              latitude decimal,
    #              longitude decimal

    #              )""")

    #c.execute("DELETE FROM suburb_lat_lng WHERE suburb=?", ('Aarons Pass',))
    #conn.commit

    #c.execute("SELECT * FROM suburb_lat_lng")
    c.execute("SELECT suburb_name, latitude, longitude FROM suburb_table WHERE suburb_name = (%s);", [suburb])
    data = c.fetchone()


    if data != None:
        return True
    elif data == None:
        return False

    conn.close()

def insert_into_db(suburb,lat,lng):

    '''This function inserts the suburb/lat/lng into the db if the entry does not exist'''

    conn = psycopg2.connect(
            host = 'localhost',
            database='suren',
            user='postgres'
            )

    c = conn.cursor()

    c.execute("INSERT INTO suburb_table (suburb_name, latitude, longitude) VALUES(%s, %s, %s)", (suburb, lat, lng))
    print('inserted {} into database'.format(suburb))
    conn.commit()
    c.close()
    conn.close()

def retrieve_coordinates(suburb):

    conn = psycopg2.connect(
            host = 'localhost',
            database='suren',
            user='postgres'
            )

    c = conn.cursor()

    c.execute("SELECT latitude,longitude FROM suburb_table WHERE suburb_name = (%s);", [suburb])

    lat = c.fetchone()[0]
    lng = c.fetchone()[1]
    conn.commit()
    c.close()
    conn.close()

    return (lat, lng)

