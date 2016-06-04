import requests
import json

# Local variables (hardcoded for now)
language_code = 'en-US'
units_code = 'e' # English (imperial) units
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
    return {
        'e': 'imperial',
        'h': 'uk_hybrid',
        'm': 'metric',
        's': 'metric_si'
        }[units]


def get_recent_precip_range(hours):
    if hours <= 1 :
        return 'precip_1hour'
    else:
        if hours <= 6 :
            return 'precip_6hour'
        else :
            return 'precip_24hour'


def get_recent_precipitation(conditions):
    measurement = get_measurement_type(units_code)
    range = get_recent_precip_range(forecast_range)
    return conditions['observation'][measurement][range]


def get_recent_snow_range(hours):
    if hours <= 1:
        return 'snow_1hour'
    else:
        if hours <= 6:
            return 'snow_6hour'
        else :
            return 'snow_24hour'


def get_recent_snow(conditions):
    measurement = get_measurement_type(units_code)
    range = get_recent_snow_range(forecast_range)
    return conditions['observation'][measurement][range]


def get_current_temp(conditions):
    measurement = get_measurement_type(units_code)
    return conditions['observation'][measurement]['temp']


def get_forecast_precipitation(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast['forecasts']
    precip = []
    for index in range(0, min(forecast_range, len(forecasts))):
        precip.append(forecasts[index]['precip_type']+":"+str(forecasts[index]['pop']))
    return precip


def get_forecast_temps(forecast):
    measurement = get_measurement_type(units_code)
    forecasts = forecast['forecasts']
    temps = []
    for index in range(0, min(forecast_range, len(forecasts))):
        temps.append(forecasts[index]['temp'])
    return temps


def get_min_forecast_temp(forecast):
    return min(get_forecast_temps(forecast))


def get_max_forecast_temp(forecast):
    return max(get_forecast_temps(forecast))


def example_for_location(location, latitude, longitude):
    print("\nWeather Conditions at "+location)

    conditions = get_current_conditions(latitude, longitude)
    print 'Current temp:', get_current_temp(conditions)
    print 'Recent precipitation:', get_recent_precipitation(conditions)
    print 'Recent snow:', get_recent_snow(conditions)

    forecast = get_forecast(latitude, longitude)
    print 'Forecast precipitation (next',forecast_range,'hours):', get_forecast_precipitation(forecast)
    print 'Forecast min temp (next',forecast_range,'hours):', get_min_forecast_temp(forecast)
    print 'Forecast max temp (next',forecast_range,'hours):', get_max_forecast_temp(forecast)


def example_usage():
    example_for_location("Austin, Texas", '30.2672', '-97.7431')
    example_for_location("McMurdo Station, Antartica", '-77.8419', '166.6863')
    example_for_location("Gobi Desert, China", '42.5900', '103.4300')

example_usage()