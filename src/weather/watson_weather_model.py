import json

import requests

import geocoding

# Local variables (hardcoded for now)
language_code = 'en-US'
units_code = 'e' # English (imperial) units
forecast_range = 6 # Number of hours of forecasts to look at
history_range = 24 # Number of hours of history to look at

# Service constants
service_username = 'cf2b9be6-e01e-454f-8f52-dd9ee9f12282'
service_password = 'Pw7SIihDTH'
service_host = 'twcservice.mybluemix.net'
service_base_url = 'https://' + service_username + ':' + service_password + '@' + service_host + '/api/weather/v2/'


def get_current_conditions(latitude, longitude):
    service_url = service_base_url + '/observations/current?geocode=' + str(latitude) + '%2C' + str(longitude) + '&language=' + language_code + '&units=' +units_code
    response = requests.get(service_url)
    return json.loads(response.text)


def get_forecast(latitude, longitude):
    service_url = service_base_url + '/forecast/hourly/24hour?geocode=' + str(latitude) + '%2C' + str(longitude) + '&language=' + language_code + '&units=' +units_code
    response = requests.get(service_url)
    return json.loads(response.text)


def get_measurement_type(units):
    return {
        'e': u'imperial',
        'h': u'uk_hybrid',
        'm': u'metric',
        's': u'metric_si'
        }[units]


def get_recent_precip_range(hours):
    if hours <= 1 :
        return 'precip_1hour'
    else:
        if hours <= 6 :
            return u'precip_6hour'
        else :
            return u'precip_24hour'


def get_recent_precipitation(conditions):
    measurement = get_measurement_type(units_code)
    range = get_recent_precip_range(history_range)
    return conditions[u'observation'][measurement][range]


def get_recent_snow_range(hours):
    if hours <= 1:
        return u'snow_1hour'
    else:
        if hours <= 6:
            return u'snow_6hour'
        else :
            return u'snow_24hour'


def get_recent_snow(conditions):
    measurement = get_measurement_type(units_code)
    range = get_recent_snow_range(history_range)
    return conditions[u'observation'][measurement][range]


def get_current_temp(conditions):
    measurement = get_measurement_type(units_code)
    return conditions[u'observation'][measurement][u'temp']


def get_forecast_precipitation_range(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast[u'forecasts']
    precip = []
    # Grab the precip type and percentage for the given range of hours
    for index in range(0, min(forecast_range, len(forecasts))):
        precip.append((forecasts[index][u'precip_type'],forecasts[index][u'pop']))
    return precip


def get_forecast_precipitation(forecast):
    precip_range = get_forecast_precipitation_range(forecast)
    max_precip = (u'precip', 0)
    for value in precip_range:
        if value[1] >= max_precip[1]:
            max_precip = value
    return max_precip

def get_forecast_temps(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast[u'forecasts']
    temps = []
    for index in range(0, min(forecast_range, len(forecasts))):
        temps.append(forecasts[index][u'temp'])
    return temps


def get_min_forecast_temp(forecast):
    return min(get_forecast_temps(forecast))


def get_max_forecast_temp(forecast):
    return max(get_forecast_temps(forecast))


def example_for_location(address):
    print("\nWeather Conditions at "+address)
    geocode = geocoding.get_geocoding(address)
    place = geocoding.get_lat_lon(geocode)
    latitude = place[u'lat']
    longitude = place[u'lng']

    conditions = get_current_conditions(latitude, longitude)
    print 'Current temp:', get_current_temp(conditions)
    print 'Recent precipitation:', get_recent_precipitation(conditions)
    print 'Recent snow:', get_recent_snow(conditions)

    forecast = get_forecast(latitude, longitude)
    print 'Forecast precipitation (next',forecast_range,'hours):', get_forecast_precipitation(forecast)
    print 'Forecast min temp (next',forecast_range,'hours):', get_min_forecast_temp(forecast)
    print 'Forecast max temp (next',forecast_range,'hours):', get_max_forecast_temp(forecast)


def example_usage():
    example_for_location("St. Edwards, 3001 S. Congress, Austin, Texas")
    example_for_location("McMurdo Station, Antartica")
    example_for_location("Gobi Desert")

#example_usage()