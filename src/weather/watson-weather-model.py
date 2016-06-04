import requests
import json

# Local variables (hardcoded for now)
language_code = 'en-US'
units_code = 'e' # English (imperial) units
latitude = '30.23'
longitude = '-97.76'
forecast_range = 6 # Number of hours of forecasts to look at

# Service constants
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

def get_recent_precipitation(conditions):
    measurement = get_measurement_type(units_code)
    return conditions['observation'][measurement]['precip_6hour']

def get_recent_snow(conditions):
    measurement = get_measurement_type(units_code)
    return conditions['observation'][measurement]['snow_6hour']

def get_current_temp(conditions):
    measurement = get_measurement_type(units_code)
    return conditions['observation'][measurement]['temp']

def get_forecast_precipitation(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast['forecasts']
    precip = []
    for index in range(0,forecast_range):
        precip.append(forecasts[index]['precip_type'])
    return list(set(precip))

def get_forecast_temps(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast['forecasts']
    temps = []
    for index in range(0,forecast_range):
        temps.append(forecasts[index]['temp'])
    return temps

def get_min_forecast_temp(forecast):
    return min(get_forecast_temps(forecast))

def get_max_forecast_temp(forecast):
    return max(get_forecast_temps(forecast))

def example_usage():
    conditions = get_current_conditions(latitude, longitude)
    print 'Current temp:', get_current_temp(conditions)
    print 'Recent precipitation:', get_recent_precipitation(conditions)
    print 'Recent snow:', get_recent_snow(conditions)

    forecast = get_forecast(latitude, longitude)
    print 'Forecast precipitation (next',forecast_range,'hours):', get_forecast_precipitation(forecast)
    print 'Forecast min temp (next',forecast_range,'hours):', get_min_forecast_temp(forecast)
    print 'Forecast max temp (next',forecast_range,'hours):', get_max_forecast_temp(forecast)

example_usage()