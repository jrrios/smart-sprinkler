import googlemaps
import urllib

gmaps = googlemaps.Client(key='AIzaSyB5L7V0QPYkRGBapeWuQ6gNm9IgB6dSUos')


def get_geocoding(address):
    return gmaps.geocode(urllib.quote_plus(address))


def get_lat_lon(geocode_result):
    return geocode_result[0][u'geometry'][u'location']


def get_formatted_address(geocode_result):
    return geocode_result[0][u'formatted_address']


def get_city_and_state(geocode_result):
    city = 'Unknown'
    state = 'N/A'
    for component in geocode_result[0][u'address_components']:
        if u'locality' in component[u'types']:
            city = component[u'long_name']
        else:
            if u'administrative_area_level_1' in component[u'types']:
                state = component[u'short_name']
    return city,state


def example_usage_for_address(address):
    print "Query "+address
    geocode = get_geocoding(address)
    formatted_address = get_formatted_address(geocode)
    print "\tCity %s, %s" % get_city_and_state(geocode)
    location = get_lat_lon(geocode)
    print "\tAddress %s\n\tLat,Lon: %f,%f\n" % (formatted_address, location[u'lat'], location[u'lng'])


def example_usage():
    example_usage_for_address("1600 Amphitheatre Parkway, Mountain View, CA")
    example_usage_for_address("St. Edwards, 3001 S. Congress, Austin, Texas")
    example_usage_for_address("McMurdo Station, Antartica")


#example_usage()