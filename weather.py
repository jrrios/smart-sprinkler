import requests
import json

# Local variables
language_code = 'en-US'
units_code = 'h'
latitude = '30.23'
longitude = '-97.76'
service_username = 'cf2b9be6-e01e-454f-8f52-dd9ee9f12282'
service_password = 'Pw7SIihDTH'
service_host = 'twcservice.mybluemix.net'
service_base_url = 'https://' + service_username + ':' + service_password + '@' + service_host + '/api/weather/v2/'

def get_current_conditions(latitude, longitude):
    service_url = service_base_url + '/observations/current?geocode=' + latitude + '%2C' + longitude + '&language=' + language_code + '&units=' +units_code
    response = requests.get(service_url)
    return json.loads(response.text)

def get_forecast(latitude, longitude):
    service_url = service_base_url + '/forecast/hourly/24hour?geocode=' + latitude + '%2C' + longitude + '&language=' + language_code + '&units=' +units_code
    response = requests.get(service_url)
    return json.loads(response.text)

def get_measurement_type(units):
    if units == 'e' : return 'imperial'
    else :
        if units == 'h' : return 'uk_hybrid'
        else : return 'metric'

def get_recent_precipitation(latitude, longitude):
    conditions = get_current_conditions(latitude, longitude)
    measurement = get_measurement_type(units_code)
    return conditions['observation'][measurement]['precip_6hour']

print 'Recent precipitation: ', get_recent_precipitation(latitude,longitude)

