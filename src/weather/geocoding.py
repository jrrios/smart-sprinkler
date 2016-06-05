import googlemaps
import urllib

gmaps = googlemaps.Client(key='AIzaSyB5L7V0QPYkRGBapeWuQ6gNm9IgB6dSUos')

def get_lat_lon(address):
    geocode_result = gmaps.geocode(address)
    return geocode_result[0][u'geometry'][u'location']


def example_usage_for_address(address):
    location = get_lat_lon(urllib.quote_plus(address))
    print "Address %s\n\tLat,Lon: %f,%f\n" % (address, location[u'lat'], location[u'lng'])


def example_usage():
    example_usage_for_address("1600 Amphitheatre Parkway, Mountain View, CA")
    example_usage_for_address("St. Edwards University, Austin, TX")
    example_usage_for_address("McMurdo Station, Antartica")


#example_usage()